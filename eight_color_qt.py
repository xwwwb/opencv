# author: xwwwb
# date: 2022-09-19
# description: 色彩空间 因为highgui在apple下有bug 这里的trackber不能用 我用pyqt的控件代替了
from signal import siginterrupt
import cv2
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QSlider
from PyQt6.QtCore import Qt
import sys


def cvPart():
    cv2.namedWindow('color', cv2.WINDOW_NORMAL)
    img = cv2.imread('./resource/demo.jpg')

    def callback():
        pass

    colorspaces = [cv2.COLOR_BGR2RGBA, cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY,
                   cv2.COLOR_BGR2HSV_FULL, cv2.COLOR_BGR2YUV]

    cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces), callback)

    while True:
        index = cv2.getTrackbarPos('curcolor', 'color')

        # 颜色空间转换API
        # cvt_img = cv2.cvtColor(img, colorspaces[index])
        global slideIndex
        cvt_img = cv2.cvtColor(img, colorspaces[slideIndex])
        cv2.imshow('color', cvt_img)

        key = cv2.waitKey(10)
        if key & 0xff == ord('q'):
            break

    cv2.destroyAllWindows()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("色彩空间")
        self.resize(500, 500)
        self.sliderbar = QSlider(Qt.Orientation.Horizontal)
        self.sliderbar.setRange(0, 4)
        self.sliderbar.valueChanged.connect(self.sliderbar_valueChanged)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.sliderbar)
        self.setLayout(self.vbox)

    def sliderbar_valueChanged(self):
        print(self.sliderbar.value())
        global slideIndex
        slideIndex = self.sliderbar.value()


app = QApplication(sys.argv)

slideIndex = 0

window = Window()
window.show()

cvPart()

sys.exit(app.exec())
