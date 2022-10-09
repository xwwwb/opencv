# author: xwwwb
# date: 2022-10-3
# description: 外接矩阵
import cv2
import numpy as np


def drawShape(src, points):
    i = 0
    while i < len(points):
        if i == len(points) - 1:
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 2)
        else:
            x, y = points[i][0]
            x1, y1 = points[i + 1][0]
            cv2.line(src, (x, y), (x1, y1), (0, 0, 255), 2)
        i += 1


img = cv2.imread('./resource/hello.png')
# 单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, 1, (0, 244, 0), 2)

# 最小外接矩阵
rect = cv2.minAreaRect(contours[1])
print(rect)
box = cv2.boxPoints(rect)
box = np.int0(box)
print(box)
print([box])
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)

# 边界矩阵


cv2.imshow('binary', binary)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
