该网站使用url重置密码。



## 1. 抓取重置密码数据包

![](images/59683C3F73AA43E7AE3B9A026C9EC2A5clipboard.png)

## 2. 尝试添加：X-Forworded-For标头，覆盖生成的链接

![](images/656910FB4D334E7D96385218AC20AF45clipboard.png)

X-Forwarded-Host：填写自己服务器的链接

username：填写受害者名称



## 3. 观察服务器访问记录，发现重置密码链接令牌

![](images/F52271CD3E474B728D8EC16F1E3EF8E3clipboard.png)

将令牌黏贴到攻击网址后缀即可，进入carlos用户的密码重置界面