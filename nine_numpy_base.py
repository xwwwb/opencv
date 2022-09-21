# author: xwwwb
# date: 2022-09-21
# description: numpy的基础
import numpy as np
import cv2


def np_base():
    a = np.array([2, 3, 4])
    print(a)
    c = np.array([[1.1, 2.0], [3.0, 4.0]])
    print(c)

    # 行的个数，列的个数，通道数
    d = np.zeros((4, 4, 3), np.uint8)
    print(d)

    e = np.ones((8, 8), np.uint8)
    print(e)

    # 定义 full
    f = np.full((8, 8), 255, np.uint8)
    print(f)

    # identity 定义单位矩阵
    g = np.identity(4)
    print(g)

    h = np.eye(5)
    print(h)

    i = np.eye(5, 7)
    print(i)

    i = np.eye(5, 7, k=3)
    print(i)
# np_base()
# Numpy 索引值 [y,x]
img = np.zeros((480, 640, 3), np.uint8)
print(img[100, 100])
# img[100,100] = 255
# 可以看出来是[y,x]
count = 0
while count < 200:
    # img[count, 100, 0] = 255
    img[count,100] = [0,0,255]
    count += 1


cv2.imshow('img', img)

key = cv2.waitKey(0)

if key & 0xff == ord('q'):
    cv2.destroyAllWindows()
