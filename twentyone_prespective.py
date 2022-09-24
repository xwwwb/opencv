# author: xwwwb
# date: 2022-09-25
# description: 透视变换 更换demo照片吧
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')

src = np.float32([[1000, 120], [2100, 1100], [0, 4000], [2500, 3900]])
dst = np.float32([[0, 0], [img.shape[1], 0], [0, img.shape[0]], [img.shape[1], img.shape[0]]])
M = cv2.getPerspectiveTransform(src, dst)


new = cv2.warpPerspective(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('new', new)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
