# 知识点：

# 1. php伪随机数

# 2. php_mt_seed 工具使用

参考链接：

https://www.freebuf.com/vuls/192012.html



# 1. 进入页面发现需要输入，一个20位的数字才能得到flag。爆破根本不可能



# 2. 查看check.php发现源码

```javascript
<?php
#这不是抽奖程序的源代码！不许看！
header("Content-Type: text/html;charset=utf-8");
session_start();
if(!isset($_SESSION['seed'])){
    $_SESSION['seed']=rand(0,999999999);
}

mt_srand($_SESSION['seed']);
$str_long1 = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
$str='';
$len1=20;
for ( $i = 0; $i < $len1; $i++ ){
    $str.=substr($str_long1, mt_rand(0, strlen($str_long1) - 1), 1);
}
$str_show = substr($str, 0, 10);
echo "<p id='p1'>".$str_show."</p>";


if(isset($_POST['num'])){
    if($_POST['num']===$str){
        echo "<p id=flag>抽奖，就是那么枯燥且无味，给你flag{xxxxxxxxx}</p>";
    }
    else{
        echo "<p id=flag>没抽中哦，再试试吧</p>";
    }
}
show_source("check.php");
```



# 3. 此时考虑php伪随机数

首先将给出的十位数转换成php_mt_seed工具能够破解形式



```javascript
str1='abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
str2='zOHF0Cxp49'
str3 = str1[::-1]
length = len(str2)
res=''
for i in range(len(str2)):
    for j in range(len(str1)):
        if str2[i] == str1[j]:
            res+=str(j)+' '+str(j)+' '+'0'+' '+str(len(str1)-1)+' '
            break
print res
```



注意10位字符串需要替换自己的



# 4. 使用php_mt_seed工具

github下载：

https://github.com/lepiaf/php_mt_seed



官网：

https://www.openwall.com/php_mt_seed/

### 推荐下载4.0版本



下载下来之后，需要在目录下make一下：

```javascript
root@kali:~/桌面/软件/php_mt_seed-4.0# make
gcc -Wall -march=native -mtune=generic -O2 -fomit-frame-pointer -funroll-loops -fopenmp php_mt_seed.c -o php_mt_seed
php_mt_seed.c:47:2: warning: #warning AVX-512 not enabled. Try gcc -mavx512f (on Intel Knights Landing, Skylake-X, or some newer). [-Wcpp]
   47 | #warning AVX-512 not enabled. Try gcc -mavx512f (on Intel Knights Landing, Skylake-X, or some newer).
      |  ^~~~~~~
root@kali:~/桌面/软件/php_mt_seed-4.0# ./php_mt_seed 51 51 0 61 38 38 0 61 23 23 0 61 38 38 0 61 20 20 0 61 1 1 0 61 48 48 0 61 44 44 0 61 13 13 0 61 3 3 0 61 
Pattern: EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62 EXACT-FROM-62
Version: 3.0.7 to 5.2.0
Found 0, trying 0xfc000000 - 0xffffffff, speed 886.3 Mseeds/s 
Version: 5.2.1+
Found 0, trying 0x38000000 - 0x39ffffff, speed 79.8 Mseeds/s 
seed = 0x382cfaec = 942471916 (PHP 7.1.0+)
Found 1, trying 0xec000000 - 0xedffffff, speed 77.6 Mseeds/s ^C
root@kali:~/桌面/软件/php_mt_seed-4.0# 

```

### 得到随机数种子：942471916

### 注意后面的提示，需要使用php7.1以上的版本生成



# 5. 带到源代码，运行：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/270A7D4A00A14E25A182B5A5F11F088Aclipboard.png)

提交得到flag

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/6C6D973497F843AD8EC0803467673E8Eclipboard.png)

