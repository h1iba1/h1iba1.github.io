和labs11一样只不过变成了post提交数据。

直接写heibai.php%00不行。显示上传失败。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/0A5289DD3CCC42498BDF24580448F854clipboard.png)



查了资料才发现。使用00截断。并且需要更改上传的文件路径名的hex编码为00

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/AD4C73D9643E4830A32A9317DB06F2B4clipboard.png)



文件上传成功：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/3B27D40AE436453D90046E9A25A6C672clipboard.png)

访问文件：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/ACF298F797B04EB79102DA84F49EF52Bclipboard.png)

