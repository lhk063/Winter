import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 마스크 생성
# kernel = np.array([[1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9],
#                    [1/9, 1/9, 1/9]], dtype = np.float64)
# kernel = np.ones((3, 3), dtype=np.float64) / 9.
# dst = cv2.filter2D(src, -1, kernel) # -1을 주면 입력영상과 동일한 데이터 타입 생성
dst = cv2.blur(src, (3, 3))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
