# author: xwwwb
# date: 2022-07-10
# description: 视频文件读取
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_path", help="path to the video file")
args = parser.parse_args()
# VideoCapture可以读取视频文件
# 也可以读取网络摄像头 具体操作还没有查呢
capture = cv2.VideoCapture(args.video_path)
if capture.isOpened() == False:
    print("Error opening the video file!")
while capture.isOpened():
    ret, frame = capture.read()
    if ret == True:
        cv2.imshow("Original frame from the video file", frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('Grayscale frame', gray_frame)
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()
