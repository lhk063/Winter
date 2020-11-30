import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp', cv2.IMREAD_GRAYSCALE)

# kenel size (0, 0) 을 권장 / 임의의 커널 사이즈 설정시 잘리는 부분이 발생하므로 가우시안 블러를 사용하는 취지에 어긋난다
# sigma x = 3 sigma y = 따로 설정 하지 않아도 괜찮다
dst = cv2.GaussianBlur(src, (0, 0), 3) 

dst2 = cv2.blur(src, (7, 7)) # mean filter 와 비교

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
