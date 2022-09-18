# author: xwwwb
# date: 2022-09-18
# description: 鼠标控制
import cv2
import numpy as np


def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)
    cv2.circle(img,(x,y),10,(0,0,255),2)


cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)

cv2.setMouseCallback('mouse', mouse_callback, "123")

img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1)

    if key & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
