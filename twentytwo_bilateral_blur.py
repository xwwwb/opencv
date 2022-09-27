# author: xwwwb
# date: 2022-09-25
# description: 双边滤波
import cv2

img = cv2.imread('./resource/demo2.jpg')

# 双边滤波
dst = cv2 = cv2.bilateralFilter(img, 9, 20, 50)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
