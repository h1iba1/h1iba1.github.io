直接访问/admin目录

发现cookie中存在一个Admin=false参数

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/35B1E239CC444157A390DA16B8854DA5clipboard.png)

将参数修改为：Admin=true

访问到/admin目录

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/28F1D2261CAC4CFBB210C4D8A10CE09Fclipboard.png)

删除用户时，将Admin=true即可删除用户