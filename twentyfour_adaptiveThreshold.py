# author: xwwwb
# date: 2022-09-27
# description: 自适应二值化

import cv2

img = cv2.imread('./resource/demo.jpg')

dst = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,10)

cv2.waitKey(0)
cv2.destroyAllWindows()
