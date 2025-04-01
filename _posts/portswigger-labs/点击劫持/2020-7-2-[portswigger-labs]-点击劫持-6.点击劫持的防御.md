# 1. X-Frame-Options 响应头

可以通过以下deny指令禁止将网页包含在框架中：

```javascript
X-Frame-Options: deny
```



使用sameorigin指令 可以将框架限制为与网站相同的来源

```javascript
X-Frame-Options: sameorigin
```



或使用allow-from伪指令访问命名网站：

```javascript
X-Frame-Options: allow-from https://normal-website.com
```



X-Frame-Options在浏览器之间的实现方式不一致（allow-from例如，Chrome 76或Safari 12不支持该指令）。但是，当与内容安全策略一起正确应用作为多层防御策略的一部分时，它可以提供有效的保护，以防止点击劫持攻击。



# 2.内容安全政策（CSP）

内容安全策略（CSP）是一种检测和预防机制，可缓解XSS和Clickjacking等攻击。CSP通常在Web服务器中以以下形式的返回标头实现：

```javascript
Content-Security-Policy: policy
```

其中policy是由分号分隔的一串策略指令。CSP向客户端浏览器提供有关允许的Web资源来源的信息，该浏览器可以将其应用于检测和拦截恶意行为。

以下指令仅允许该页面由相同来源的其他页面构成框架：

```javascript
frame-ancestors 'self'
```

以下指令将完全阻止帧：

```javascript
frame-ancestors 'none'
```

使用内容安全策略来防止点击劫持比使用X-Frame-Options标头更灵活，因为您可以指定多个域并使用通配符。例如：

```javascript
frame-ancestors 'self' https://normal-website.com https://*.robust-website.com
```

CSP还验证父框架层次结构中的每个框架，而X-Frame-Options仅验证顶层框架。

建议使用CSP防止点击劫持攻击。您还可以将其与X-Frame-Options标头结合使用，以在不支持CSP的旧版浏览器（例如Internet Explorer）上提供保护。



