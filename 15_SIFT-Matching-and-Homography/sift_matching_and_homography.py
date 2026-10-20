"""Detect SIFT features, match a template, and estimate its planar location."""

import argparse
import json
from pathlib import Path
import time

import cv2 as cv
import numpy as np


PROJECT_DIR = Path(__file__).resolve().parent
ASSET_DIR = PROJECT_DIR / "assets"


def recorded_path(path):
    resolved = path.resolve()
    try:
        return resolved.relative_to(PROJECT_DIR).as_posix()
    except ValueError:
        return str(resolved)


def read_image(path):
    image = cv.imread(str(path), cv.IMREAD_COLOR)
    if image is None:
        raise ValueError(f"Could not read image: {path}")
    return image


def write_image(path, image):
    if not cv.imwrite(str(path), image):
        raise OSError(f"Could not save image: {path}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=ASSET_DIR / "mot_color70.jpg")
    parser.add_argument("--target", type=Path, default=ASSET_DIR / "mot_color83.jpg")
    parser.add_argument("--crop", type=int, nargs=4, default=(440, 190, 560, 350),
                        metavar=("X1", "Y1", "X2", "Y2"),
                        help="Template rectangle in the source image; default preserves the original crop.")
    parser.add_argument("--ratio", type=float, default=0.7, help="Lowe ratio threshold, between 0 and 1.")
    parser.add_argument("--ransac-threshold", type=float, default=5.0, help="Reprojection threshold in pixels.")
    parser.add_argument("--output-dir", type=Path, default=PROJECT_DIR / "outputs")
    parser.add_argument("--show", action="store_true", help="Open result windows; requires a GUI-enabled OpenCV build.")
    args = parser.parse_args()
    if not 0 < args.ratio < 1 or args.ransac_threshold <= 0:
        parser.error("--ratio must be between 0 and 1, and --ransac-threshold must be positive.")
    try:
        source, target = read_image(args.source), read_image(args.target)
    except ValueError as exc:
        parser.error(str(exc))
    x1, y1, x2, y2 = args.crop
    height, width = source.shape[:2]
    if not (0 <= x1 < x2 <= width and 0 <= y1 < y2 <= height):
        parser.error(f"Invalid --crop for a {width} x {height} source image: {args.crop}")
    template = source[y1:y2, x1:x2].copy()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    cv.setRNGSeed(0)
    started = time.perf_counter()
    sift = cv.SIFT_create()
    template_keypoints, template_descriptors = sift.detectAndCompute(cv.cvtColor(template, cv.COLOR_BGR2GRAY), None)
    target_keypoints, target_descriptors = sift.detectAndCompute(cv.cvtColor(target, cv.COLOR_BGR2GRAY), None)
    feature_seconds = time.perf_counter() - started
    good_matches, matching_seconds = [], 0.0
    metrics = {
        "source": recorded_path(args.source), "target": recorded_path(args.target),
        "crop_xyxy": list(args.crop), "ratio_threshold": args.ratio,
        "ransac_threshold_pixels": args.ransac_threshold,
        "template_keypoints": len(template_keypoints), "target_keypoints": len(target_keypoints),
        "feature_seconds": feature_seconds, "good_matches": 0, "inliers": 0,
        "status": "insufficient_features", "homography": None, "projected_corners_xy": None,
        "opencv_version": cv.__version__,
    }
    if template_descriptors is not None and target_descriptors is not None and len(target_descriptors) >= 2:
        started = time.perf_counter()
        matcher = cv.FlannBasedMatcher(dict(algorithm=1, trees=5), dict(checks=50))
        for neighbors in matcher.knnMatch(template_descriptors, target_descriptors, k=2):
            if len(neighbors) == 2:
                first, second = neighbors
                if first.distance < args.ratio * second.distance:
                    good_matches.append(first)
        matching_seconds = time.perf_counter() - started
        metrics["status"] = "insufficient_matches"
    metrics["good_matches"] = len(good_matches)
    metrics["matching_seconds"] = matching_seconds
    localized = target.copy()
    inlier_matches = []
    if len(good_matches) >= 4:
        source_points = np.float32([template_keypoints[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        target_points = np.float32([target_keypoints[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        started = time.perf_counter()
        homography, mask = cv.findHomography(source_points, target_points, cv.RANSAC, args.ransac_threshold)
        metrics["homography_seconds"] = time.perf_counter() - started
        metrics["status"] = "homography_failed"
        if homography is not None and mask is not None and np.isfinite(homography).all():
            inlier_matches = [m for m, keep in zip(good_matches, mask.ravel()) if keep]
            metrics["inliers"] = len(inlier_matches)
            metrics["inlier_ratio"] = len(inlier_matches) / len(good_matches)
            template_h, template_w = template.shape[:2]
            corners = np.float32([[0, 0], [0, template_h - 1],
                                  [template_w - 1, template_h - 1], [template_w - 1, 0]]).reshape(-1, 1, 2)
            projected = cv.perspectiveTransform(corners, homography)
            # Do not cast non-finite or enormous values to integer drawing coordinates.
            if len(inlier_matches) >= 4 and np.isfinite(projected).all() and np.max(np.abs(projected)) < 1_000_000:
                metrics["status"] = "homography_estimated"
                metrics["homography"] = homography.tolist()
                metrics["projected_corners_xy"] = projected.reshape(-1, 2).tolist()
                cv.polylines(localized, [np.rint(projected).astype(np.int32)], True, (0, 255, 0), 3)
    results = {
        "template.png": template,
        "template_keypoints.png": cv.drawKeypoints(template, template_keypoints, None,
                                                    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS),
        "target_keypoints.png": cv.drawKeypoints(target, target_keypoints, None,
                                                  flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS),
        "good_matches.png": cv.drawMatches(template, template_keypoints, target, target_keypoints,
                                            good_matches, None, flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS),
        "inlier_matches_and_location.png": cv.drawMatches(template, template_keypoints, localized,
                                                           target_keypoints, inlier_matches, None,
                                                           flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS),
        "localized_target.png": localized,
    }
    for name, result in results.items():
        write_image(args.output_dir / name, result)
    (args.output_dir / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(metrics, ensure_ascii=False, indent=2))
    print(f"Saved results to {args.output_dir.resolve()}")
    if args.show:
        for name, result in results.items():
            cv.imshow(name, result)
        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == "__main__":
    main()
