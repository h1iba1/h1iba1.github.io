1.打开网页发现三个文件：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/6280761DFD414BCEBB81798D60BA1607clipboard.png)



2. 依次打开：

2.1 flag.txt

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/7490DF9B6EA64A2EA09B025986FF2282clipboard.png)



2.2 welcome.txt

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/01DB11714738407395E75401EA73BD3Cclipboard.png)



2.3 hints.txt

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/EB7BFA71399442EE9B3FE9748D78AB2Eclipboard.png)



根据hints.txt可以发现每个文件打开都需要md5(cookie_secret+md5(filename))

而此时cookie_secrect不知道，http请求包中也没有。所以现在的首要思路就是找到cookie_secrect



2.4查看大佬们的wp

welcome提示了render，render是python的一个模板，所以考虑是否存在模板注入。

关于模板注入的文章。

https://www.k0rz3n.com/2018/11/12/%E4%B8%80%E7%AF%87%E6%96%87%E7%AB%A0%E5%B8%A6%E4%BD%A0%E7%90%86%E8%A7%A3%E6%BC%8F%E6%B4%9E%E4%B9%8BSSTI%E6%BC%8F%E6%B4%9E/



2.5 判断是否存在注入

error?msg={{1^0}}

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/EB299E4BE3FF4522A8AB4B1E818C0DB3clipboard.png)



1^0为0说明执行了表达式。存在注入



2.6 cookie_secret存在于handler.settings中，直接payload:

error?msg={{handler.settings}}

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/865EB4511FFD499491EBC5116CC3B501clipboard.png)

得到cookie_secret。



2.7 根据hint提示：filehash=md5(cookie_secret+md5(filename))

所以payload:

file?filename=/fllllllllllllag&filehash=md5(cookie_secret+md5(/fllllllllllllag))  (此处需要算出md5值）

