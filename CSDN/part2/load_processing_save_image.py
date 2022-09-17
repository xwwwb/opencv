# author: xwwwb
# date: 2022-07-10
# description: 输入输出案例 转图片为灰度
import argparse
import cv2


parser = argparse.ArgumentParser()
parser.add_argument('path_image_input',
                    help='path to input image to be displayed')
parser.add_argument('path_image_output',
                    help='path of the processed image to be saved')
args = vars(parser.parse_args())
image_input = cv2.imread(args['path_image_input'])
cv2.imshow('loaded image', image_input)
# 将图片转为灰度
gray_image = cv2.cvtColor(image_input, cv2.COLOR_BGR2GRAY)
# 如果已经加载了RGB彩色图像并想转为灰度 使用
# gray_image = cv2.cvtColor(image_input,cv2.COLOR_RGB2GRAY)
cv2.imshow("gray_image", gray_image)
cv2.imwrite(args['path_image_output'], gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
