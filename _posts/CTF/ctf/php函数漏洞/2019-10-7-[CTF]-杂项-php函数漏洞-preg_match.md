preg_match函数

用于正则表达式判断。



漏洞点1：

## 数组绕过

待绕过目标如下

```javascript
<?php
echo preg_match('/<\?.*[(`;?>].*/is', $_GET['a']);
```



```javascript
http://localhost/?a=<?php phpinfo();?>&a=123123
或者
http://localhost/?a[]=<?php phpinfo();?>
```



漏洞点2:

## 最大回溯绕过：

```javascript
<?php phpinfo();?>//AAAAAAA······ 此处省略数万个
 
Tips: pcre.backtrack_limit（回溯限制），当正则匹配的回溯次数达到这个值时
就不会再匹配了，所以就没有匹配到最前面的eval
```

