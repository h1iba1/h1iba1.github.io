```javascript
flag In the variable ! <?php  

error_reporting(0);
include "flag1.php";
highlight_file(__file__);
if(isset($_GET['args'])){
    $args = $_GET['args'];
    if(!preg_match("/^\w+$/",$args)){
        die("args error!");
    }
    eval("var_dump($$args);");
}
?>
```

一开始以为这个题是要绕过正则表达式。preg_match有三个方式可以绕过，在这里再复习一下

1.数组绕过

2.当正则表达式结尾含，/m,^,$时会匹配结尾

可以采用/n绕过

3.最大回溯绕过

但是此题的关键为：

```javascript
eval("var_dump($$args);");
```

$$args可以采用变量覆盖，题目提示flag in the variable

可采用全局变量：

- 

- 

- 

- 

- 

- 

- 

- 

- 

*payload:*[*http://123.206.87.240:8004/index1.php?args=GLOBALS*](http://123.206.87.240:8004/index1.php?args=GLOBALS)