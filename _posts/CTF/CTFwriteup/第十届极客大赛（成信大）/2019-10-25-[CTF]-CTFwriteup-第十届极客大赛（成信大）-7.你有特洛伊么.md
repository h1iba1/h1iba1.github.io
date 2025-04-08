# 你有特洛伊么
## 考察知识点：
### 1.文件上传
### 2.php可解析文件名（php3,phtml）
### 3.php脚本的另一种写法

### 1.上传测试，发现jpg,gif,php文件都无法上传，但是png图片可以

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/1100F0A791814AF5AF9C49D6AD7DB7E6你有特洛伊么1.png)

但是不知道上传路径，尝试upload/68.png,可以访问，那现在就确定了文件上传路径

### 2.构造木马
在图片数据中添加`<?php phpinfo();?>`

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/A04EB9C8E74D416E8F4D1B9AEEA8F934你有特洛伊么2.png)

发现检测到了<?。尝试php文件的另一种写法：

```
<script language='php'>
phpinfo();
</script>
```

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/A09FB82C121241BE9D828DC12EE98A26你有特洛伊么3.png)

上传成功。

### 3.解析上传的图片马

尝试文件后缀，发现php被限制，但是php1可以上传但是，68.php1无法解析

php3,php5等接被过滤，后尝试phtml，可以上传。

### 4.蚁剑连接上传的木马

在根目录找到flag

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/72202EA3418D416BB12939EAB23AA3AD你有特洛伊么4.png)