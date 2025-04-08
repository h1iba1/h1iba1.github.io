利用ssrf进行内网探测



使用bp intruder爆破内网8080端口，得到一个和其他访问不一样的status。说明该ip8080端口存在服务

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/ssrf/images/4A788FC3EF22459A8A83DD6B7914EC2Dclipboard.png)

访问admin目录

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/ssrf/images/D4896BF059F548A6A9AB4B4D8398EF25clipboard.png)

发现删除用户的连接



访问：http://192.168.0.122:8080/admin/delete?username=carlos

即可删除carlos用户