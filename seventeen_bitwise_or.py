# author: xwwwb
# date: 2022-09-23
# description: 或 异或
import cv2
import numpy as np

img = np.zeros((200, 200), np.uint8)
img2 = np.zeros((200, 200), np.uint8)

img[20:120, 20:120] = 255
img2[80:180, 80:180] = 255

new_img = cv2.bitwise_or(img, img2)
new_img2 = cv2.bitwise_xor(img, img2)
cv2.imshow("img", img)
cv2.imshow("img2", img2)
cv2.imshow("new_img", new_img)
cv2.imshow("new_img2", new_img2)


cv2.waitKey(0)
