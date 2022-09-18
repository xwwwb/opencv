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

- setMouseCallback(winname,callback,userdata)
- callback(event,x,y,flags,userdata)

# TrackBar

- createTrackbar(trackbarName,winname,value,count,callback) value 当前值 count 最大值 callback 回调函数
- callback(value)
- getTrackbarPos(trackbarName,winname)

不知道是什么问题 窗口会闪退
