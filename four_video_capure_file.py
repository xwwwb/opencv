# author: xwwwb
# date: 2022-09-18
# description: 文件读取视频
import cv2

# 创建窗口
cv2.namedWindow("video", cv2.WINDOW_AUTOSIZE)
cv2.resizeWindow("video", 640, 480)

# 可以从设备 可以从文件
cap = cv2.VideoCapture('./resource/demo.mp4')

while True:
    ret, frame = cap.read()
    cv2.imshow('video', frame)

    key = cv2.waitKey(10)
    if (key & 0xff == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()
