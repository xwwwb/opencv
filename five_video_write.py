# author: xwwwb
# date: 2022-09-18
# description: 视频文件写入
import cv2


cv2.namedWindow("video", cv2.WINDOW_NORMAL)
cv2.resizeWindow("video", 640, 480)

cap = cv2.VideoCapture(0)

framewidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frameheight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
vw = cv2.VideoWriter('./resource/five_output.mp4', fourcc, 33, (int(framewidth), int(frameheight)))

while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    cv2.imshow('video', frame)
    cv2.resizeWindow("video", 640, 480)

    vw.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
vw.release()
cv2.destroyAllWindows()
