# author: xwwwb
# date: 2022-09-23
# description: 鼠标控制绘图 自己完成
import cv2
import numpy as np

# state为1就是画直线
state = 0
point = []


def mouseCallback(event, x, y, flags, userdata):
    if state == 1:
        if event == cv2.EVENT_LBUTTONUP:
            # 当前是第一次点击 将坐标推入point数组
            point.append((x, y))
        if (event == cv2.EVENT_MOUSEMOVE) and (len(point) == 1):
            # 移动鼠标的时候 绘制
            img[:] = (251, 128, 47)
            cv2.line(img, point[0], (x, y), (255, 255, 255), 2, 16)
    if state == 2:
        if event == cv2.EVENT_LBUTTONUP:
            # 当前是第一次点击 将坐标推入point数组
            point.append((x, y))
        if (event == cv2.EVENT_MOUSEMOVE) and (len(point) == 1):
            img[:] = (251, 128, 47)
            cv2.rectangle(img, point[0], (x, y), (255, 255, 255), 2, 16)
    if state == 3:
        if event == cv2.EVENT_LBUTTONUP:
            point.append((x, y))
        if(event == cv2.EVENT_MOUSEMOVE) and (len(point) == 1):
            img[:] = (251, 128, 47)
            center_x = (x+point[0][0])/2
            center_y = (y+point[0][1])/2
            center = (int(center_x), int(center_y))
            r = int(abs(x-point[0][0])/2)
            cv2.circle(img, center, r, (255, 255, 255), 2, 16)
            cv2.rectangle(img, point[0], (x, y), (0, 0, 255), 2, 16)


img = np.full((400, 400, 3), (251, 128, 47), np.uint8)

cv2.putText(img, "Line:L,Rectangle:R,Circle:C", (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 150))

cv2.imshow('img', img)
# 写入标题


# 等待键盘输入
key = cv2.waitKey(0)

if key & 0xff == ord('l'):
    # 当前是画直线的模式
    state = 1
elif key & 0xff == ord('r'):
    state = 2
elif key & 0xff == ord('c'):
    state = 3

# 等待鼠标点击
cv2.setMouseCallback('img', mouseCallback)

while True:
    cv2.imshow('img', img)
    key_ = cv2.waitKey(2)
    if key_ & 0xff == ord('q'):
        break

cv2.destroyAllWindows()
