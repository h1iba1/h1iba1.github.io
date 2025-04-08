

queue队列，很好的解决了生产者消费者问题

```javascript
import threading
import queue
import os
import sys

# 继承线程
class CheckPing(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    # 重构run函数
    def run(self):
        # 如果队列不为空
        while not self._queue.empty():
            # print(self._queue.get())
            # 取出队列里面的值，并将索引向下移动
            ip=str(self._queue.get())

            # print(ip)
            # 执行系统命令
            result=os.popen('ping '+ip)

            if "TTL" in result.read():
                sys.stdout.write(ip+'\n')



def main():
    # 线程池
    threads = []
    # 线程数
    thread_count = 10
    # 队列池
    queues = queue.Queue()

    # 初始化ip
    for i in range(1, 256):
        queues.put('112.45.120.'+str(i))

    # 创建的线程入队
    for i in range(thread_count):
        threads.append(CheckPing(queues))

    # 启动线程
    for i in threads:
        i.start()

    # 销毁线程
    for i in threads:
        i.join()


if __name__ == '__main__':
    main()
```

