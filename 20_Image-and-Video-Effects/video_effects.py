"""Apply an OpenCV effect to a webcam or video, optionally saving results."""

import argparse
import math
from pathlib import Path
import sys

import cv2 as cv

from effects import EFFECT_NAMES, apply_effect


def positive_int(value: str) -> int:
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("Must be a positive integer.")
    return number


def positive_float(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise argparse.ArgumentTypeError("Must be a finite positive number.")
    return number


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source", default="0", help="Camera index (e.g. 0) or local video path."
    )
    parser.add_argument("--effect", choices=EFFECT_NAMES, default="cartoon")
    parser.add_argument(
        "--output", type=Path, help="Save processed video as .mp4 or .avi."
    )
    parser.add_argument(
        "--output-fps", type=positive_float,
        help="Override output frame rate; otherwise use source FPS or 30."
    )
    parser.add_argument(
        "--no-display", action="store_true", help="Run without opening a window."
    )
    parser.add_argument(
        "--max-frames", type=positive_int,
        help="Stop after this many frames, useful for a short smoke test."
    )
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    source = int(args.source) if args.source.isdecimal() else args.source
    if isinstance(source, int) and args.no_display and args.max_frames is None:
        parser.error("A camera with --no-display also requires --max-frames.")
    if args.output and args.output.suffix.lower() not in (".mp4", ".avi"):
        parser.error("--output must use the .mp4 or .avi extension.")
    if isinstance(source, str) and args.output:
        if Path(source).resolve() == args.output.resolve():
            parser.error("The output path must differ from the source video path.")

    capture = None
    writer = None
    processed = 0
    try:
        if isinstance(source, str) and not Path(source).is_file():
            raise FileNotFoundError(f"Input video not found: {source}")
        capture = cv.VideoCapture(source)
        if not capture.isOpened():
            raise RuntimeError(f"Could not open camera or video: {args.source}")
        fps = args.output_fps or capture.get(cv.CAP_PROP_FPS)
        if not math.isfinite(fps) or fps <= 0:
            fps = 30.0

        while args.max_frames is None or processed < args.max_frames:
            success, frame = capture.read()
            if not success:
                if processed == 0:
                    raise RuntimeError("The source opened but provided no readable frames.")
                if isinstance(source, int):
                    raise RuntimeError("The camera stopped providing frames.")
                break

            result = apply_effect(frame, args.effect)
            if args.output:
                # Most video encoders expect three channels even for gray effects.
                encoded_frame = (
                    cv.cvtColor(result, cv.COLOR_GRAY2BGR)
                    if result.ndim == 2 else result
                )
                if writer is None:
                    args.output.parent.mkdir(parents=True, exist_ok=True)
                    codec = "mp4v" if args.output.suffix.lower() == ".mp4" else "MJPG"
                    height, width = encoded_frame.shape[:2]
                    writer = cv.VideoWriter(
                        str(args.output), cv.VideoWriter_fourcc(*codec), fps,
                        (width, height), isColor=True,
                    )
                    if not writer.isOpened():
                        raise RuntimeError(f"Could not create output video: {args.output}")
                writer.write(encoded_frame)

            processed += 1
            if not args.no_display:
                cv.imshow(f"Effect: {args.effect} (q to quit)", result)
                if cv.waitKey(1) & 0xFF == ord("q"):
                    break

        print(f"Processed {processed} frames with effect '{args.effect}'.")
        if args.output:
            print(f"Saved video: {args.output} ({fps:g} FPS metadata)")
        return 0
    except (OSError, ValueError, RuntimeError, cv.error) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    finally:
        if capture is not None:
            capture.release()
        if writer is not None:
            writer.release()
        if not args.no_display:
            try:
                cv.destroyAllWindows()
            except cv.error:
                pass


if __name__ == "__main__":
    raise SystemExit(main())
