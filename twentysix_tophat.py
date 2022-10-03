# author: xwwwb
# date: 2022-10-3
# description: 高帽运算 原图-开运算
import cv2

img = cv2.imread('./resource/demo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 200, cv2.THRESH_BINARY_INV)

# kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))

dst = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
