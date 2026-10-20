"""Reusable OpenCV effects for BGR images and video frames."""

import cv2 as cv
import numpy as np


EFFECT_NAMES = ("emboss", "cartoon", "pencil-gray", "pencil-color", "oil")


def apply_effect(image: np.ndarray, effect: str) -> np.ndarray:
    """Apply one effect to a uint8 BGR image; some effects return grayscale.

    Parameters follow the original photo/video scripts. This function neither
    opens windows nor writes files, so it can also be used by other programs.
    """
    if not isinstance(image, np.ndarray) or image.size == 0:
        raise ValueError("The input image must be a nonempty NumPy array.")
    if image.dtype != np.uint8 or image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("The input image must have uint8 BGR format (H, W, 3).")
    if effect not in EFFECT_NAMES:
        raise ValueError(f"Unknown effect: {effect}. Choose from {EFFECT_NAMES}.")

    if effect == "emboss":
        kernel = np.array([[-1.0, 0.0, 0.0],
                           [0.0, 0.0, 0.0],
                           [0.0, 0.0, 1.0]], dtype=np.float32)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        response = cv.filter2D(gray, cv.CV_16S, kernel)
        return np.clip(response + 128, 0, 255).astype(np.uint8)
    if effect == "cartoon":
        return cv.stylization(image, sigma_s=60, sigma_r=0.45)
    if effect in ("pencil-gray", "pencil-color"):
        gray, color = cv.pencilSketch(
            image, sigma_s=60, sigma_r=0.07, shade_factor=0.02
        )
        return gray if effect == "pencil-gray" else color

    if not hasattr(cv, "xphoto") or not hasattr(cv.xphoto, "oilPainting"):
        raise RuntimeError(
            "Oil painting requires opencv-contrib-python. Install the project's "
            "requirements in a clean environment without opencv-python."
        )
    return cv.xphoto.oilPainting(image, 10, 1, cv.COLOR_BGR2Lab)
