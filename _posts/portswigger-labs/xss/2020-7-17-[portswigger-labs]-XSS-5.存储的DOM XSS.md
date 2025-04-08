

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/9C63CAB1D1574CDC86F4F11990AC5B7Dclipboard.png)

js文件将输入值的第一个<>替换未&lt;,&gt;



可以使用<><img src=1 onerror=alert(1)>

waf只对第一个<>进行过滤，后面的没有没有，造成xss