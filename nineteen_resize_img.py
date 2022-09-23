# author: xwwwb
# date: 2022-09-24
# description: 图片缩放
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')

# 这里的size是一个元组，第一个元素是宽，第二个元素是高 但是这里制定了fx fy
img_resize = cv2.resize(img, (0, 0), fx=5, fy=5, interpolation=cv2.INTER_AREA)
print(img_resize.shape)
cv2.imshow('img', img)
cv2.imshow('img_resize', img_resize)
cv2.imwrite('./resource/nineteen_resize.jpg', img_resize)
cv2.waitKey(0)
