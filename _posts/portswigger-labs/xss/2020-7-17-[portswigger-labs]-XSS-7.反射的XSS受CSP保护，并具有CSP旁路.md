

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/C586B987AEBD4207A7377F51BFE58283clipboard.png)

csp策略阻止了script脚本的执行



观察到scp策略中有一个token参数，思考是否可以进行利用。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/7E79D1CCD2EC4114B1291F1BA30DE807clipboard.png)

发现在/csp-report?token=接口参数中添加的参数会注入到响应头中



但是直接拦截/csp-report接口进行注入却不可以，在搜索接口时，直接注入payload:

```javascript
<script>alert(1)</script>&token=;script-src-elem 'unsafe-inline'
```

script-src-elem 'unsafe-inline'会覆盖script-scr 'self'。使script脚本可以使用。