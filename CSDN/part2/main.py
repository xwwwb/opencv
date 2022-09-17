# author: xwwwb
# date: 2022-07-10
# description: cv2的基本输入输出
import argparse
import cv2

parser = argparse.ArgumentParser()
parser.add_argument('path_image', help="path to input image to be displayed")
parser.add_argument('path_image_output',
                    help="path of the procesed image to be saved")
args = parser.parse_args()
image = cv2.imread(args.path_image)

# 下面的看不太懂
# args = vars(parser.parse_args())
# image2 = cv2.imread(args['path_image'])

cv2.imshow('loaded image', image)
# cv2.imshow('loaded image2', image2)

args = vars(parser.parse_args())
cv2.imwrite(args['path_image_output'], image)
cv2.waitKey(0)
cv2.destroyAllWindows()
