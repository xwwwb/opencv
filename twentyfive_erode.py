# author: xwwwb
# date: 2022-10-1
# description: 腐蚀
import cv2

img = cv2.imread('./resource/demo.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

# kernel = np.ones((3, 3), np.uint8)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
kernel1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
print(kernel)
print(kernel1)
print(kernel2)
# 被侵蚀了
dst = cv2.erode(img, kernel, iterations=1)
dst1 = cv2.erode(img, kernel1, iterations=1)
dst2 = cv2.erode(img, kernel2, iterations=1)

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
