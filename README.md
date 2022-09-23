# 创建和显示窗口

- namedWindow() 给窗口打编号
- imshow()
- destroyAllWindows()
- resizeWindow 默认窗口大小和图片大小一样

# 读取和保存图像

- imread() 读取图像
- imwrite() 保存图像

# 读取和保存视频

- VideoCapture() 读取视频
- VideoWriter() 保存视频
- cap.read() 读取视频帧 返回两个值 一个是状态一个是帧
- cap.isOpened() 检查是否成功打开
- cap.get() 获取视频属性
- cap.set() 设置视频属性
- cap.release() 释放视频

# 鼠标控制

- setMouseCallback(winname,callback,us erdata)
- callback(event,x,y,flags,userdata)

# TrackBar

- createTrackbar(trackbarName,winname,value,count,callback) value 当前值 count 最大值 callback 回调函数
- callback(value)
- getTrackbarPos(trackbarName,winname)

不知道是什么问题 窗口会闪退

# 色彩空间

HSV(HSB)
Hue: 色相，色彩，红色，蓝色
Saturation: 饱和度，纯度，鲜艳程度
Value: 亮度，明度，明亮程度 Brightness

YUV 常用作视频中
YUV 4:2:0
YUV 4:2:2
YUV 4:4:4

# Numpy

- 创建数组 array()
- 创建全零 zeros() / ones
- 全值数组 full()
- 创建单元数组 identity() / eye()

- 索引 [y,x]
- [y,x,channel] 通道索引 可以认为 [y,x,z]

# Mat

# 图像融合

addWeighted(A,alpha,B,beta,gamma)
aplha A 的权重
beta B 的权重
gamma 静态权重
