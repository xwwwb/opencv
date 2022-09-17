splite()费时
可以使用NumPy索引获得通道

```
B = img_OpenCV[:, :, 0]
G = img_OpenCV[:, :, 1]
R = img_OpenCV[:, :, 2]
```
可以使用NumPy在一条语句中将图像从BGR转为RGB
```
img_matplotlib = img_OpenCV[:, :, ::-1]
```
