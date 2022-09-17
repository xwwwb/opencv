# author: xwwwb
# date: 2022-07-12
# description: 视频倒放
import cv2
import argparse

# 这里也无法倒放
# read出来ret是False 抽时间检查吧
# parser = argparse.ArgumentParser()
# parser.add_argument("video_path", help="path to the video file")
# args = parser.parse_args()

# capture = cv2.VideoCapture(args.video_path)
capture = cv2.VideoCapture('./part2/demo.avi')
if capture.isOpened() == False:
    print("Error opening video file")

# 拿到视频的总帧数
frame_index = capture.get(cv2.CAP_PROP_FRAME_COUNT) - 2
print("Starting in frame:{}".format(frame_index))

while capture.isOpened() and frame_index >= 0:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = capture.read()

    if ret:
        cv2.imshow("Original frame", frame)
        frame_index = frame_index-1
        print("Next index to read:{}".format(frame_index))

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
