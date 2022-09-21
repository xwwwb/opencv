# author: xwwwb
# date: 2022-09-21
# description: 访问图片属性
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')

# 包含三个信息 高 长 通道数
print(img.shape)
# 图像占用多大空间 高 乘 宽 乘 通道数
print(img.size)
# 图像中每个元素的位深
print(img.dtype)
