

```javascript
# coding=utf-8
import random

###############################
# for-in循环
sum = 0
# range范围 如果执行到100，要写成range(101)
for x in range(101):
    sum += x
print(sum)

#########################################################
# range()作用
# range(101) 可以产生0到100的整数序列
# range(1,100) 可以产生1到99的整数序列
# range(1,100,2) 可以产生一个1到99的奇数序列，其中2是增量
# 求1~100之间的偶数和
sum = 0
for x in range(0, 100, 2):
    sum += x
print(sum)

###########################################################
# 使用分支结构来实现相同的功能
sum = 0
for x in range(1, 100):
    if x % 2 == 0:
        sum += x
print(sum)

################################################################
# while
# counter = 0
# answer = random.randint(1, 100)
# while True:
#     counter += 1
#     number = int(input('请猜测生成的数字：'))
#     print(answer)
#     if number < answer:
#         print("猜小了")
#     elif number > answer:
#         print("猜大了")
#     else:
#         print("恭喜你回答正确")
#         break;
# print("你总共猜了%d次" % counter)
# if counter > 7:
#     print("脑残吧，猜了这么久")

##################################################################
# 输出99乘法表
for i in range(1, 10):
    for j in range(i + 1):
        print('%d*%d=%d' % (i, j, i * j), end='\t')
    print()

################################################################
# test1 输入一个数判断是不是素数
number = int(input('请随机输入一个数'))
for x in range(2, number):
    if number % x == 0:
        is_prime = False
        break;
    else:
        is_prime = True

# 必须要用一个值来接收判断
if is_prime:
    print("是素数")
else:
    print("不是素数")
###############################################################
# test2 输入两个正整数，计算他们的最大公约数和最小公倍数
number1 = int(input('请输入第一个正整数：'))
number2 = int(input('请输入第二个正整数：'))

# 最大公约数
# python 三目运算符：true是返回numbere1，否则返回number
number3 = number1 if (number1 < number2) else number2
maxNumber = 0
for x in range(1, number3 + 1):
    if (number1 % x == 0 and number2 % x == 0):
        maxNumber1 = x
    maxNumber = maxNumber1 if (maxNumber1 > maxNumber) else maxNumber
print("最大公约数为：", maxNumber)
print("最小公倍数：", number1 * number2)

# 更简单的实现方式
number1 = int(input('请输入第一个正整数：'))
number2 = int(input('请输入第二个正整数：'))

number3 = number1 if (number1 < number2) else number2
# 从最小的数做递减循环
for x in range(number3, 0, -1):
    if number1 % x == 0 and number2 % x == 0:
        print("%d和%d的最大公约数为：%d" % (number1, number2, x))
        print("%d和%d的最小公倍数为：%d" % (number1, number2, number1 * number2))
        break;

######################################################################################
# 打印三角形图案

row = int(input("请输入行数："))
# 循环输出三行
for i in range(row):
    # 在每行循环输出一个*
    for _ in range(i + 1):
        print('*', end='')
    print()

for i in range(row):
    for j in range(row):
        # 如果是第0行就填空格，知道最后一个填*
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
```

