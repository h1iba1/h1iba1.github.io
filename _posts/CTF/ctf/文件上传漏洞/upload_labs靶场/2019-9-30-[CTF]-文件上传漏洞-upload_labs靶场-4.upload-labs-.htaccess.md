直接上传测试发现，php，php3,phtml无法上传。但是随便输入一个phpinfo.a却可以上传。判断依旧使用黑名单。考虑上传.htaccess文件。（上传.htaccess文件适用于labs3）

上传.htaccess文件

```javascript
<FilesMatch "heibai">//注意这里的heibai需修改为上传文件的文件名
    SetHandler application/x-httpd-php
</FilesMatch>
```

上传成功。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/7ACD1DEF42544F028771BF0D1661DEB4clipboard.png)

接下来上传一个黑名单里并不存在的文件后缀木马。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/8D741FB0B20D442ABCC034F244DCD450clipboard.png)

访问该文件。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/6981EE0438FF4E41A52CAD12C8231531clipboard.png)

参考链接:

http://lawlietweb.com/2018/06/07/upload-labs/#%E7%AC%AC%E4%B8%89%E5%85%B3-amp-%E7%AC%AC%E5%9B%9B%E5%85%B3