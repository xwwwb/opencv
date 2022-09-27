# author: xwwwb
# date: 2022-09-27
# description: sobel算子 索贝尔算子

# 先向X方向求导
# 再向Y方向求导
# 最后将X方向和Y方向的结果相加
import cv2

src = cv2.imread('./resource/demo.jpg')

# 1.先向X方向求导
d1 = cv2.Sobel(src, cv2.CV_64F, 1, 0, ksize=3)
# 2.再向Y方向求导
d2 = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize=3)
# 3.最后将X方向和Y方向的结果相加
# dst = cv2.addWeighted(d1, 0.5, d2, 0.5, 0)
# dst = d1 + d2
dst = cv2.add(d1, d2)

cv2.imshow('d1', d1)
cv2.imshow('d2', d2)
cv2.imshow('src', src)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
