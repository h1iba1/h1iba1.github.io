python的os模块提供了frok()函数来操作进程。但是windows系统没有提供frok()函数。

但是windows系统可以使用multiprocessing模块的process类来创建子进程。

而且该模块还提供了更高级的封装，例如批量启动进程的进程池（Pool）、用于进程间通信的队列（Queue）和管道（Pipe）等



# 1. 使用进程和不使用进程的对比

不使用进程：

```javascript
from random import randint
from time import time,sleep

def download_task(filename):
    print('开始下载 %s ....' % filename)
    download_time=randint(1,3)
    sleep(download_time)
    print('下载完成，耗时 %d 秒' % download_time)

def main():
    start=time()
    download_task('python从入门到入土')
    download_task('av.avi')
    end=time()
    print('总共耗时%.2f秒' % (end-start))

if __name__ == '__main__':
    main()
    
开始下载 python从入门到入土 ....
下载完成，耗时 1 秒
开始下载 av.avi ....
下载完成，耗时 2 秒
总共耗时3.03秒
```

使用进程：

```javascript
from multiprocessing import Process
from os import getpid

from random import randint
from time import time, sleep


def download_task(filename):
    print('启动下载进程，进程号：[%d]' % getpid())
    print('开始下载 %s ....' % filename)
    download_time = randint(1, 3)
    sleep(download_time)
    print('下载完成，耗时 %d 秒' % download_time)


def main():
    start = time()

    # args参数后面还有,(逗号)，应该是为了接收 多个参数
    p1 = Process(target=download_task, args=('python从入门到入土',))
    p1.start()
    p2 = Process(target=download_task, args=('av.avi',))
    p2.start()
    p1.join()
    p2.join()

    end = time()
    print('总共耗时%.2f秒' % (end - start))


if __name__ == '__main__':
    main()
    
启动下载进程，进程号：[15720]
开始下载 av.avi ....
启动下载进程，进程号：[13744]
开始下载 python从入门到入土 ....
下载完成，耗时 1 秒下载完成，耗时 1 秒

总共耗时1.08秒
```



使用进程之后，程序不在是依次执行，而是变成了并发执行



# 2.创建多进程的步骤

```javascript
1.导入multiprocessing模块
import multiprocessing
2.创建进程
p=Process(target=函数名(),args=('参数1','参数2',))
#参数后面还要加一个,
3.启动进程
p.start()
4.终止线程
p.join()
```



# 3.创建线程

python可以使用threading模块来创建线程，该模块对多线程编程提供了很好的面向对象封装。

```javascript
1. 导入threading模块
import threading
2. 继承线程类
class Dom(thread):
    def __init__(self,per):
        super().__init__()
        self.per=per

3. 创建线程
t=Dom(per)
4.启动线程
t.start()
5. 终止线程
t.join()

6. 批量创建线程：
threads=[]
for _ in range(100):
    t=Dom(per)
    threads.append(t)
    t.start()

7. 批量终止线程：
for t in threads:
    t.join()
```



4. 线程临界资源的访问

因为多个线程可以共享进程的内存空间，因此要实现多个线程间的通信相对简单，大家能想到的最直接的办法就是设置一个全局变量，多个线程共享这个全局变量即可。但是当多个线程共享同一个变量（我们通常称之为“资源”）的时候，很有可能产生不可控的结果从而导致程序失效甚至崩溃。如果一个资源被多个线程竞争使用，那么我们通常称之为“临界资源”，对“临界资源”的访问需要加上保护，否则资源会处于“混乱”的状态。下面的例子演示了100个线程向同一个银行账户转账（转入1元钱）的场景，在这个例子中，银行账户就是一个临界资源，在没有保护的情况下我们很有可能会得到错误的结果。

```javascript
from threading import Thread
from time import sleep


class Account(object):

    def __init__(self):
        self._balance = 0

    def display(self, money):
        new_balance=self._balance + money
        sleep(0.01)
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AddMoneyThred(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.display(self._money)


def main():
    account = Account()
    threads = []
    #     创建100个线程，向账户存钱
    for _ in range(0, 100):
        t = AddMoneyThred(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额 %d ' % account.balance)


if __name__ == '__main__':
    main()
```

结果：

```javascript
账户余额 2 
```

这个显然是不对的，因为多线程执行的时候，每个线程都同时进行了+1的操作，所以结果为2，而不是依次+1



解决这个问题的办法：

是提供“锁”来保护“临界资源”，只有获得“锁”的线程才能访问“临界资源”，而其他没有得到“锁”的线程只能被阻塞起来，直到获得“锁”的线程释放了“锁”，其他线程才有机会获得“锁”，进而访问被保护的“临界资源”

创建进程锁的办法：

```javascript
1.导入Lock函数
from threading import Lock
2.获取锁
只有获得锁，才能访问锁后面的代码
Lock().acquire()
3.finally释放锁
释放操作一般放在finally后
Lock().release()
```



例子：

```javascript
from threading import Thread,Lock
from time import sleep


class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock=Lock()

    def display(self, money):
        # 获取锁才能访问后面代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 释放锁资源
            self._lock.release()


    @property
    def balance(self):
        return self._balance


class AddMoneyThred(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.display(self._money)


def main():
    account = Account()
    threads = []
    #     创建100个线程，向账户存钱
    for _ in range(0, 100):
        t = AddMoneyThred(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额 %d ' % account.balance)


if __name__ == '__main__':
    main()
    
# print : 余额 100
```

