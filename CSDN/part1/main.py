# author: xwwwb
# date: 2022-07-10
# description: 认识cv2的基础函数
import cv2
from matplotlib import pyplot as plt
import numpy as np

# 读取图像
img_OpenCV = cv2.imread('./part1/demo.jpg')
# 将OpenCV的BGR格式转换为RGB格式
b, g, r = cv2.split(img_OpenCV)
# 将RGB格式的图像合并为一个三通道的图像
img_matplotlib = cv2.merge([r, g, b])

# 也可以从BGR转为RGB 速度更快 和img_matplotlib一样
img_matplotlib_2 = img_OpenCV[:, :, ::-1]


# subplot可以省略逗号
# subbplot(nrows, ncols, index)
plt.subplot(121)
plt.imshow(img_OpenCV)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()
# 左边BGR 右边RBG 使用matplotlib显示的图像是BGR格式

# cv2.imshow('BGR', img_OpenCV)
# cv2.imshow('RGB', img_matplotlib)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

img_concats = np.concatenate((img_OpenCV, img_matplotlib_2), axis=1)
cv2.imshow('BGR and RGB', img_concats)
# 5秒内不按任意键 就自动退出
cv2.waitKey(5000)
cv2.destroyAllWindows()

# 获得图像的行列和通道的数量
dimensions = img_OpenCV.shape
print("行列和通道", dimensions)
# 获得图像的大小(img.size=高*宽*通道)
total_number_of_elements = img_OpenCV.size
print("图像大小", total_number_of_elements)
# 获得图像数据类型 因为像素值在0-255之间 所以数据类型为uint8
image_dtype = img_OpenCV.dtype
print("图像数据类型", image_dtype)
# 读取某个像素值
(b, g, r) = img_OpenCV[100, 100]
print("100,100的B G R", b, g, r)
# 读取某个像素的蓝色值
b = img_OpenCV[100, 100]
# 修改像素点
img_OpenCV[100, 100] = [0, 255, 0]
print("100,100的像素", img_OpenCV[100, 100])
# 处理切片 分块
top_left_corner = img_OpenCV[0:100, 0:100]
# top_left_corner 是一个小图像
# 修改颜色
top_left_corner[:] = [0, 0, 255]
cv2.imshow("Change", img_OpenCV)
cv2.waitKey(0)

# 灰度相关
# 传入第二个标志位
gray_img = cv2.imread('./part1/demo.jpg', cv2.IMREAD_GRAYSCALE)
print("灰度图像无通道", gray_img.shape)
# 这里i只能获得一个值 称为像素强度
i = gray_img[1000, 1000]
print("1000,1000的像素强度", i)
# 可修改
gray_img[1000, 1000] = 0
print("1000,1000修改后的像素强度", gray_img[1000, 1000])
# 展示gray_img
cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
