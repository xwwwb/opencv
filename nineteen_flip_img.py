# author: xwwwb
# date: 2022-09-21
# description: 翻转
import cv2

img = cv2.imread('./resource/demo.jpg')
new_img = cv2.flip(img, 0)

cv2.imshow('img',new_img)
cv2.waitKey(0)