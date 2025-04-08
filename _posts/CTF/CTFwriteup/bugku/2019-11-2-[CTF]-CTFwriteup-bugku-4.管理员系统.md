使用admin,password登陆，提示：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/bugku/images/EA7963CF57AF47169C457FCA6A7F0198clipboard.png)

所以采用X-Forworded=For:127.0.0.1头登陆

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/bugku/images/1D67BE0CC9024B479E5C1C4571B2AC32clipboard.png)

但是提示错误。

后面看了wp才发现，返回的源码里有一个字符串，看起来像是base64解码得到test123

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/bugku/images/1C866BFC3A934CDBA20AE0A2916A7970clipboard.png)



密码使用test123登陆，即可得到flag

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/bugku/images/3ECC1908E5A648D490D6A59BA7C7EBB9clipboard.png)

