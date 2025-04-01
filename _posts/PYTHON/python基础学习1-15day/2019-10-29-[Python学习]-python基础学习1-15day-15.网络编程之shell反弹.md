server.py



```javascript
from socket import socket,SOCK_STREAM,AF_INET
from datetime import datetime
from subprocess import Popen,PIPE
import os

def main():
    # 1.创建套接字对象，并指定使用哪种服务
    server=socket(family=AF_INET,type=SOCK_STREAM)

    # 2.绑定ip地址和端口
    # server.bind(('169.254.208.151',6789))
    server.bind(('127.0.0.1', 12345))

    # 3. 开启监听，监听客户端连接到服务器
    server.listen(512)

    while True:
        print('等待连接')
        client,addr=server.accept()
        print(str(addr)+'链接到了服务器')

        # 建立shell连接
        while True:
            data =client.recv(1024)
            # 接收到的客户端命令为bytes型，需解码为str
            data=bytes.decode(data)
            # print(data)

            if not data:
                break
            # cmd=Popen(['/bin/bash','-c',data],stdin=PIPE,stdout=PIPE)
            # os.popen函数执行传入的命令
            cmd=os.popen(data)
            # 回显数据为str，需转换为bytes型，作为send（）参数
            result=bytes(cmd.read(),encoding='utf-8')

            # send发送的数据为bytes型
            client.send(result)

        client.close()

if __name__ == '__main__':
    main()
```



client.py:

```javascript
from socket import socket

def main():
    # 1.创建套接字
    client=socket()

    # 2.连接到服务器
    client.connect(('127.0.0.1', 12345))

    while True:
        data=input('~:')
        # 将str转为bytes
        data=bytes(data,encoding='utf-8')
        if not data:
            break
        #     发送客户端输入的数据
        client.send(data)
        # 客户端接收到的数据
        data=client.recv(1024)
        # 将bytes型的数据转为str
        result=str(data,encoding='utf-8')
        if not result:
            break
        print(result)

    # 3.从服务器接收数据
    # print(client.recv(1024).decode('utf-8'))

    client.close()

if __name__ == '__main__':
    main()
```



需要特别注意字符类型的转换，str转bytes

参考链接：

https://blog.csdn.net/yatere/article/details/6606316