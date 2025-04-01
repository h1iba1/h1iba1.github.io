上传测试发现php，php3，.htaccess等都不能上。上传一个不存在的文件名.heibai

![](images/6C975E77841847E1A2B5295ED1F42752clipboard.png)

emmmmmmmm，还是黑名单限制。

尝试 空格，::$DATA，.后缀发现均不能上传。查看tips，发现过滤了好多的后缀，对::$DATA等也做了过滤。

![](images/05FA089B294B47BAA5D72BF4E7AB8DD8clipboard.png)

但是发现黑名单限制不完整，上传phpinfo.phP，上传成功。

访问phpinfo.phP文件。

![](images/14A8C096EC0F45EC993A5A598043F3F9clipboard.png)

