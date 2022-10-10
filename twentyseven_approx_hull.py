# author: xwwwb
# date: 2022-10-3
# description: 凸包和逼近
import cv2


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


img = cv2.imread('./resource/hand.png')
# 单通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
ret, binary = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)

# 轮廓查找
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
img_contours = cv2.drawContours(img, contours, -1, (0, 244, 0), 2)

e = 30
# approx 近似的 Polygon 多边形 DP好像是算法名字
approx = cv2.approxPolyDP(contours[0], e, True)
# convex 凸面的 Hull 外壳
hull = cv2.convexHull(contours[0])
print(approx)
print(approx.shape)
drawShape(img_contours, approx)
drawShape(img_contours, hull)
cv2.imshow('binary', binary)
cv2.imshow('img_contours', img_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
