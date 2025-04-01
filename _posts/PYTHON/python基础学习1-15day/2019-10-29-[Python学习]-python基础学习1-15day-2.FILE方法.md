python中文件的读取方法

打开并读取文件：

```javascript
# 读取data.txt里面的内容
with open('data.txt', 'r') as f:
    data = f.read()
    print('context:{}'.format(data))
```



写入数据到文件中：

```javascript
with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)
```



遍历指定目录下的所有文件名:

```javascript
import os
entries = os.scandir()
with os.scandir('H:/pythonScript/study/FILE') as entries:
    for entry in entries:
        print(entry.name)
```



列出指定目录下的所有文件的子目录：

```javascript
basePath = 'H:/pythonScript'
print("目录")
with os.scandir(basePath) as entries:
    for entry in entries :
        if entry.is_dir():
            print(entry.name)
```

