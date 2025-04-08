.htaccess

一般来说，配置文件的作用范围都是全局的，但 Apache 提供了一种很方便的、可作用于当前目录及其子目录的配置文件—— .htaccess（分布式配置文件）

要想使 .htaccess 文件生效，需要两个条件:

一是在 Apache 的配置文件中写上：

```javascript
AllowOverrideAll
```

若这样写则 .htaccess 不会生效：

```javascript
AllowOverrideNone
```

二是 Apache 要加载 mod_Rewrite 模块。加载该模块，需要在 Apache 的配置文件中写上：

```javascript
LoadModulerewrite_module/usr/lib/apache2/modules/mod_rewrite.so
```

若是在 Ubuntu 中，可能还需要执行命令：

```javascript
sudoa2enmod rewrite
```

配置完后需要重启 Apache。

.htaccess 文件可以配置很多事情，如是否开启站点的图片缓存、自定义错误页面、自定义默认文档、设置 WWW 域名重定向、设置网页重定向、设置图片防盗链和访问权限控制。但我们这里只关心 .htaccess 文件的一个作用—— MIME 类型修改。

如在 .htaccess 文件中写入：

```javascript
AddTypeapplication/x-httpd-phpxxx
```

就成功地使该 .htaccess 文件所在目录及其子目录中的后缀为 .xxx 的文件被 Apache 当做 php 文件。

另一种写法是：

```javascript
<FilesMatch"shell.jpg">
 SetHandlerapplication/x-httpd-php
</FilesMatch>
```

该语句会让 Apache 把 shell.jpg 文件当作 php 文件来解析。



