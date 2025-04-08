直接访问/admin目录

提示只有admin用户能够访问



## 修改邮箱处，抓包发现json数据传输的email，在其中添加参数: "roleid":2

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/9703CE528E0A4CAE865F69674F8AFFD0clipboard.png)



再次访问/admin目录时，既有访问权限

