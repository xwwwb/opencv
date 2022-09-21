# author: xwwwb
# date: 2022-09-21
# description: 深拷贝
import numpy as np
import cv2

img = cv2.imread('./resource/demo.jpg')

# 默认浅拷贝
img2 = img
# copy深拷贝
img3 = img.copy()

img[10:100, 10:100] = [0, 0, 255]

cv2.imshow('img', img)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey(0)

cv2.destroyAllWindows()
