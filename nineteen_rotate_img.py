# author: xwwwb
# date: 2022-09-21
# description: 旋转
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')
new = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
new2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
new3 = cv2.rotate(img, cv2.ROTATE_180)


cv2.imshow('img', img)
cv2.imshow('new', new)
cv2.imshow('new2', new2)
cv2.imshow('new3', new3)
cv2.waitKey(0)
cv2.destroyAllWindows()
