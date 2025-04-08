# 方法一：http走私

本题提示有waf，尝试使用http走私绕过



1.cl-cl

这里猜测是，cl=0是waf不对请求头进行处理，而后端对请求头进行了处理，造成http走私

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/182D081363E441868818F955DA0F2A8Eclipboard.png)



2.cl-te

这里猜测是，waf对第一个参数请求进行了响应并报错，但是并没有终止请求把信息发送到了后端，后端处理了请求，返回了目录信息

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/09B468E01DAA4BEA9E5C7A19F2902652clipboard.png)



# 方法二：字符串解析漏洞

该题打开是一个计算器：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/14F5989666774D8D9460805850429AC1clipboard.png)





## 1.提示存在一个waf并且，将提交的参数传给calc.php处理

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/0BCD9940A4474719904A9B8DF897BB62clipboard.png)



## 2.访问calc.php得到calc.php的源代码

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/98C086FF1A9D4F7DA8B0CBD03C2B408Cclipboard.png)

## 3.查看源代码需要传入num参数，再由eval函数执行，但是直接传入phpinfo()；报错。多次尝试只能传入数字。所以猜测传递的参数被一个waf拦截，而且该waf只能传递数字。现在所需的就是要是绕过waf。



## 4.当把参数名num改为nums时：绕过了waf直接访问到了calc.php界面，说明waf只能拦截，num传递来的参数。



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/E528273C284B420ABEDDDEC12966FC69clipboard.png)



## 5.确定waf只能拦截num参数，此时我们构造的payload只要满足：

5.1. 参数名不为num

5.2. 传递到calc.php时，程序会把该参数识别成num



## 6.此时字符串解析漏洞可以派上用场

我们只需构造/?%20num=phpinfo();即可绕过waf

%20num不被waf识别但是到达calc.php时，空格自动删除，所以传递的参数为num=phpinnfo();

（get,post,cookie传递的参数大多都使用parse_str()函数处理）

```javascript
//空格被删除
parse_str(" foo_bar=asd",$o);
print_r($o);

输出：
Array
(
    [foo_bar] => asd
)

```



7.构造的/?%20num=phpinfo();得到phpinfo界面，现在尝试读取目录下的文件构造/?%20num=scandir('/');但是 / 被过滤，所以构造/?%20num=scandir(char(47));



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/C459AF4222B84D3DB4A4993D88023E41clipboard.png)



为了将数组显示出来得用到var_dump()；



## 8. 然后直接去读f1agg文件得内容

/?%20num=var_dump(file_get_contents(chr(47).f1agg));





























