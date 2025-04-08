## 1. 登陆admin用户。将提升用户权限步骤抓包

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/A91C5E05B6764E2EA0F4CA4EA817DF2Fclipboard.png)



## 2. 登陆wiener用户，将url更改为：

```javascript
username=wiener&action=upgrade
```

尝试更改wiener用户的权限

提示：未授权

随机跳转到login界面



admin用户更改权限之后跳转到admin界面。普通用户执行更改权限操作跳转到login界面



推测可能和referer头有关：



## 3. 抓包更改wiener用户url和referer头

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/876AB44FFC4F4B63B0CF7D90D3C0D621clipboard.png)

放包之后即可更改用户权限