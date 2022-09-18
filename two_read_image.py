# author: xwwwb
# date: 2022-09-18
# description: 读取图片文件
import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('./resource/demo.jpg', cv2.IMREAD_COLOR)
cv2.imshow('img', img)

key = cv2.waitKey(0)

if (key & 0xff) == ord('q'):
    cv2.destroyAllWindows()
