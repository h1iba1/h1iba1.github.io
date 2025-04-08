## 1. 登陆administrator用户。发现用户权限升级操作。最后需要执行yes操作。将该步骤抓包

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/C0906A92797949B19429A12A9D54121Cclipboard.png)



## 2. 登陆wiener用户。发送请求抓包。将数据包中的GET请求改为POST

数据包改为：

```javascript
action=upgrade&confirmed=true&username=wiener
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/E1730215BFB64E3887C0F80B0F41BDF7clipboard.png)



## 3. 放包即可进入admin界面，此时wirner用户已经是管理员权限。