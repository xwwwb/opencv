# author: xwwwb
# date: 2022-09-27
# description: 拉普拉斯算子

import cv2

img = cv2.imread('./resource/demo2.jpg')

dst = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
