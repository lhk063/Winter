import sys
import numpy as np
import cv2
# 원색적인 색상 찾을때
# RGB 는 밝기가 어두운 사진에서는 색을 찾아내기 힘들기 때문에 HSV를 사용한다

src = cv2.imread('candies.png')
#src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
