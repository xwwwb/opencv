# author: xwwwb
# date: 2022-09-23
# description: 添加水印
import cv2
import numpy as np

img = cv2.imread('./resource/demo2.jpg')

logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

logo[20:120, 20:120] = [0, 0, 255]
logo[80:180, 80:180] = [0, 255, 0]

mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

# 对mask按位求反
m = cv2.bitwise_not(mask)

# 选择图像位置
roi = img[0:200, 0:200]
# 与m进行与操作
tmp = cv2.bitwise_and(roi, roi, mask=m)

dst = cv2.add(tmp, logo)

img[0:200, 0:200] = dst

cv2.imshow('dst', dst)
cv2.imshow('tmp', tmp)

cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.imshow('result', img)

cv2.waitKey(0)
