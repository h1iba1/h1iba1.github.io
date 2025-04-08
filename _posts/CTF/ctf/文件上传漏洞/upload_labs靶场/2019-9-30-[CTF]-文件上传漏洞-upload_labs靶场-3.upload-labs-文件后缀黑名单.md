直接上传phpinfo.php文件发现返回提示：不允许上传asp，jsp...推测可能使用黑名单限制。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/6C1C31B833EC4A87A01AEB3D9CB5745Fclipboard.png)

遂更改后缀名为php3，发现上传上传。并返回上传文件路径

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/1B3D782F49B3431EADAC47332F3AE6DAclipboard.png)

直接访问文件发现虽无报错，但却无法解析。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/DC9D749A29064CB689E9F08862E3851Fclipboard.png)

查看apache配置文件httpd.conf。发现AddType被注释，且只允许访问.php/.phtml后缀的文件。取消注释。重启服务器。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/AEE77FF3A2EA4C5E9806E16A73E0AE23clipboard.png)

上传.phtml结尾的文件，返回phpinfo()信息。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/B3F3B757848C4F708AD6D4D9739616DEclipboard.png)

总结:

1.apache服务器默认关闭非php后缀的解析方式。需到http.conf文件中开启。



