# author: xwwwb
# date: 2022-10-3
# description: 外接矩形
import cv2
import numpy as np

img = cv2.imread('./resource/hello.png')
# 单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, 1, (0, 244, 0), 2)

# 最小外接矩形
rect = cv2.minAreaRect(contours[3])
print(rect)
box = cv2.boxPoints(rect)
box = np.int0(box)
print(box)
print([box])
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 边界矩形
rect_2 = cv2.boundingRect(contours[1])
[x, y, w, h] = rect_2
print(rect_2)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

rect_3 = cv2.boundingRect(contours[3])
[x_, y_, w_, h_] = rect_3
cv2.rectangle(img, (x_, y_), (x_ + w_, y_ + h_), (0, 255, 0), 2)

cv2.imshow('binary', binary)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
