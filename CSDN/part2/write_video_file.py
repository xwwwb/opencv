# author: xwwwb
# date: 2022-07-11
# description: 创建并保存视频文件
# 本案例保存的视频文件无法打开是为什么？？ 抽空排错
import cv2
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("output_video_path",
                    help="path to the video file to write")
args = parser.parse_args()

capture = cv2.VideoCapture(0)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

out_gray = cv2.VideoWriter(args.output_video_path, fourcc, int(
    fps), (int(frame_width), int(frame_width)), False)

while capture.isOpened():
    ret, frame = capture.read()
    if ret:
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        out_gray.write(gray_frame)

        cv2.imshow('gray', gray_frame)

        if cv2.waitKey(1) & 0Xff == ord('q'):
            break
    else:
        break
capture.release()
out_gray.release()
cv2.destroyAllWindows()
