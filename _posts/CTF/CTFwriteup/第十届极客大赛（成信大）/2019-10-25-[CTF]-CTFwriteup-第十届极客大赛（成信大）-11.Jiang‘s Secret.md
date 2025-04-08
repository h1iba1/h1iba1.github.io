# Jiang‘s Secret

## 1.f12查看网页源码

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/00BFC7AC4DC445E3BBB33820B73EBF35Jiang‘s%20Secret1.png)

## 2.访问该php文件

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/578383E2481A4E92879C126198D40DB7Jiang‘s%20Secret2.png)

## 3.点击secret，跳转到end.php
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/18A0819447484F80B52DE9F5F0EE8DC0Jiang‘s%20Secret3.png)

提示：没看清么？回去再仔细看看吧。

感觉中间经过了302跳转，抓包查看一下

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/5F8ACB603239466FAD059811395E5DDDJiang‘s%20Secret4.png)

## 4.数据包中存在   secr3t.php  文件，访问试试：

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/EE3EB358B254411EAD775588F7282A66Jiang‘s%20Secret5.png)

## 5.网页源码，提示flag在flag中，而且该页面存在文件包含漏洞，虽然过滤了几个关键字，但是php://filter没有过滤，可以采用读文件源码的伪协议

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/664B1D861BCD427DBC388FF60C5220CEJiang‘s%20Secret6.png)

解码即可得到flag