import re
# author: xwwwb
# date: 2022-09-23
# description: 图片融合
import cv2
import numpy as np

img1 = cv2.imread('./resource/demo.jpg')
img2 = cv2.imread('./resource/demo2.jpg')

# 融合要保证两个图片信息一致
print(img1.shape)
print(img2.shape)

result = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('result',result)

cv2.waitKey(0)