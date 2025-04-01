## 1.  跨域资源共享是同源策略（same-origin policy)的一种放宽策略



## 2. Access-Control-Allow-Origin：* 

web浏览器将Access-Control-Allow-Origin与请求网站的来源进行比较，如果匹配则允许访问响应



## 3. Access-Control-Allow-Credentials: true 

跨域资源请求的默认行为是在不使用Cookie和Authorization标头之类的凭据的情况下传递请求。

通过将CORS Access-Control-Allow-Credentials标头设置为true ，跨域服务器可以在将凭据传递给响应时允许读取响应



## 4. 使用通配符放宽cors规范

```javascript
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
```

禁止这样做，因为这样做很危险，不安全，因此会将目标站点上的所有经过身份验证的内容暴露给所有人。



不能在其他值内使用*，例如：

```javascript
Access-Control-Allow-Origin: https://*.normal-website.com
```



## 5. 其他cors标头

request:

```javascript
OPTIONS /data HTTP/1.1
Host: <some website>
...
Origin: https://normal-website.com
//访问控制请求方法
Access-Control-Request-Method: PUT
//访问控制请求头
Access-Control-Request-Headers: Special-Request-Header
```

response:

```javascript
HTTP/1.1 204 No Content
...
//访问控制允许源
Access-Control-Allow-Origin: https://normal-website.com
//访问控制允许方法
Access-Control-Allow-Methods: PUT, POST, OPTIONS
//访问控制允许头
Access-Control-Allow-Headers: Special-Request-Header
//访问控制允许证书
Access-Control-Allow-Credentials: true
//访问控制允许最大时间范围
Access-Control-Max-Age: 240
```







