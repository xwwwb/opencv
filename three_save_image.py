# author: xwwwb
# date: 2022-09-18
# description: 保存文件
import cv2

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread('./resource/demo.jpg', cv2.IMREAD_COLOR)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(0)

    if (key & 0xff) == ord('q'):
        break
    elif(key & 0xff) == ord('s'):
        # 将Mat 转为图片
        cv2.imwrite('./resource/three_output.png', img)

cv2.destroyAllWindows()
