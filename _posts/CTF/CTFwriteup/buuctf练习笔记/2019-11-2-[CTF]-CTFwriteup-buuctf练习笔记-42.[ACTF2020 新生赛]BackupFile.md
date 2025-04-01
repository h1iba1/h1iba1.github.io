知识点：

1. bak源码泄露

2. php弱类型



1.首页提示

Try to find out source file!



尝试index.php.bak发现源码

```javascript
<?php
include_once "flag.php";

if(isset($_GET['key'])) {
    $key = $_GET['key'];
    if(!is_numeric($key)) {
        exit("Just num!");
    }
    $key = intval($key);
    $str = "123ffwsfwefwf24r2f32ir23jrw923rskfjwtsw54w3";
    if($key == $str) {
        echo $flag;
    }
}
else {
    echo "Try to find out source file!";
}
```



2.利用php弱类型

payload:

```javascript
?key=123
```

