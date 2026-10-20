import cv2

# 원본 이미지 읽기 (기본값인 BGR 컬러로 읽힘)
img_bgr = cv2.imread('Lenna.png')

if img_bgr is not None:
    # BGR 색 공간을 YUV 색 공간으로 변환
    img_yuv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YUV)
    
    # Y, U, V 성분으로 분리
    y, u, v = cv2.split(img_yuv)
    
    # 각각의 성분 출력
    cv2.imshow('Original (BGR)', img_bgr)
    cv2.imshow('Y Channel (Luminance)', y) # 밝기 성분 (흑백처럼 보임)
    cv2.imshow('U Channel (Chrominance)', u) # 색차 성분
    cv2.imshow('V Channel (Chrominance)', v) # 색차 성분
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Lenna.png 파일을 찾을 수 없습니다.")