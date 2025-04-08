http://chinalover.sinaapp.com/web21/



源码审计：

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



当post的pass小于pass1时得到flag。

此处利用strcmp函数的漏洞，不能处理数组。

post:pass[]=1即可。