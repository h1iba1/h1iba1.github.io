## 提交反馈处存在命令执行注入

服务器端应用程序会向站点管理员生成一封包含反馈的电子邮件。为此，它mail使用提交的详细信息调出程序。例如：

```javascript
mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com
```

mail命令 的输出（如果有）不会在应用程序的响应中返回，因此使用echo有效负载将无效。在这种情况下，您可以使用ping命令延时检测





paylaod:

```javascript
email=||+ping+-c+10+127.0.0.1+||
```





“||”分隔符

同C、C++语言逻辑运算符"||"类似，遇到首个命令执行成功后，后面的命令不会执行。如：

输入：命令A || 命令B || 命令C

先执行命令A，若A命令执行失败则再执行命令B。假如命令B执行成功，则停止，C命令不会被执行到。