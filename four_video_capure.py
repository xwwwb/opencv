# author: xwwwb
# date: 2022-09-18
# description: 视频采集
import cv2

# 创建窗口
cv2.namedWindow("video",cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow("video", 640, 480)

cap = cv2.VideoCapture(0)

while True:
  ret,frame = cap.read()
  cv2.imshow('video',frame)

  key = cv2.waitKey(5)
  if (key & 0xff == ord('q')):
    break

cap.release()
cv2.destroyAllWindows()