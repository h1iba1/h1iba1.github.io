当攻击者可控制的数据可以写入触发跨域导航的接收器时，就会出现基于DOM的开放重定向漏洞。例如，以下代码由于处理location.hash属性的不安全方式而容易受到攻击：

```javascript
let url=/https?:\/\/.+/.exec(location.hash)
    if(url) {
        location = url[0];
    }
```



如果攻击者可以控制协议，还有可能升级为JavaScript注入攻击。攻击者可以使用javascript:伪协议构造URL，以在浏览器处理URL时执行任意代码。



以下是一些可能导致基于DOM的开放重定向漏洞的主要接收器：

```javascript
location
location.host
location.hostname
location.href
location.pathname
location.search
location.protocol
location.assign()
location.replace()
open()
domElem.srcdoc
XMLHttpRequest.open()
XMLHttpRequest.send()
jQuery.ajax()
$.ajax()
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/基于DOM的漏洞/images/6D9E0781E30047789DD1DC6432ADC27Fclipboard.png)

```javascript
//从url参数中获取https协议后的内容，如果内容存在则使用location.href定位到网站内容
//实现重定向

<a href='#' onclick='returnUrl = /url=(https?:\/\/.+)/.exec(location); 
if(returnUrl)location.href = returnUrl[1];else location.href = "/"'>
Back to Blog</a>
```



网站的back to blog处从url获取返回连接可能存在重定向漏洞



poc:

```javascript
https://your-lab-id.web-security-academy.net/post?postId=4
&url=https://your-exploit-server-id.web-security-academy.net/
```





