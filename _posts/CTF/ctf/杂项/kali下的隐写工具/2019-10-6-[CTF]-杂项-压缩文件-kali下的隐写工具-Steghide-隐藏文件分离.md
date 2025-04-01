Steghide是数据隐藏工具，通过此工具你可以轻松的将文件隐藏到一个图片/音频中。一旦文件被隐藏到图片中，那么图片看起来依然就是图片，可以正常使用图片浏览工具打开查看图片，唯一的区别是它里面包含着被隐藏的文件。这样做的好处是便于传播或发送一些私密的文件，防止被人截取。

Steghide可以把信息隐藏在AU, BMP, JPEG 或 WAV格式的文件中。

以一个文本文件为例

创建一个文本文件，随便写入点东西：

```javascript
# vim my_secret.txt
```



![](images/4DD97EA7E54A4C0FABAC118BE0219CACt%2009.31.12.png)

我要把my_secret.txt隐藏到图片中：

```javascript
# steghide embed -ef my_secret.txt -cf normal_pic.jpg
```

设置密码；

下图中包含了隐藏文件（和原始图片相比文件变大了）：

![](images/DA90849B3E67414FBCDDE38339DFB9DCnormal_pic.jpeg)

获得隐藏文件：

```javascript
# steghide extract –sf normal_pic.jpg
```

