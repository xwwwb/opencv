# author: xwwwb
# date: 2022-09-25
# description: 简单滤波
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')

# 手写均值滤波
kernel = np.ones((20, 20), np.float32) / 400
dst = cv2.filter2D(img, -1, kernel)

# 使用opencv自带的均值滤波
dst2 = cv2.blur(img,(20,20))
# 或者使用方盒滤波normalize设置为1
dst3 = cv2.boxFilter(img, -1, (50, 50), normalize=1)

cv2.imshow('boxFilter', dst3)
cv2.imshow('blur', dst2)
cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
