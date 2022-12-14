# author: xwwwb
# date: 2022-09-25
# description: 高斯滤波
import cv2

img = cv2.imread('./resource/demo2.jpg')

dst = cv2.GaussianBlur(img, (9, 9), sigmaX=10, sigmaY=100)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
