# author: xwwwb
# date: 2022-09-23
# description: 位运算 非运算
import cv2
import numpy as np

img = np.zeros((200, 200), np.uint8)

img[50:150, 50:150] = 255

new_img = cv2.bitwise_not(img)

cv2.imshow('new_img', new_img)
cv2.imshow('img', img)

img2 = cv2.imread('./resource/demo.jpg')
new_img2 = cv2.bitwise_not(img2)

cv2.imshow('new_img2', new_img2)
cv2.imshow('img2', img2)

cv2.waitKey(0)
