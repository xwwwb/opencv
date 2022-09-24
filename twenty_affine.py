# author: xwwwb
# date: 2022-09-24
# description: 仿射变换
import cv2
import numpy as np

img = cv2.imread('./resource/demo.jpg')

# 平移变换 手写平移矩阵
M = np.float32([[1, 0, 300], [0, 1, 100]])
new = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))

# 使用cv2.getRotationMatrix2D()函数生存旋转矩阵
M_ = cv2.getRotationMatrix2D((500, 500), 15, 0.6)
new_ = cv2.warpAffine(img, M_, (img.shape[1], img.shape[0]))

# 仿射变换
# 使用getAffineTransorm()函数生成仿射矩阵
# 选取三个点，分别为原图中的三个点，和目标图中的三个点

# 原图中的三个点
pts1 = np.float32([[100, 100], [200, 100], [100, 200]])
# 目标图中的三个点
# pts2 = np.float32([[200, 100], [300, 100], [200, 200]]) # 这是平移
pts2 = np.float32([[100, 80], [180, 100], [100, 220]])


# 生成仿射矩阵
M__ = cv2.getAffineTransform(pts1, pts2)
print(M__)
new__ = cv2.warpAffine(img, M__, (img.shape[1], img.shape[0]))

cv2.imshow('new__', new__)

cv2.imshow('new_', new_)
cv2.imshow('img', img)
cv2.imshow('new', new)
cv2.waitKey(0)
cv2.destroyAllWindows()
