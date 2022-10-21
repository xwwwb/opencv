# author: xwwwb
# date: 2022-10-21
# description: demo.flv的车辆检测 只有左边

import cv2

minW = 120
minH = 150

# 检测线高度
line_height = 820
# 线的偏移量
offset = 11

line_height_ = 700
# 线的偏移量
offset_ = 3

# 左边占比
left = 3 / 5


def center(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy


cap = cv2.VideoCapture("demo.flv")

bg_sub_mog = cv2.bgsegm.createBackgroundSubtractorMOG(history=300)
# 腐蚀膨胀使用
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
# 开闭运算使用
kernel_ = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
cars = []
car_num = 0
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        # 灰度
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 去噪
        blur = cv2.GaussianBlur(gray, (3, 3), 5)
        # 去背景
        mask = bg_sub_mog.apply(blur)
        # 腐蚀
        erode = cv2.erode(mask, kernel)
        # 膨胀
        dilate = cv2.dilate(erode, kernel)
        # 闭运算 去掉内部白块
        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel_, iterations=2)

        cnts, h = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.line(frame, (10, line_height), (int(frame.shape[1] * left), line_height), (0, 0, 255), 2)
        cv2.line(frame, (10, line_height - offset), (int(frame.shape[1] * left), line_height - offset), (0, 0, 255), 2)

        cv2.line(frame, (int(frame.shape[1] * left), line_height_), (frame.shape[1] - 10, line_height_), (0, 0, 255), 2)
        for i, c in enumerate(cnts):
            x, y, w, h = cv2.boundingRect(c)
            isValid = (w >= minW) and (h >= minH)
            if not isValid:
                continue
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 255, 255), 2)
            cv2.rectangle(close, (x, y), (x + w, y + h), (255, 255, 255), 2)
            c_point = center(x, y, w, h)
            cv2.circle(frame, c_point, 5, (0, 0, 255), -1)
            cars.append(c_point)

            for (x, y) in cars:
                if x < frame.shape[1] * left:
                    if (y > line_height - offset) and y < line_height:
                        car_num += 1
                        cars.remove((x, y))
                        print(car_num)
                else:
                    # if (y > line_height_ - offset_) and (y < line_height_ + offset_):
                    #     car_num += 1
                    #     cars.remove((x, y))
                    #     print(car_num)
                    pass
        cv2.putText(frame, f"Car Count:{car_num}", (100, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
        cv2.imshow('frame', frame)
        cv2.imshow('nomask', mask)
        cv2.imshow('close', close)

    key = cv2.waitKey(15)
    # if key & 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()
