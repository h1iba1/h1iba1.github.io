# 文件包含漏洞利用图片马



发现题目变了，需要配合文件包含漏洞来利用漏洞：

![](images/A89F116A505F4BB4BA3F17B0A594C7EBclipboard.png)



点击文件包含漏洞，发现源代码。

![](images/7D8BC7262BAD4663BBDD6D5E8C051398clipboard.png)

构造图片马：

最简单的图片马构造方法：

copy /b C:\Users\microsoft\Desktop\文件上传\1.jpg+C:\Users\microsoft\Desktop\文件上 传\phpinfo.php phpinfo.jpg

![](images/638EAA74B2DB42F1BF35B721278BE0B9clipboard.png)

使用notepad++打开图片文件，文件最后有我们构造的恶意代码。

![](images/0A02EC17CF58410499A0BBBAC3057E84clipboard.png)



上传图片马，使用文件包含漏洞访问：

![](images/B4E80B6E7D9F485DAB01F1136846E5C7clipboard.png)

成功执行图片马中的php代码。

