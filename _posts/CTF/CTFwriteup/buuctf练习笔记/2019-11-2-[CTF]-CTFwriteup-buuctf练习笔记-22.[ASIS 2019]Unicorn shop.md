考察知识点：

1.unicode编码

2.unicode编码的安全问题

https://xz.aliyun.com/t/5402#toc-0



1.网页源码发现存在

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/90D546C01F6247AE89F7B561A74B55BEclipboard.png)



2.报错提示需要一个unicode字符作为参数

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/785DF0EFFEF64222A9BA91376E9530C2clipboard.png)



3.当输入价格为a是购买1，2，3件商品均提示，购买商品错误

说明a的数值大于购买的商品价格8，购买成功



4.搜索数值大于1300的字符

https://www.compart.com/en/unicode/



输入：thousand



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/71D14C20379B4C268953C824A9604539clipboard.png)



5.找一个数值大于1370的

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/7157FC33B38E475791215A91902E0C18clipboard.png)



6.但是需要将其转换成url编码

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/626790998D3843E49F75CDE1F693EB7Fclipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/7621B730F7F346E6910F5FC36E84C748clipboard.png)

其实也就是其utf-8编码，将0x变为%



7.购买超级独角兽

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/D56B0D471A264BD4A5D9705327536380clipboard.png)

