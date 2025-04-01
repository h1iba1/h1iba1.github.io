# 1.f12查看看到一个source.php

![](images/6B22815557A34894BFFA8EB3DCFB83F4clipboard.png)



# 2.访问souce.php

```python
<?php
highlight_file(__FILE__);
class emmm
{
    public static function checkFile(&$page)
    {
//        白名单
        $whitelist = ["source"=>"source.php","hint"=>"hint.php"];

//        不存在$page或$page不是字符串
//        return flase
        if (! isset($page) || !is_string($page)) {
            echo "you can't see it";
            return false;
        }

//        $page在白名单中返回true
        if (in_array($page, $whitelist)) {
            return true;
        }

//截取0-最后的字符串
        $_page = mb_substr(
            $page,
            0,
//            在$page后面跟了一个？，并查找？最后出现的位置，所以，这里获取的是最后一个字符的索引
            mb_strpos($page . '?', '?')
        );

//        if$page 还在白名单中则返回true
        if (in_array($_page, $whitelist)) {
            return true;
        }

//        $page url解码得到$_page
        $_page = urldecode($page);

//        截取0-最后的字符
        $_page = mb_substr(
            $_page,
            0,
            mb_strpos($_page . '?', '?')
        );
//
        if (in_array($_page, $whitelist)) {
            return true;
        }
        echo "you can't see it";
        return false;
    }
}

//请求的file不为空，而且is_string&&checkFile return 1
//就包含文件
if (! empty($_REQUEST['file'])
    && is_string($_REQUEST['file'])

//    该题目标file=ffffllllaaaagggg时返回true
//    但是采用了白名单
//    有一个urldecode可以利用
//


    && emmm::checkFile($_REQUEST['file'])
) {
    include $_REQUEST['file'];
    exit;
} else {
    echo "<br><img src=\"https://i.loli.net/2018/11/01/5bdb0d93dc794.jpg\" />";
}
?>
```

得到源码



3.代码大体意思就是输入的file参数值只能为 $whitelist = ["source"=>"source.php","hint"=>"hint.php"];

而且还是白名单 



4.一开始以为利用点在urldecode,后面尝试，

source.php?file=source.php?file=../../../../../../ffffllllaaaagggg得到flag



5.只能说自己的还太年轻，source.php?file=ffffllllaaaagggg这个有想到。但是没想到../



6.所以这个题的思路就是source.php被该函数截取出来，绕过了前面的白名单检测，到include()时为source.php?file=../../../../../../ffffllllaaaagggg读取到flag

```python
        $_page = mb_substr(
            $page,
            0,
//            在$page后面跟了一个？，并查找？最后出现的位置，所以，这里获取的是最后一个字符的索引
            mb_strpos($page . '?', '?')
        );
```





