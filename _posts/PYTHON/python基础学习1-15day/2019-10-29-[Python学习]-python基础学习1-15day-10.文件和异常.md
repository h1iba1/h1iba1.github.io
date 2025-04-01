# 1. 文件操作模式

r 读取

w 写 写入时，会清空之前的内容

x 当文件不存在使，产生异常

a 追加

b 二进制模式

t 文本模式

+ 既可以读又可以写



# 2. 读取文本文件

```javascript
def main():
    f=None
    try:
        f = open('致橡树.txt', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print("无法打开指定文件")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误")

    #     finally总是执行模块，就算调用了sys的exit函数，最后也会执行finally
    # 所以一般用来，释放资源
    finally:
        if f:
            f.close()



if __name__ == '__main__':
    main()
```



open()函数不指定文件操作模式时，默认为r



except 关键字执行异常。

文件不存在时产出fileNOtFoundError 异常。

没有指定编码，文件编码和系统不一样是，产生 LookuoError 异常。

读取文件时无法按照指定方式解码，会产生unicodeDecodeError异常



# 2. 写入文本文件

```javascript
from math import sqrt

# 判断素数的函数
def is_prime(n):
    assert n > 0
    # 2----》根号n
    for factor in range(2, int(sqrt(n)) + 1):
        # 然和一个数除以n为0，则不为素数
        if n % factor == 0:
            return False

    # 所有小于根号n的数除以n之后不为0，则为素数
    return True if n != 1 else False


def main():
    filenames = ['a.txt', 'b.txt', 'c.txt']
    fs_list = []

    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))

        for number in range(1, 9999):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')

    except IOError as ex:
        print(ex)
        print('写入错误')

    finally:
        for fs in fs_list:
            fs.close()

if __name__ == '__main__':
    main()
```



# 3. 读取二进制文件

```javascript
def main():

    try:
        with open('1.jpg', 'rb') as f1:
            data = f1.read()
            print(type(data))
            print(data)
            
        # 复制1.jpg文件
        with open('2.jpg', 'wb') as f2:
            f2.write(data)

    except FileNotFoundError:
        print('文件不存在')

    except IOError  as ex:
        print(ex)
        print('文件读取时出现错误')

    finally:
        f1.close()
        f2.close()

if __name__ == '__main__':
    main()
```



# 4. json模块

json模块有四个比较重要的模块：

- dump - 将Python对象按照JSON格式序列化到文件中

- dumps - 将Python对象处理成JSON格式的字符串

- load - 将文件中的JSON数据反序列化成对象

- loads - 将字符串的内容反序列化成Python对象



```javascript
import json

def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        #将字典数据json化
        with open('2.json', 'w') as fs:
            json.dump(mydict, fs)

        #将json数据，打印出来
        with open('2.json','r') as fs2:
            print(json.load(fs2))

    except IOError:
        print('写入出错')

    finally:
        fs.close()

if __name__ == '__main__':
    main()
```

