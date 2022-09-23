# author: xwwwb
# date: 2022-09-23
# description: 绘制图形
from math import fabs
import cv2
import numpy as np

# 坐标 (y,x)
img = np.zeros((480, 640, 3), np.uint8)

# 坐标 (x,y)
# 最后一个参数 是画线的方法 4 8 16 其中16是抗锯齿的
cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5, 16)
# 椭圆
cv2.ellipse(img, (300, 300), (100, 80), 0, 0, 360, (0, 0, 255), 2, 16)

# 度是顺时针
cv2.ellipse(img, (400, 400), (100, 80), 0, 60, 300, (0, 0, 255), -1, 16)

# 矩形
cv2.rectangle(img, (20, 20), (80, 140), (0, 0, 255), -1, 8)
# 圆
cv2.circle(img, (200, 200), 10, (255, 10, 10), 1, 16)
# 多边形 类型要用int32
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
# 填充不能写-1
cv2.polylines(img, [pts], True, (30, 30, 245), 1, 16)
# 用fillPoly填充
cv2.fillPoly(img, [pts], (255, 0, 0))
# 绘制文本
cv2.putText(img,"Hello World!",(10,400),4,4,(50,50,255))


cv2.imshow('draw', img)

cv2.waitKey(0)
