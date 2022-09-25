# author: xwwwb
# date: 2022-09-25
# description: 透视变换
import cv2
import numpy as np

point = []
cv2.namedWindow('img', cv2.WINDOW_NORMAL)

img = cv2.imread('./resource/demo3.jpg')
img_ = img.copy()
showNew = False
dst = np.float32([
    [0, 0],
    [img.shape[1], 0],
    [img.shape[1], img.shape[0]],
    [0, img.shape[0]]

])


def mouse_callback(event, x, y, flags, data):
    if event == cv2.EVENT_LBUTTONUP:
        point.append((x, y))
        if 1 < len(point) < 5:
            cv2.line(img, (point[len(point) - 2][0],
                           point[len(point) - 2][1]), (x, y), (0, 0, 255), 10, 16)
    global new, showNew
    if len(point) == 4 and not showNew :
        cv2.line(img, (point[0][0], point[0][1]), (x, y), (0, 0, 255), 10, 16)

        # 选定了四个点
        src = np.float32([
            [point[0][0], point[0][1]],
            [point[1][0], point[1][1]],
            [point[2][0], point[2][1]],
            [point[3][0], point[3][1]],
        ])

        M = cv2.getPerspectiveTransform(src, dst)
        new = cv2.warpPerspective(img_, M, (1080, 1439))
        showNew = True


cv2.setMouseCallback('img', mouse_callback)

while True:
    cv2.imshow('img', img)
    if showNew:
        cv2.imshow('new', new)

    key = cv2.waitKey(2)
    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
