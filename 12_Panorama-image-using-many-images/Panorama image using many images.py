import cv2
import numpy as np
from pathlib import Path


folder = Path(__file__).resolve().parent

image_paths = sorted(list(folder.glob('*.jpg')) + list(folder.glob('*.png')))

images = []

for path in image_paths:
    img = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if img is not None:
        images.append(img)

print('Loaded images:', len(images))

if len(images) < 2:
    print('이미지가 2장 이상 필요합니다.')
    exit()


stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
stitcher.setPanoConfidenceThresh(0.3)

ret, pano = stitcher.stitch(images)


if ret == cv2.Stitcher_OK:
    pano = cv2.resize(pano, dsize=(0, 0), fx=0.2, fy=0.2)
    cv2.imshow('panorama', pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Error during stitching')
    print('Error code:', ret)