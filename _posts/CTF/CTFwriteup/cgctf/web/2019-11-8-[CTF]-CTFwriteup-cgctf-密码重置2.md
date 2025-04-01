1.TIPS:
  1.管理员邮箱观察一下就可以找到
  2.linux下一般使用vi编辑器，并且异常退出会留下备份文件
  3.弱类型bypass

2.进入首页发现需要输入email和token

email提示说，观察一下就能找到。emmmmmmm，我找不到，后面看wp为admin@网址

所以为：admin@nuptzj.cn



3.此时还差token

tips2百度一下，发现linux异常退出的备份文件为.swp

所以访问：http://nctf.nuptzj.cn/web14/submit.php.swp

提示404......

然后访问：http://nctf.nuptzj.cn/web14/index.php.swp

还是404

后面看了wp才发现。submit.php.swp前面也要加.

所以访问：http://nctf.nuptzj.cn/web14/.submit.php.swp

返回页面：

```javascript


........这一行是省略的代码........

/*
如果登录邮箱地址不是管理员则 die()
数据库结构

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `token` int(255) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `token`) VALUES
(1, '****不可见***', '***不可见***', 0);
*/


........这一行是省略的代码........

if(!empty($token)&&!empty($emailAddress)){
	if(strlen($token)!=10) die('fail');
	if($token!='0') die('fail');
	$sql = "SELECT count(*) as num from `user` where token='$token' AND email='$emailAddress'";
	$r = mysql_query($sql) or die('db error');
	$r = mysql_fetch_assoc($r);
	$r = $r['num'];
	if($r>0){
		echo $flag;
	}else{
		echo "失败了呀";
	}
}
	
```



4.根据页面知道，strlen(token)=10&tonken='0'

此时可以采用弱类型：0=0e12345678

所以email=admin@nuptzj.cn

token=0e12345678

