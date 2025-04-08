配置问题导致漏洞

1、如果在 Apache 的 conf 里有这样一行配置 AddHandler php5-script .php 这时只要文件名里包含 .php  即使文件名是 test2.php.jpg 也会以 php 来执行。

2、如果在 Apache 的 conf 里有这样一行配置 AddType application/x-httpd-php .jpg即使扩展名是 jpg，一样能以 php 方式执行。

修复方案

1、apache 配置文件，禁止 .php. 这样的文件执行，配置文件里面加入

```javascript
<Files~“.(php.|php3.)”>
      Order Allow,Deny
      Deny from all
</Files>
```

2、用伪静态能解决这个问题，重写类似.php.*这类文件，打开 apache 的 httpd.conf 找到 

LoadModule rewrite_module modules/mod_rewrite.so

把 # 号去掉，重启 apache, 在网站根目录下建立 .htaccess 文件,代码如下:

```javascript
<IfModulemod_rewrite.c>
RewriteEngine On
RewriteRule .(php.|php3.) /index.php
RewriteRule .(pHp.|pHp3.) /index.php
RewriteRule .(phP.|phP3.) /index.php
RewriteRule .(Php.|Php3.) /index.php
RewriteRule .(PHp.|PHp3.) /index.php
RewriteRule .(PhP.|PhP3.) /index.php
RewriteRule .(pHP.|pHP3.) /index.php
RewriteRule .(PHP.|PHP3.) /index.php
</IfModule>
```



实验不理想可能和浏览器，apache版本关系。