import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# RGB 색 평면 분할
blue_plane, green_plane, red_plane = cv2.split(src)

#blue_plane = src[:, :, 0]
#green_plane = src[:, :, 1]
#red_plane = src[:, :, 2]


cv2.imshow('src', src)
cv2.imshow('Blue_plane', blue_plane)
cv2.imshow('Green_plane', green_plane)

cv2.imshow('Red_plane', red_plane)
cv2.waitKey()

cv2.destroyAllWindows()
