# author: xwwwb
# date: 2022-10-3
# description: 轮廓绘制
import cv2

img = cv2.imread('./resource/contours1.png')
# 单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
print(hierarchy)
img_contours = cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

cv2.imshow('binary', binary)
cv2.imshow('img_contours', img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
