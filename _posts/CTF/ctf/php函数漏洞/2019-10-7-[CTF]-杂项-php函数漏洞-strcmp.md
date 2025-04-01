## strcmp():

字符串比较函数。

```javascript
strcmp($string1,$string2);
//当$string1>$string2时返回flase,当string1>string2时返回true
```



## 漏洞利用点：

不能处理数组。



## 实列：

CGCTF pass check

http://chinalover.sinaapp.com/web21/

```javascript
$pass=@$_POST['pass'];
$pass1=***********;//被隐藏起来的密码
if(isset($pass))
{
if(@!strcmp($pass,$pass1)){
echo "flag:nctf{*}";
}else{
echo "the pass is wrong!";
}
}else{
echo "please input pass!";
}
?>
```

当psot

pass[]=1时即可绕过。