# author: xwwwb
# date: 2022-09-27
# description: scharr算子 沙尔算子

# 与Sobel类似 只不过使用kernel值不同 只能单独求x和y
import cv2

img = cv2.imread('./resource/demo2.jpg')
d1 = cv2.Scharr(img, cv2.CV_64F, 1, 0)
d2 = cv2.Scharr(img, cv2.CV_64F, 0, 1)
dst = cv2.add(d1, d2)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
