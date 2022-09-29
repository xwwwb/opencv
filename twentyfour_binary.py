# author: xwwwb
# date: 2022-09-27
# description: 二值化

import cv2

img = cv2.imread('./resource/demo2.jpg')
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

result, dst = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY)
result_2, dst_2 = cv2.threshold(img1, 180, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('img', img)
cv2.imshow('img1', img1)
cv2.imshow('dst_2', dst_2)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
