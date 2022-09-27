# author: xwwwb
# date: 2022-09-27
# description: Canny边缘检测
import cv2

img = cv2.imread('./resource/demo2.jpg')
dst = cv2.Canny(img, 100, 200)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
