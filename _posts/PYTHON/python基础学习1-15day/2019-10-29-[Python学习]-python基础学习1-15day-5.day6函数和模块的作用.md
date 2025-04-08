def.py

```javascript
############################################
# coding=utf-8
# test1:x1+x2+x3+x4=8,求该方程有多少组正整数解
from random import randint

m = int(input('m= '))
n = int(input('n= '))
fm = 1
for num in range(1, m + 1):
    fm *= num
fn = 1
for num in range(1, n + 1):
    fn *= num
fmn = 1
for num in range(1, m - n + 1):
    fmn *= num
print(fm // fn // fmn)


# test1:函数
# 求阶乘
def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result


m = int(input('m= '))
n = int(input('n= '))
print(factorial(m) // factorial(n) // factorial(m - n))


#  test3:函数的参数
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
        return total


def add(a=0, b=0, c=0):
    return a + b + c


print(roll_dice())

# 摇三颗骰子
print(roll_dice(3))

# 不用刻意去写，但是也可以进行重载
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按参数顺序传递
print(add(c=100, a=900, b=80))


# 用模块管理函数
# python中没有重载函数这个概念，后面写的同名函数会覆盖前面写的同名函数
# 在多人协作的项目中无法保证，大家使用的变量名不冲突，引入了模块的概念
# python中每个文件就代表了一个模块
# import关键字导入指定的模块就可以区分到底要使用那个模块中的foo函数
# import有三种写法
# 1.import
# 2.from 模块（包） import 函数
# 3.from 模块 (包） as 对象（可以以对象.函数()的形式调用 模块中的函数）

#再导入一个模块时，模块除了定义了函数之外，还可能有可执行代码，那么python解释器在导入这些模块时
# 有可能执行这些代码，我们不希望如此，所以将可执行代码放在if 条件下
# 列如： if __name__ =='__main__'
def foo():
    pass


def bar():
    pass


if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
    
```



test.py

```javascript
# test1:求最大公约数和最小公倍数的函数
# 最大公约数
def gcd(x, y):
    # if x<y x=x,y=y else x=y,x=y.总之就是让x最小
    (x, y) = (x, y) if (x < y) else (y, x)
    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i


# 最大公倍数
def lmc(x, y):
    return x * y


print(gcd(5, 10))
print(lmc(5, 10))


# test2:实现判断一个数是不是回文数
# 输入的数==倒数即是回文数
def is_palindrome(num):
    temp = num
    total = 0
    # 每次%10获取temp的最后一位，最后一位*10相加将数到回来
    while temp > 0:
        total = total * 10 + temp % 10
        # 每次整出10，将数缩小
        temp //= 10
        # if到回来的数和原来的数相等则为true
    return total == num


palindrome = int(input('请输入需要判断的回文数：'))
print(palindrome, "是回文数吗？", is_palindrome(palindrome))


# test3:判断一个数是不是素数
def is_prime_number(num):
    for x in range(2, num):
        if num % x == 0:
            return False
            break
        else:
            return True


prime = int(input("请输入需要判断的素数："))
print(prime, "是素数吗？", is_prime_number(prime))


# 判断一个数是不是回文素数

def is_palidrome_prime(num):
    if is_prime_number(num) and is_palindrome(num):
        return True
    else:
        return False


palindrome_prime = int(input("请输入一个数判断是不是回文素数："))
print(palindrome_prime, "是回文素数吗？", is_palidrome_prime(palindrome_prime))


# 关于局部变量和全局变量的讨论
def foo():
    a=200
    print(a)


if __name__=='__main__':
    a=100
    foo()
    print(a)
# 上面的函数输出200，100，。。。
# 如果想让foo函数的内容影响a，可以使用关键字global

```

