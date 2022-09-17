# author: xwwwb
# date: 2022-07-10
# description: 从相机读取画面
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "index_camera", help="index of the camera to read from", type=int)
args = parser.parse_args()

capture = cv2.VideoCapture(args.index_camera)

frame_width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = capture.get(cv2.CAP_PROP_FPS)

print("CV_CAP_PROP_FRAME_WIDTH:{}".format(frame_width))
print("CV_CAP_PROP_FRAME_HEIGHT:{}".format(frame_height))
print("CAP_PROP_FPS:{}".format(fps))

if capture.isOpened() is False:
    print("Error opening the camera")

frame_index = 0
while capture.isOpened():
    ret, frame = capture.read()

    if ret == True:
        cv2.imshow("Input frame from the camera", frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale input camera", gray_frame)
        if cv2.waitKey(1) & 0xFF == ord('c'):
            frame_name = "./part2/camera_frame_{}.png".format(frame_index)
            gray_frame_name = "./part2/grayscale_camera_frame_{}.png".format(
                frame_index)
            cv2.imwrite(frame_name, frame)
            cv2.imwrite(gray_frame_name, gray_frame)
            frame_index += 1
        # 这里的waitkey 可以实现简单的帧数控制
        # 写成1000 就是 每次等待一秒 间接控制帧数为1帧 至少现在是这样理解的😂
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
capture.release()
cv2.destroyAllWindows()
