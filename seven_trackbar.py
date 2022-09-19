# author: xwwwb
# date: 2022-09-18
# description: Trackbar

import cv2
import numpy as np


def callback(x):
    print(x)


# 创建窗口
cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)
# 创建滑动条
cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

img = np.zeros((480, 460, 3), np.uint8)

while True:
    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    img[:] = [b, g, r]
    cv2.imshow('trackbar', img)

    key = cv2.waitKey(10)
    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
