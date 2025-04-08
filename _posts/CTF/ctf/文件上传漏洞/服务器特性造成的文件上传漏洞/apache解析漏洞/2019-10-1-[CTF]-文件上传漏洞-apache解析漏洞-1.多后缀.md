# 1.多后缀

### 原理：

在apache1.x和2.x中。文件解析规则是从右到左，如果文件名为不可识别文件，则再往左解析。



例如：

1.php.rar.rar.rar

apache无法解析rar，一直往左判断，直到遇到可解析的php，开始执行。



### 漏洞作用：

文件上传中可构造1.php.jpg来绕过文件名限制。



### 漏洞存在版本：

- Apache 2.0.x <= 2.0.59

- Apache 2.2.x <= 2.2.17

- Apache 2.2.2 <= 2.2.8



### apache服务器版本查看命令行：

httpd -v；

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/服务器特性造成的文件上传漏洞/apache解析漏洞/images/90A32FCD06CA45B9A48DA84C88F78FF2clipboard.png)



### apache能够认识的文件放在mime.types文件里：

文件路径：D:\phpstudy\phpstudy2018\PHPTutorial\Apache\conf\mime.types

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/服务器特性造成的文件上传漏洞/apache解析漏洞/images/5752F706E60E456A9422F94F342356E0clipboard.png)



由于本人的apache版本为2.4.37无法触发该漏洞。所以暂时不做测试。







