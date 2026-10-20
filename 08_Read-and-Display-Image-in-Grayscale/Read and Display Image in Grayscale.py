import cv2

# 1. 이미지를 그레이스케일(흑백)로 읽기
img_gray = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# 이미지가 정상적으로 불러와졌는지 확인
if img_gray is not None:
    # 윈도우 창에 이미지 출력
    cv2.imshow('Lenna - Grayscale', img_gray)
    
    # 키보드 입력이 있을 때까지 대기 (0은 무한 대기)
    cv2.waitKey(0)
    # 열려있는 모든 창 닫기
    cv2.destroyAllWindows()
else:
    print("Lenna.png 파일을 찾을 수 없습니다.")