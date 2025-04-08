访问myaccout界面。发现url id参数为用户名。

## 1. 将id值改为administrator得到admin界面

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/4B24E81C0C974BC5A5B1D907169EAC0Fclipboard.png)

虽然用户密码不可见。但是可以通过审查元素，将type=password改为type=text。从而显示密码



## 2. 得到密码之后登陆administrator用户。访问admin panel面板。删除carlos用户

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/AB7050255BE84A03BF51BB7BB37735B7clipboard.png)

