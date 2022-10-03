# author: xwwwb
# date: 2022-10-3
# description: 开运算
# 看荧的嘴巴 去除毛刺
import cv2

img = cv2.imread('./resource/demo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 200, cv2.THRESH_BINARY_INV)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

dst = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
