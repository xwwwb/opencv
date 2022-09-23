# author: xwwwb
# date: 2022-09-23
# description: 图片相加
from cgitb import reset
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')

img_ = np.ones(img.shape, np.uint8) * 80

add_result = cv2.add(img, img_)
subtract_result = cv2.subtract(img, img_)
multiply_result = cv2.multiply(img, img_)
# 除法用cv2.divide()

cv2.imshow('add', add_result)
cv2.imshow('subtract', subtract_result)
cv2.imshow('multiply', multiply_result)
cv2.imshow('origin', img)


cv2.waitKey(0)

cv2.destroyAllWindows()
