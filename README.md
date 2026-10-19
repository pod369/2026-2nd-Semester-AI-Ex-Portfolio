# 2026년 2학기 AI-Ex 포트폴리오

영상처리·컴퓨터 비전·딥러닝 실습 6개를 **각각 독립된 공개 저장소**로 정리했습니다. 이 저장소는 프로젝트를 안내하는 목차입니다. 각 링크에서 실행 코드, 원본 `reference/`, 설치 방법, 실험 설명을 확인할 수 있습니다.

| 번호 | 개별 저장소 | 주제 | 기술 | 검증 상태 |
|---|---|---|---|---|
| 1 | [SIFT-Matching-and-Homography](https://github.com/pod369/SIFT-Matching-and-Homography) | SIFT 특징점 매칭·호모그래피 | OpenCV, SIFT, FLANN, RANSAC | 기본 입력 실행·결과 저장 확인 |
| 2 | [Superpixel-and-Normalized-Cut](https://github.com/pod369/Superpixel-and-Normalized-Cut) | 슈퍼픽셀·그래프 기반 영상 분할 | SLIC, RAG, Normalized Cut | 기본 입력 실행·결과 저장 확인 |
| 3 | [Edge-and-Contour-Detection](https://github.com/pod369/Edge-and-Contour-Detection) | 경계·윤곽선 검출 | Sobel, Canny, contours | 기본 입력 실행·결과 저장 확인 |
| 4 | [Image-and-Video-Effects](https://github.com/pod369/Image-and-Video-Effects) | 사진·동영상 효과 | OpenCV, emboss, cartoon, sketch, oil | 사진 5종·동영상 파일 처리 확인 |
| 5 | [MNIST-Handwritten-Digit-Recognition](https://github.com/pod369/MNIST-Handwritten-Digit-Recognition) | 손글씨 숫자 인식 | TensorFlow, MLP, MNIST | 학습·마우스 GUI 코드 포함 / 새 학습 미수행 |
| 6 | [YOLO-Hangul-Text-Detection](https://github.com/pod369/YOLO-Hangul-Text-Detection) | 한글 손글씨 영역 탐지 | YOLOv8n, Ultralytics | 학습·추론·평가 코드 포함 / 데이터·가중치 별도 준비 |

## 구성과 출처

- 원본: [pod369/Image-processing-4](https://github.com/pod369/Image-processing-4), 기준 커밋 `b2f9a5b94bbe353cce22ce469e358bb2715759ce`.
- 원본 실습 파일과 입력 이미지의 바이트를 보존하고 각 `SOURCE_MANIFEST.json`에 해시를 기록했습니다.
- 실행 경로를 개별 저장소 구조로 바꾸고, CLI·오류 처리·결과 저장·사용법을 정리했습니다.
- 1~4번은 입력 이미지와 실제 결과 자료를 포함합니다. 기존 `results/`는 2026-10-14 실행 기록이며, 2026-10-19 개별 저장소 경로에서도 기본 실행을 확인했습니다.
- 5~6번은 새 모델 학습이나 새로운 성능 측정을 수행하지 않았습니다. 한글 노트북의 과거 검증 로그는 새 시험 성능과 구분해 표시했습니다. 한글 탐지는 영역 검출이며 OCR은 포함하지 않습니다.

## 확인 결과

2026-10-19: 6개 저장소 모두 공개 상태이며, 총 95개 파일의 Git blob SHA를 로컬 준비본과 대조해 일치함을 확인했습니다. 각 프로젝트의 원본 코드, 실행 안내, 요구 패키지와 결과 또는 실행 제약을 구분했습니다.
