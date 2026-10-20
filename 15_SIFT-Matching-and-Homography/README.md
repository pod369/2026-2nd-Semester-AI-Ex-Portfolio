# SIFT Matching and Homography

**포트폴리오 제목: SIFT 특징점 매칭 및 객체 위치 추정**

이미지에서 SIFT 특징점과 기술자를 추출하고, 두 프레임의 특징점 대응으로 템플릿의 위치를 추정하는 영상처리 실습입니다. `mot_color70.jpg`의 원본 지정 영역을 잘라 `mot_color83.jpg`에서 찾습니다.

## 처리 과정

1. 원본 이미지에서 `(x1, y1, x2, y2) = (440, 190, 560, 350)` 영역을 추출합니다. 원본 코드의 `[190:350, 440:560]`과 같습니다.
2. 템플릿과 대상 이미지에서 SIFT 특징점과 기술자를 추출합니다.
3. FLANN의 KNN 검색으로 후보 2개를 찾고 Lowe 비율 검사 `d1 < 0.7 × d2`로 대응점을 선택합니다.
4. 대응점이 4개 이상이면 RANSAC으로 호모그래피를 계산합니다. 기본 재투영 오차 임계값은 5픽셀입니다.
5. 추정한 변환으로 템플릿의 네 모서리를 대상 이미지에 투영합니다.

## 실행

Python 3.10 이상을 권장합니다. 아래 명령은 **저장소 루트**에서 실행합니다.

```bash
python -m pip install -r requirements.txt
python sift_matching_and_homography.py
```

기본 입력 경로는 스크립트 위치를 기준으로 계산하므로 다른 작업 폴더에서 실행해도 같습니다. 기본 출력 폴더는 `outputs/`입니다.

```bash
python sift_matching_and_homography.py --ratio 0.75 --output-dir results/sift
python sift_matching_and_homography.py --source assets/mot_color70.jpg --target assets/mot_color83.jpg --crop 440 190 560 350 --show
```

`--show`는 선택 사항입니다. 기본 실행은 창을 띄우지 않습니다. GUI 표시에는 화면 환경과 GUI를 지원하는 OpenCV가 필요합니다. 사용자 지정 상대 경로는 명령을 실행한 작업 폴더를 기준으로 해석합니다.

## 생성 자료

| 파일 | 내용 |
|---|---|
| `template.png` | 지정 영역에서 추출한 템플릿 |
| `template_keypoints.png`, `target_keypoints.png` | SIFT 특징점의 위치·크기·방향 |
| `good_matches.png` | 비율 검사를 통과한 모든 대응점 |
| `inlier_matches_and_location.png` | RANSAC 인라이어 대응점과 추정 위치 |
| `localized_target.png` | 대상 이미지에 투영한 템플릿 사각형 |
| `metrics.json` | 특징점 수, 대응점 수, 인라이어 수, 처리 시간, 변환 행렬, 처리 상태 |

실행 결과의 `status`를 확인해야 합니다. `homography_estimated`는 변환을 계산했다는 의미이며, 탐지 정확도나 객체 식별 성공률을 측정한 값은 아닙니다. 특징점이 부족하면 `insufficient_features`, 대응점이 4개 미만이면 `insufficient_matches`, 유효한 변환을 얻지 못하면 `homography_failed`를 기록합니다. 이때도 확인 가능한 특징점·매칭 이미지와 JSON을 저장합니다.

## 실제 실행 예시

기본 입력과 파라미터로 실행하여 대응점 35개 중 인라이어 33개를 얻고 호모그래피를 추정했습니다. 상세 측정값은 [`results/metrics.json`](results/metrics.json)에 있습니다. 이 수치는 한 이미지 쌍에서 얻은 결과입니다.

![SIFT 대응점과 추정 위치](results/inlier_matches_and_location.png)

![대상 이미지에 투영한 템플릿 영역](results/localized_target.png)

## 원본과 보완 내용

원본 저장소: [pod369/Image-processing-4](https://github.com/pod369/Image-processing-4)

| 원본 | 기능 | 보관 위치 |
|---|---|---|
| `play_5_2.py` | SIFT 특징점 표시 | `reference/play_5_2.py` |
| `play_5_3.py` | SIFT + FLANN 대응점 검색 | `reference/play_5_3.py` |
| `play_5_4.py` | RANSAC 호모그래피와 위치 표시 | `reference/play_5_4.py` |

세 실습을 하나의 실행 프로그램으로 통합했습니다. 영문 파일명, CLI 설정, 자동 결과 저장, 작업 폴더와 독립적인 기본 경로, 입력 및 특징점 부족 검사, 측정값 JSON 기록을 추가했습니다. `reference/`에는 원본을 보존했습니다.

## 한계 및 추가 실험

호모그래피는 평면 또는 근사 평면 대응을 가정합니다. 3차원 대상의 큰 시점 변화, 가림, 흐림, 반복 무늬에서는 잘못된 변환이 나올 수 있습니다. 비율 검사 임계값을 바꾸며 대응점 수·인라이어 비율·시각적 정합을 비교하는 실험을 추가할 수 있습니다. 결과 수치는 실행 환경과 이미지에 따라 달라지며, 이 문서에는 미측정 정확도를 제시하지 않습니다.

## AI-Ex 포트폴리오

2026년 2학기 AI-Ex 포트폴리오의 개별 프로젝트입니다. 원본 파일은 `reference/`에 보존했으며, 정리한 실행 코드와 원본을 구분했습니다. 원본 기준 커밋은 `b2f9a5b94bbe353cce22ce469e358bb2715759ce`입니다. 원본 재배포 라이선스는 별도로 추가하지 않았습니다.

실행 예시와 결과 설명은 이 저장소의 루트 구조에 맞췄습니다. `results/`에 포함된 측정 기록은 2026-10-14 실행 당시의 자료로, 과거 통합 폴더 경로가 메타데이터에 남아 있을 수 있습니다.

| 관련 프로젝트 |
|---|
| [Superpixel and Normalized Cut](https://github.com/pod369/Superpixel-and-Normalized-Cut) |
| [Edge and Contour Detection](https://github.com/pod369/Edge-and-Contour-Detection) |
| [Image and Video Effects](https://github.com/pod369/Image-and-Video-Effects) |
| [MNIST Handwritten Digit Recognition](https://github.com/pod369/MNIST-Handwritten-Digit-Recognition) |
| [YOLO Hangul Text Detection](https://github.com/pod369/YOLO-Hangul-Text-Detection) |

개별 저장소 검증일: **2026-10-19**. `/tmp` 작업 폴더에서 기본 입력으로 실행해 결과 저장을 확인했습니다. 원본 코드와 입력 이미지의 SHA-256도 보존 여부를 확인했습니다. 기존 `results/`는 2026-10-14 실행 기록을 유지합니다.
