import cv2
import numpy as np

# 이미지 읽기
img_candies = cv2.imread('Candies.png')

if img_candies is not None:
    # BGR을 HSV 색 공간으로 변환
    hsv = cv2.cvtColor(img_candies, cv2.COLOR_BGR2HSV)
    
    # 파란색 영역 정의 (H: 100~140, S와 V는 50~255 범위로 설정해 너무 어둡거나 하얀색 제외)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])
    
    # inRange 함수를 사용하여 파란색 영역만 흰색(255), 나머지는 검은색(0)인 마스크 생성
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # 원본 이미지와 마스크를 AND 연산하여 파란색 캔디만 추출
    blue_candies = cv2.bitwise_and(img_candies, img_candies, mask=mask)
    
    # 결과 출력
    cv2.imshow('Original Candies', img_candies)
    cv2.imshow('Blue Mask', mask)
    cv2.imshow('Extracted Blue Candies', blue_candies)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Candies.png 파일을 찾을 수 없습니다.")