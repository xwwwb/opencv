# author: xwwwb
# date: 2022-09-25
# description: 中值滤波 去胡椒噪音
import cv2

img = cv2.imread('./resource/demo2.jpg')

dst = cv2.medianBlur(img, 5)

cv2.imshow('dst', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
