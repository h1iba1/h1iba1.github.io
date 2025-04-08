使用密码找回功能。发现找回密码时会将url重置链接发送到用户邮箱。用户打开链接即可重置密码



## 1. 找回已知账户的密码，在email中访问重置密码链接



## 2. 在重置界面，输入新密码最后一步抓包。

删除url中的token参数。和post中的参数。将username改为carlos。发送请求。发现密码更改成功。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/307BFF6473BC450C8A10AE8B14CE7ABCclipboard.png)

这是因为服务端没有验证重置链接，也没有将用户和重置链接绑定在一起。