import sys
import cv2


print('Hello, OpenCV', cv2.__version__) # 버전 출력

img = cv2.imread('cat.bmp')

if img is None:
    
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.waitKey() # keyboard 입력을 기다린다. 키보드를 누르기 전까지 영상이 켜져있다.

cv2.destroyAllWindows() # 열려있는 모든 창을 닫기.

## python 파일 실행 경로일치 > cd 경로 or cd ../  > python 파일이름.py 끝