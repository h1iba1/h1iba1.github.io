该网站密码登陆之后该需要输入一遍邮箱验证码才能登陆。但是此过程存在逻辑错误:

第一步输入已知账号的密码登陆，第二步输入邮箱邮箱验证码处抓包将。cookie中的用户名替换为攻击账号。发送到Intruder模块爆破验证码



1. 使用wiener:peter账号登陆

在跳转到/login2处抓包，将用户名改为carlos。（此处是为了使服务器发送carlos的验证码，以为使carlos用户在操作）

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/1BB98C605BF744698CEEDB5D25EBC9E4clipboard.png)



2. wiener用户在 /login2 发送一个错误的验证码，并抓包

将用户名更改为carlos.并准备爆破验证码

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/F9E94E9961F345F9B236C56679C24CFDclipboard.png)



3. 爆破成功。状态吗为302.

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/F44D9C7C0B024737AC3B882EBDCA4A2Cclipboard.png)



4.此时因为有csrftoken的存在不能直接使用验证码去登陆。而因该在响应模块中用浏览器打开。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/256835CA552A46BA8959A7A512C01D5Aclipboard.png)

访问链接，到carlos账户的myaccout界面即可