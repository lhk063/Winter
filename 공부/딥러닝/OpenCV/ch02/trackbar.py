import numpy as np
import cv2


def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow('image', img)

'''
def on_level_change(pos):
    global img

    level = pos * 16
    level = np.clip(level, 0, 255) # 0보다 작으면 무조건 0 255보다 크면 무조건 255 라는 numpy clip 함수

    img[:, :] = level
    cv2.imshow('image', img)
'''


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('Brightness', 'image', 0, 16, on_level_change) # 이 함수는 반드시 창이 생성된 후에 사용하여야 한다 namedWindow or imshow

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
