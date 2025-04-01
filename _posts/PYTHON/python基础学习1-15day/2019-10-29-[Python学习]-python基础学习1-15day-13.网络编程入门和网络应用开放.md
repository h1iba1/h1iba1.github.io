# 1. 基于http协议的网络资源访问

```javascript
import requests
from threading import Thread


class DowloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        # 切片获取url最后一个/后面的内容，以得到图片名
        filename = self.url[self.url.rfind('/') + 1:]
        # 获取图片内容，写入文件，获得图片
        resp = requests.get(self.url)
        with open(r'H:/pythonScript/study/day14/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    r = requests.get('http://api.tianapi.com/meinv/index?key=0821659b0274cff36cd67d9561ca50c8&num=10')
    data_model = r.json()
    # 依次取出data_model列表的数据
    for data in data_model['newslist']:
        # 获取图片url
        url = data['picUrl']
        DowloadHanlder(url).start()


if __name__ == '__main__':
    main()
```



# 2.基于传输层协议的套接字编程

通俗来说套接字就是一套用C语言写成的应用程序开发库，主要用于实现进程间通信和网络编程，在网络应用开发中被广泛使用



# python实现套接字编程服务器端创建的五个步骤：

```javascript
1.创建套接字对象，并指定使用哪种服务
   socket(fimaly=,type=)
 # family=AF_INET - IPv4地址
 # family=AF_INET6 - IPv6地址
 # type=SOCK_STREAM - TCP套接字
 # type=SOCK_DGRAM - UDP套接字

2.绑定ip地址和端口
 # 同一时间在同一个端口上只能绑定一个服务否则报错
server.bind(('127.0.0.1',12345))

3.开启监听，监听客户端链接到服务器
#参数512可以理解为连接队列的大小
server.listen(512)

4.通过循环接收客户端的链接，并做出相应的处理
while True:
    client,addr=server.accept()
    
    5.发送数据
    server.send(str(datetime.now()).encode('utf-8'))
    
    6.断开链接
    server.close()

```



server.py

```javascript
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime

def main():
    # 1.创建套接字对象，并指定使用哪种服务
    server=socket(family=AF_INET,type=SOCK_STREAM)

    # 2.绑定ip地址和端口
    # server.bind(('169.254.208.151',6789))
    server.bind(('127.0.0.1', 12345))

    # 3. 开启监听，监听客户端连接到服务器
    server.listen(512)

    while True:
        client,addr=server.accept()
        print(str(addr)+'链接到了服务器')

        client.send(str(datetime.now()).encode('utf-8'))

        client.close()

if __name__ == '__main__':
    main()
```



# 客户端创建的三个步骤：

```javascript
1.创建套接字对象默认使用IPv4和TCP协议
client=socket()

2.连接到服务器
client.connect(('127.0.0.1',12345))

3.从服务器接收数据
client.recv(1024).decode('utf-8')
```



client.py

```javascript
from socket import socket

def main():
    # 1.创建套接字
    client=socket()

    # 2.连接到服务器
    client.connect(('127.0.0.1', 12345))

    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))

    client.close()

if __name__ == '__main__':
    main()
```



实例：

server.py

```javascript
from socket import socket
from base64 import b64encode
from threading import Thread
from json import dumps


def main():
    # 自定义一个线程类
    class FileTransferHandler(Thread):

        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'gaogu.jpg'
            my_dict['filedata'] = data

            # 将字典处理成字符串
            json_str = dumps(my_dict)
            # 将字典的字符串数据，发送给连接者
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象
    server = socket()

    # 2.绑定ip地址
    server.bind(('127.0.0.1', 12345))

    # 3.监听服务器
    server.listen(512)

    print('服务器开启监听')
    with open('gaogu.jpg', 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')

    while True:
        client, addr = server.accept()

        # 开启一个单线程
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
```

client.py

```javascript
from socket import socket
from base64 import b64decode
from json import loads

def main():
    # 将收到的数据接收起来
    in_data=bytes()
    client=socket()
    client.connect(('127.0.0.1',12345))
    data=client.recv(1024)


    while data:
        in_data+=data
        data=client.recv(1024)

    my_dict=loads(in_data.decode('utf-8'))
    filename=my_dict['filename']
    filedata=my_dict['filedata'].encode('utf-8')

    with open('H:/pythonScript/study/day14/gaogu1.jpg','wb') as f:
        f.write(b64decode(filedata))

    print('图片以保持')

if __name__ == '__main__':
    main()
```



# 3. UDP套接字

UDP套接字和TCP套接字的差别就类似于一个是打电话一个是发短信



# 3.1 使用smtp协议发送邮件

```javascript
1. 导入smtp模块
from smtplib import SMTP

2.实例化smtp套接字对象
smtper=SMTP(smtp.qq.com)

3.登陆smtp服务器
smtper.login('210@qq.com',pass)

4.发送邮件
smtper.sendmail(sender,receivers,message.as_string())
```



# 3.2 使用qq邮箱发送邮件

## 1. 需要先开启qq邮箱的smtp服务

## 2. 获取授权码，以替代密码



```javascript
import smtplib
from email.header import Header
from email.mime.text import  MIMEText

def main():
    # 发送者
    sender='14063@qq.com'

    # qq邮箱授权码
    pwd='ryxiirc'

    # 邮件接收者
    receivers='210@qq.com'
    message=MIMEText('用python发送邮件的示例代码','plain','utf-8')

    # MIMEText三个主要参数
    # 1. 邮件内容
    # 2. MIME子类型，在此案例我们用plain表示text类型
    # 3. 邮件编码格式，一定要用"utf-8"编码，因为内容可能包含非英文字符，不用的可能收到的邮件是乱码
    message['From']=Header('王大锤','utf-8')
    message['To']=Header('驼号','utf-8')
    message['Subject']=Header('示例代码实验邮件','utf-8')

    # qq邮件的smtp服务器网址
    smtp_ser='smtp.qq.com'

    # 不能直接使用smtplib.SMTP来实例化，第三方邮箱会认为它是不安全的而报错
    # 使用加密过的SMTP_SSL来实例化，它负责让服务器做出具体操作，它有两个参数
    # 第一个是服务器地址，但它是bytes格式，所以需要编码
    # 第二个参数是服务器的接受访问端口，SMTP_SSL协议默认端口是465
    srv = smtplib.SMTP_SSL(smtp_ser.encode(), 465)

    # 使用授权码登陆邮箱
    srv.login(sender,pwd)

    # 使用sendmail方法来发送邮件，它有三个参数
    # 第一个是发送地址
    # 第二个是接受地址，是list格式，意在同时发送给多个邮箱
    # 第三个是发送内容，作为字符串发送
    srv.sendmail(sender,receivers,message.as_string())

    print('发送完成')

if __name__ == '__main__':
    main()

```



# 3.3 发送短信

