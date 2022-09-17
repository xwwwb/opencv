# author: xwwwb
# date: 2022-07-10
# description: FPS相关学习

# 关于本代码 存在问题 这里显示的帧数 应该不是真实相机能捕获的帧数吧？
import cv2
import time

# 这里直接指定相机为0 本人使用MacBook Air
capture = cv2.VideoCapture(0)

if capture.isOpened() is False:
    print("Error opening the camera")

while capture.isOpened():
    ret, frame = capture.read()
    if ret is True:
        processing_start = time.time()
        cv2.imshow("Input frame from the camera", frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale input camera", gray_frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
        processing_end = time.time()
        processing_time_frame = processing_end - processing_start
        print("FPS:{}".format(1.0/processing_time_frame))
    else:
        break
capture.release()
cv2.destroyAllWindows()
