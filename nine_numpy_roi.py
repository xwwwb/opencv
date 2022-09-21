# author: xwwwb
# date: 2022-09-21
# description: numpy的切片
import numpy as np
import cv2

img = np.zeros((480, 640, 3), np.uint8)
sub = img[100:200,100:200]
sub[:,:]=[0,0,255]
sub[10:200,10:200] = [0,255,0]

cv2.imshow('img',sub)
key = cv2.waitKey(0)
if key & 0xff == ord('q'):
    cv2.destroyAllWindows()