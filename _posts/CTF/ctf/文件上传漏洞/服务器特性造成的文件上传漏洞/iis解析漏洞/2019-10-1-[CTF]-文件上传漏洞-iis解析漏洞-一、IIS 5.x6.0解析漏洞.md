一、IIS 5.x/6.0解析漏洞

---

IIS 6.0解析利用方法有两种

1.目录解析

/xx.asp/xx.jpg


2.文件解析

wooyun.asp;.jpg 


第一种，在网站下建立文件夹的名字为 .asp、.asa 的文件夹，其目录内的任何扩展名的文件都被IIS当作asp文件来解析并执行。

例如创建目录 wooyun.asp，那么

/wooyun.asp/1.jpg


将被当作asp文件来执行。假设黑阔可以控制上传文件夹路径,就可以不管你上传后你的图片改不改名都能拿shell了。

第二种，在IIS6.0下，分号后面的不被解析，也就是说

wooyun.asp;.jpg


会被服务器看成是wooyun.asp

还有IIS6.0 默认的可执行文件除了asp还包含这三种

/wooyun.asa
/wooyun.cer
/wooyun.cdx