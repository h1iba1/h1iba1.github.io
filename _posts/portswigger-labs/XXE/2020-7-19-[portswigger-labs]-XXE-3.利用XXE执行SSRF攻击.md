检查库存处抓包，发现xml格式数据

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/XXE/images/37692C97E92C445DBC3488F975FC0DC8clipboard.png)



使用文件爆破进行ssrf探测

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/XXE/images/5DC21AF604A74DB9A3AEAC837A9C561Cclipboard.png)



当访问的路径为：/latest/meta-data/iam/security-credentials/admin

返回JSON SecretAccessKey。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/XXE/images/FBFEE71D254C44709CBA70A3BA316749clipboard.png)

