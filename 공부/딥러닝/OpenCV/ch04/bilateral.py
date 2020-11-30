import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()
# 음수(-1)을 입력하면 sigmaSpace 값에 의해 자동 결정됨
dst = cv2.bilateralFilter(src, -1, 10, 5)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
