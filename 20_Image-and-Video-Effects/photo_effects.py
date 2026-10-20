"""Generate five photo effects without a display, or preview with --show."""

import argparse
from pathlib import Path
import sys

import cv2 as cv

from effects import EFFECT_NAMES, apply_effect


PROJECT_DIR = Path(__file__).resolve().parent
DEFAULT_IMAGE = PROJECT_DIR / "assets" / "river.jpg"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "image", nargs="?", type=Path, default=DEFAULT_IMAGE,
        help="Input image path (default: repository assets/river.jpg).",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=PROJECT_DIR / "outputs" / "photo",
        help="Directory for all five PNG results.",
    )
    parser.add_argument(
        "--show", action="store_true",
        help="Show the original and results; press any key to close them.",
    )
    return parser


def main(argv=None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if not args.image.is_file():
            raise FileNotFoundError(f"Input image not found: {args.image}")
        image = cv.imread(str(args.image), cv.IMREAD_COLOR)
        if image is None:
            raise ValueError(f"OpenCV could not decode the image: {args.image}")
        args.output_dir.mkdir(parents=True, exist_ok=True)
        if args.show:
            cv.imshow("Original", image)
        for effect in EFFECT_NAMES:
            result = apply_effect(image, effect)
            output = args.output_dir / f"{args.image.stem}_{effect}.png"
            if not cv.imwrite(str(output), result):
                raise OSError(f"Could not save image: {output}")
            print(f"Saved {effect}: {output}")
            if args.show:
                cv.imshow(effect, result)
        if args.show:
            cv.waitKey(0)
        return 0
    except (OSError, ValueError, RuntimeError, cv.error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    finally:
        if args.show:
            try:
                cv.destroyAllWindows()
            except cv.error:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
