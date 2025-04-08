一、低版本nginx

nginx 0.5.x、nginx 0.6.x中可以通过在任意文件名后面增加%00.php解析为php

二、php-cgi漏洞

和IIS的第四点相同，在php配置文件中，开启了cgi.fix_pathinfo，导致图片马1.jpg可以通过访问1.jpg/.php解析成php