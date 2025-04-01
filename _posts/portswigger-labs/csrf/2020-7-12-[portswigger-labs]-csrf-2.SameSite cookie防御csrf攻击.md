# 使用SameSite cookie 防御CSRF攻击。

sameSite属性被添加到Set-Cookie当服务器发出一个cookie响应报头，并且该属性可以给出两个值，Strict或Lax。例如：

```javascript
SetCookie: SessionId=sYMnfCUrAlmqVVZn9dqevxyFpKZt30NN; SameSite=Strict;
SetCookie: SessionId=sYMnfCUrAlmqVVZn9dqevxyFpKZt30NN; SameSite=Lax;
```

## 1. strict

如果该SameSite属性设置为Strict，那么浏览器将不会在来自另一个站点的任何请求中包含cookie。这是最防御性的选项，但是它可能会损害用户体验，因为如果已登录的用户遵循指向站点的第三方链接，那么他们似乎将无法登录，因此需要再次登录以正常方式与网站互动。



## 2.lax

如果将该SameSite属性设置为Lax，则浏览器将在来自另一个站点的请求中包含cookie，但前提是必须满足以下两个条件：



- 该请求使用GET方法。使用其他方法（例如POST）的请求将不包含cookie。

- 该请求来自用户的顶级导航，例如单击链接。其他请求（例如由脚本启动的请		      求 ）将不包含cookie。



SameSite在Lax模式下 使用Cookie 确实可以部分防御CSRF攻击，因为作为CSRF攻击目标的用户操作通常是使用POST方法实现的。这里有两个重要警告：

- 某些应用程序确实使用GET请求实施敏感操作。

- 许多应用程序和框架可以容忍不同的HTTP方法。在这种情况下，即使应用程序本身通过设计采用了POST方法，它实际上也会接受切换为使用GET方法的请求。

由于上述原因，不建议仅依靠SameSite cookie来防御CSRF攻击。但是，与CSRF令牌结合使用时，SameSite cookie可以提供额外的防御层，可以减轻基于令牌的防御中的任何缺陷。