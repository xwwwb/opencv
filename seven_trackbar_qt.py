# author: xwwwb
# date: 2022-09-18
# description: Trackbar

import cv2
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSlider
import sys
from PyQt6.QtCore import Qt


def cvPart():
    def callback(x):
        print(x)

    # 创建窗口
    cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)
    # 创建滑动条
    cv2.createTrackbar('R', 'trackbar', 0, 255, callback)
    cv2.createTrackbar('G', 'trackbar', 0, 255, callback)
    cv2.createTrackbar('B', 'trackbar', 0, 255, callback)

    img = np.zeros((480, 460, 3), np.uint8)

    while True:
        global b, g, r
        img[:] = [b, g, r]
        cv2.imshow('trackbar', img)

        key = cv2.waitKey(10)
        if key & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Trackbar")
        self.resize(500, 500)
        self.sliderbarR = QSlider(Qt.Orientation.Horizontal)
        self.sliderbarG = QSlider(Qt.Orientation.Horizontal)
        self.sliderbarB = QSlider(Qt.Orientation.Horizontal)

        self.sliderbarR.setRange(0, 255)
        self.sliderbarG.setRange(0, 255)
        self.sliderbarB.setRange(0, 255)

        self.sliderbarR.valueChanged.connect(self.sliderbarR_valueChanged)
        self.sliderbarG.valueChanged.connect(self.sliderbarG_valueChanged)
        self.sliderbarB.valueChanged.connect(self.sliderbarB_valueChanged)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.sliderbarR)
        self.vbox.addWidget(self.sliderbarG)
        self.vbox.addWidget(self.sliderbarB)
        self.setLayout(self.vbox)

    def sliderbarR_valueChanged(self):
        global r
        r = self.sliderbarR.value()

    def sliderbarG_valueChanged(self):
        global g
        g = self.sliderbarG.value()

    def sliderbarB_valueChanged(self):
        global b
        b = self.sliderbarB.value()


b = g = r = 0
app = QApplication(sys.argv)
window = Window()
window.show()
cvPart()
print(locals())
sys.exit(app.exec())
