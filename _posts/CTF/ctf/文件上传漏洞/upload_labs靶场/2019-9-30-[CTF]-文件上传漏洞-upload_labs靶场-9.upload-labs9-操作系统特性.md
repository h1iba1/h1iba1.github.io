发现 .， ，::$DATA，大小写也不能绕过。随便试一下.heibai。上传成功

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/4D5015B5BBAF40598E5582AB7E8A5D3Fclipboard.png)

看来还是使用的黑名单，但是做了很多的限制，前面的方法都不能用了。

参考labs3，上传phpinfo.php:jpg文件。

然后再上传php.<文件写入内容。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/EB830F5F2E584A3C95C9F62DBF6CAD2Eclipboard.png)

访问phpinfo.php

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/C916F92754A743399D482839F67846A2clipboard.png)

