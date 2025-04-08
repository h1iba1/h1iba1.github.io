

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/BE460090435B4CF7AC89B91E8EEE39ADclipboard.png)

点击提交后从url中获取storeId参数内容，使用document.write写到页面。



所以payload:

```javascript
/product?productId=1&storeId=<option><script>alert(1)</script>
```



domxss，使用burp验证时，参数可能不会直接返回到html代码中，尽量使用浏览器验证。