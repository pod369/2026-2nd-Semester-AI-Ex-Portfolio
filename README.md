# AI-EX-Portfolio

2026학년도 2학기 AI-Ex 포트폴리오 20개 항목 통합 목차 및 실습 코드 모음.

- 제출 문서: `AI-Ex 포트폴리오 학기 제출원_2025254001_노경진.pdf` (첨부 문서의 2쪽 표 기준)
- 포트폴리오 수: **20**
- 각 폴더는 PDF에 기재된 항목 번호와 프로젝트명을 사용합니다.
- 기존 개별 저장소의 원본 코드/노트북을 가져왔으며, 원래의 저장소는 보존했습니다.

## Index

| No. | Portfolio directory | Type | Listed date | Original repository |
|---:|---|---|---|---|
| 1 | [numpy_basics_with_matplotlib](./01_numpy_basics_with_matplotlib) | Python | 2025-09-23 | [Source](https://github.com/pod369/numpy_basics_with_matplotlib) |
| 2 | [pandas_string_handling_practice](./02_pandas_string_handling_practice) | Python | 2025-09-23 | [Source](https://github.com/pod369/pandas_string_handling_practice) |
| 3 | [text_preprocessing_examples](./03_text_preprocessing_examples) | Python | 2025-09-23 | [Source](https://github.com/pod369/text_preprocessing_examples) |
| 4 | [Basic-Text-Preprocessing-in-Python](./04_Basic-Text-Preprocessing-in-Python) | Jupyter | 2025-12-17 | [Source](https://github.com/pod369/Basic-Text-Preprocessing-in-Python) |
| 5 | [Gradient-Descent-Method](./05_Gradient-Descent-Method) | Jupyter | 2025-12-17 | [Source](https://github.com/pod369/Gradient-Descent-Method) |
| 6 | [Linear-Regression-with-univariate](./06_Linear-Regression-with-univariate) | Jupyter | 2025-12-17 | [Source](https://github.com/pod369/Linear-Regression-with-univariate) |
| 7 | [Linear-Regression-Multivariate](./07_Linear-Regression-Multivariate) | Jupyter | 2025-12-17 | [Source](https://github.com/pod369/Linear-Regression-Multivariate) |
| 8 | [Read-and-Display-Image-in-Grayscale](./08_Read-and-Display-Image-in-Grayscale) | Python | 2026-03-24 | [Source](https://github.com/pod369/Read-and-Display-Image-in-Grayscale) |
| 9 | [BGR-to-YUV-Color-Space-Conversion-and-Channel-Splitting](./09_BGR-to-YUV-Color-Space-Conversion-and-Channel-Splitting) | Python | 2026-03-24 | [Source](https://github.com/pod369/BGR-to-YUV-Color-Space-Conversion-and-Channel-Splitting) |
| 10 | [Extracting-Specific-Color-Objects-Using-HSV-Color-Space](./10_Extracting-Specific-Color-Objects-Using-HSV-Color-Space) | Python | 2026-03-24 | [Source](https://github.com/pod369/Extracting-Specific-Color-Objects-Using-HSV-Color-Space) |
| 11 | [uav-military-object-detection](./11_uav-military-object-detection) | Python | 2026-06-14 | [Source](https://github.com/pod369/uav-military-object-detection) |
| 12 | [Panorama-image-using-many-images](./12_Panorama-image-using-many-images) | Python | 2026-07-28 | [Source](https://github.com/pod369/Panorama-image-using-many-images) |
| 13 | [Tracking-keypointsbetween-frames-Lucas-Kanadealgorithm](./13_Tracking-keypointsbetween-frames-Lucas-Kanadealgorithm) | Python | 2026-07-28 | [Source](https://github.com/pod369/Tracking-keypointsbetween-frames-Lucas-Kanadealgorithm) |
| 14 | [Face-detection-using-Haarand-LBP-features](./14_Face-detection-using-Haarand-LBP-features) | Python | 2026-07-28 | [Source](https://github.com/pod369/Face-detection-using-Haarand-LBP-features) |
| 15 | [SIFT-Matching-and-Homography](./15_SIFT-Matching-and-Homography) | Python | 2026-10-19 | [Source](https://github.com/pod369/SIFT-Matching-and-Homography) |
| 16 | [MNIST-Handwritten-Digit-Recognition](./16_MNIST-Handwritten-Digit-Recognition) | Python | 2026-10-19 | [Source](https://github.com/pod369/MNIST-Handwritten-Digit-Recognition) |
| 17 | [Superpixel-and-Normalized-Cut](./17_Superpixel-and-Normalized-Cut) | Python | 2026-10-19 | [Source](https://github.com/pod369/Superpixel-and-Normalized-Cut) |
| 18 | [YOLO-Hangul-Text-Detection](./18_YOLO-Hangul-Text-Detection) | Jupyter | 2026-10-19 | [Source](https://github.com/pod369/YOLO-Hangul-Text-Detection) |
| 19 | [Edge-and-Contour-Detection](./19_Edge-and-Contour-Detection) | Python | 2026-10-19 | [Source](https://github.com/pod369/Edge-and-Contour-Detection) |
| 20 | [Image-and-Video-Effects](./20_Image-and-Video-Effects) | Python | 2026-10-19 | [Source](https://github.com/pod369/Image-and-Video-Effects) |

## Scope and limitations

- 본 통합 저장소에는 **20개 항목의 소스 코드 또는 노트북이 수록**되어 있습니다. 기존 개별 저장소는 원본 자료와 추가 기록을 보유합니다.
- 이미지, 영상, 실행 결과, 훈련 모델 가중치와 대용량 데이터셋은 모두 복제하지 않았습니다. 필요하면 각 항목의 **Original repository** 링크에서 가져오세요.
- 특히 11번 UAV 프로젝트의 대용량 데이터셋·모델 체크포인트는 통합 저장소에 포함하지 않고, 학습·추론·평가용 Python 코드와 데이터 설정을 수록했습니다.
- 일부 코드가 참조하는 상대경로의 입력 이미지, 동영상, 데이터셋이 통합 폴더에 없으므로, 해당 입력을 내려받아 경로를 맞춘 뒤 실행해야 합니다.
- 원본 코드 복사 자체와 별개로, 통합된 전체 20개 실습의 동작을 새 환경에서 모두 재검증한 것은 아닙니다.
- 첨부 제출원의 **작성일**을 표에 보존했습니다. 이 날짜는 통합 저장소의 커밋 생성일과 다릅니다.

## Execution

1. 해당 번호의 프로젝트 폴더를 엽니다.
2. 원본 README 및 `requirements.txt`가 있다면 환경 준비에 사용합니다.
3. 누락된 입력 파일은 원본 저장소에서 받아 경로를 조정합니다.
4. `.py`는 Python에서, `.ipynb`는 Jupyter에서 실행합니다.

## Repository naming

이 README의 프로젝트 표제는 `AI-EX-Portfolio`입니다. GitHub 저장소 자체의 이름은 별도 설정 변경이 필요합니다.
