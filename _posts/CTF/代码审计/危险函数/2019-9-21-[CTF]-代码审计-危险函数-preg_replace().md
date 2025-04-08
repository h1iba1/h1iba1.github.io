## preg_replace():

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/代码审计/危险函数/images/D4D6814D9CC04692B9B2283CA267BF70clipboard.png)



原理：preg_replce正则表达式部分包含e参数的时候，进行替换的部分会被当做代码执行。



preg_replace 函数的用法



使用burpsuite抓包，将X_FORWARDED_FOR设置为127.0.0.1，并且将url设置为 

/index.php?pat=/(.*)/e&rep=system('ls')&sub=a 

查看文件列表



