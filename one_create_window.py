# author: xwwwb
# date: 2022-09-18
# description: 创建cv2 的窗口
import cv2

cv2.namedWindow('new', cv2.WINDOW_NORMAL)
cv2.resizeWindow('new',600,600)
cv2.imshow('new', 0)


key = cv2.waitKey(0)
cv2.destroyAllWindows()
