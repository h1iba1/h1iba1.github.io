sqlmap详细命令：

- –is-dba 当前用户权限（是否为root权限）

- –dbs 所有数据库

- –current-db 网站当前数据库

- –users 所有数据库用户

- –current-user 当前数据库用户

- –random-agent 构造随机user-agent

- –passwords 数据库密码

- –proxy http://local:8080 –threads 10 (可以自定义线程加速) 代理

- –time-sec=TIMESEC DBMS响应的延迟时间（默认为5秒）



# 一些基本参数讲解：

-u:后接url，常用于get注入

-l:可以将bp中的日志导出来交给sqlmap一个一个检测是否存在注入。

-m:从文本中获取多个目标扫描

文本保存的url格式如下：

```javascript
www.target1.com/vuln1.php?q=foobar
www.target2.com/vuln2.asp?id=1
www.target3.com/vuln3/id/1*
```



-r:可以从文本文件中获取http请求，这样就可以跳过一些参数的设置（如：cookie,post等）



-g:sqlmap可以测试注入Google的搜索结果中的GET参数（只获取前100个结果）

例子：

```javascript
python sqlmap.py -g "inurl:\".php?id=1\""
```

（很牛B的功能，测试了一下，第十几个就找到新浪的一个注入点）。此外可以使用-c参数加载sqlmap.conf文件里面的相关配置。



--data:此参数是把数据以POST方式提交，sqlmap会像检测GET参数一样检测POST的参数。

例子：

```javascript
python sqlmap.py -u "http://www.target.com/vuln.php" 
--data="id=1" -f --banner --dbs --users
```



--param-del

当GET或POST的数据需要用其他字符分割测试参数的时候需要用到此参数。

例子：

```javascript
python sqlmap.py -u "http://www.target.com/vuln.php" -
-data="query=foobar;id=1" --param-del=";" -f --banner --dbs --users
```





# HTTP参数注入与修改

## http cookie头

--cookie:

用于两个方面：

1.web应用需要登陆的时候

2.进行cookie注入，当--level 2或2以上时，sqlmap会尝试cookie注入。



## http user-agent头

--user-agent:

1.默认情况下sqlmap的http请求头中user-agent值是：

```javascript
sqlmap/1.0-dev-xxxxxxx (http://sqlmap.org)
```

可以使用--user-agent参数来修改，同时也可以使用--random-agent参数来随机的从./txt/user-agent.txt中获取。

2.当leve参数设定为3时，会尝试对User-Angent进行注入。



## http referer头

--referer

sqlmap可以在请求中伪造http中的referer，

当--level参数设定为3或者以上 时，会尝试对referer注入。



## http 额外的头

--headers

可以通过该参数来增加额外的http头。



## 避免过多的错误请求被屏蔽

参数：--safe-url，--safe-freq

有的web应用程序会在你多次访问错误的请求时屏蔽掉你以后的所有请求，这样在sqlmap进行探测或者注入的时候可能造成错误请求而触发这个策略，导致以后无法进行。

绕过策略：

```javascript
1、--safe-url：提供一个安全不错误的连接，每隔一段时间都会去访问一下。
2、--safe-freq：提供一个安全不错误的连接，每次测试请求之后都会再访问一边安全连接。
```



每次请求时候执行自定义的python代码

参数：--eval

在有些时候，需要根据某个参数的变化，而修改另个一参数，才能形成正常的请求，这时可以用--eval参数在每次请求时根据所写python代码做完修改后请求。

例子：

```javascript
python sqlmap.py -u "http://www.target.com/vuln.php?
id=1&hash=c4ca4238a0b923820dcc509a6f75849b" 
--eval="import hashlib;hash=hashlib.md5(id).hexdigest()"
```

上面的请求就是每次请求时根据id参数值，做一次md5后作为hash参数的值。











