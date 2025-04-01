当请求使用POST方法时，某些应用程序正确地验证了令牌，但是当使用GET方法时，跳过了验证。

在这种情况下，攻击者可以切换到GET方法来绕过验证并发送CSRF攻击：

GET /email/change?email=pwned@evil-user.net HTTP/1.1

Host: vulnerable-website.com

Cookie: session=2yQIDcpia41WrATfjPqvm9tOkDvkMvLm