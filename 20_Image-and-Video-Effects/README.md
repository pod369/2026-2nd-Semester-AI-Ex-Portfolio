# Image and Video Effects

사진 및 카메라·동영상에 OpenCV 효과를 적용하는 포트폴리오입니다. 동일한 효과 함수를 사진과 영상 처리에서 공유하고, 결과 파일을 저장할 수 있도록 정리했습니다.

## 구현 기능

| 영문 기능명 | 결과 | 처리 방법 |
|---|---|---|
| `emboss` | 명암 엠보싱 | 회색조 변환 → 방향성 커널 필터링 → 128 오프셋 및 범위 제한 |
| `cartoon` | 컬러 카툰 | OpenCV `stylization` |
| `pencil-gray` | 명암 연필 스케치 | OpenCV `pencilSketch`의 회색조 결과 |
| `pencil-color` | 컬러 연필 스케치 | OpenCV `pencilSketch`의 컬러 결과 |
| `oil` | 유화 | OpenCV contrib `xphoto.oilPainting` |

## 원본과 정리한 코드

원본: [pod369/Image-processing-4](https://github.com/pod369/Image-processing-4)

| 원본 파일 | 정리한 파일 | 역할 |
|---|---|---|
| `reference/play_6_6.py` | `photo_effects.py` | 사진 입력 및 5종 효과 이미지 저장 |
| `reference/play_6_7.py` | `video_effects.py` | 카메라·동영상 프레임 처리 및 동영상 저장 |
| 두 원본에 중복된 효과 코드 | `effects.py` | `apply_effect(image, effect)` 공통 함수 |

`reference/`에는 원본을 수정하지 않고 보존했습니다. 원본의 PyQt5 콜백 내부 영상 반복문은 GUI 이벤트 처리를 막을 수 있어, 실행 옵션으로 동작을 지정하는 CLI로 정리했습니다. PyQt5는 정리한 코드에서 사용하지 않습니다. 사진은 기본적으로 창을 열지 않으며, 영상은 `--no-display`로 창 없이 실행할 수 있습니다. 원본의 Windows 전용 `CAP_DSHOW` 지정도 제거했습니다.

추가한 사항은 입력 파일·카메라 오류 안내, 저장 성공 확인, 영상 프레임 수 제한, 입력 영상 덮어쓰기 방지, 카메라와 영상 저장기의 `finally` 해제입니다. 효과 파라미터는 원본 설정을 유지했습니다.

## 설치

아래 명령은 **저장소 최상위 폴더**에서 실행합니다. Python 3.10 이상을 권장합니다.

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
# macOS / Linux
# source .venv/bin/activate
python -m pip install -r requirements.txt
```

`oil`은 `opencv-contrib-python`의 `xphoto` 모듈이 필요합니다. `opencv-python`과 `opencv-contrib-python`은 같은 `cv2` 이름을 사용하므로 새 가상환경에서 이 폴더의 requirements만 설치하는 것을 권장합니다. `--show`와 영상 미리보기는 그래픽 화면이 있는 환경에서 실행합니다.

## 사진 실행

기본 예제는 저장소의 `assets/river.jpg`입니다. 결과는 `outputs/photo/`에 PNG 5개로 저장됩니다.

```bash
python photo_effects.py
python photo_effects.py assets/river.jpg --output-dir outputs/image_effects
python photo_effects.py assets/river.jpg --show
```

원하는 사진 경로를 첫 번째 인자로 전달할 수 있습니다. 파일명에 공백이 있으면 경로를 따옴표로 감쌉니다. 출력 이름은 `<입력파일명>_emboss.png`, `<입력파일명>_cartoon.png`, `<입력파일명>_pencil-gray.png`, `<입력파일명>_pencil-color.png`, `<입력파일명>_oil.png`입니다. 같은 출력 경로로 다시 실행하면 결과 파일을 덮어씁니다.

## 카메라 및 영상 실행

```bash
# 첫 번째 카메라: 창에서 q를 눌러 종료
python video_effects.py --source 0 --effect cartoon

# 동영상 파일을 처리해 저장
python video_effects.py --source input.mp4 --effect pencil-gray --output outputs/pencil_video.mp4

# 화면 없이 10개 프레임만 처리하는 스모크 테스트
python video_effects.py --source input.mp4 --effect emboss --no-display --max-frames 10 --output outputs/emboss_smoke.avi

# 화면 없이 카메라를 실행할 때는 종료 기준을 반드시 지정
python video_effects.py --source 0 --effect oil --no-display --max-frames 30
```

`--source`에 숫자를 넣으면 카메라 인덱스, 그 외에는 로컬 동영상 경로로 해석합니다. `--effect`는 기능 표의 이름 중 하나를 선택합니다. `--output`을 생략하면 결과 동영상은 저장하지 않습니다. MP4는 `mp4v`, AVI는 `MJPG` 코덱을 사용하며 실제 지원 여부는 설치된 OpenCV와 운영체제에 따라 달라집니다.

저장 FPS는 입력 영상·카메라의 FPS 정보를 사용하고, 정보가 유효하지 않으면 30으로 설정합니다. 필요하면 `--output-fps 24`처럼 직접 지정할 수 있습니다. 이 값은 **출력 재생 속도 정보**이며 실시간 처리 성능의 측정값이 아닙니다. 명암 효과도 동영상 저장 시에는 3채널로 변환합니다.

## 결과 정리 및 제한

2026-10-14에 예제 사진의 5종 효과 저장을 확인했습니다. 사진으로 만든 합성 AVI 입력에 대해서도 엠보싱 8프레임 출력 파일을 다시 열어 검증했습니다. 결과 이미지는 `results/`, 영상 확인 기록은 `results/video_metrics.json`에 있습니다. 실제 웹캠 장치의 실행을 확인한 것은 아닙니다.

포트폴리오에는 같은 사진의 원본과 5종 효과 결과를 비교해 넣으면 됩니다. 영상은 입력 영상, 효과 종류, 처리한 프레임 수와 결과 영상 링크를 함께 기록할 수 있습니다. 학습 모델을 사용하는 프로젝트가 아니므로 학습 정확도나 mAP를 평가 항목으로 제시하지 않습니다.

- 해상도와 효과 종류에 따라 영상 처리 속도가 달라집니다. 실시간 FPS는 별도로 측정해야 합니다.
- 카메라 권한, 장치 연결, 코덱 및 GUI 사용 가능 여부는 사용자 환경에 의존합니다.
- 파일 입력은 영상의 끝과 중간 디코딩 실패를 완전히 구분하지 못하므로, 실제 사용 시 출력 길이도 확인해야 합니다.
- 원본 `reference/`의 PyQt5 프로그램은 보존용이며, 본 README의 실행 명령은 정리한 CLI를 기준으로 합니다.
- 동영상 실행 명령의 `input.mp4`는 사용자가 준비한 실제 파일 경로로 바꿔야 합니다.

이 README에는 측정하지 않은 처리 속도, 카메라 검증 결과 또는 탐지 정확도를 기재하지 않았습니다.

## AI-Ex 포트폴리오

2026년 2학기 AI-Ex 포트폴리오의 개별 프로젝트입니다. 원본 파일은 `reference/`에 보존했으며, 정리한 실행 코드와 원본을 구분했습니다. 원본 기준 커밋은 `b2f9a5b94bbe353cce22ce469e358bb2715759ce`입니다. 원본 재배포 라이선스는 별도로 추가하지 않았습니다.

실행 예시와 결과 설명은 이 저장소의 루트 구조에 맞췄습니다. `results/`에 포함된 측정 기록은 2026-10-14 실행 당시의 자료로, 과거 통합 폴더 경로가 메타데이터에 남아 있을 수 있습니다.

| 관련 프로젝트 |
|---|
| [SIFT Matching and Homography](https://github.com/pod369/SIFT-Matching-and-Homography) |
| [Superpixel and Normalized Cut](https://github.com/pod369/Superpixel-and-Normalized-Cut) |
| [Edge and Contour Detection](https://github.com/pod369/Edge-and-Contour-Detection) |
| [MNIST Handwritten Digit Recognition](https://github.com/pod369/MNIST-Handwritten-Digit-Recognition) |
| [YOLO Hangul Text Detection](https://github.com/pod369/YOLO-Hangul-Text-Detection) |

개별 저장소 검증일: **2026-10-19**. `/tmp` 작업 폴더에서 기본 입력으로 실행해 결과 저장을 확인했습니다. OpenCV 5.0.0, NumPy 2.3.5, scikit-image 0.26.0 환경을 사용했습니다. 사진 효과 5종과 동영상 파일 입력의 3프레임 처리도 확인했으며, 새 출력은 기존 `results/`와 구분해 검증 폴더에 저장했습니다.
