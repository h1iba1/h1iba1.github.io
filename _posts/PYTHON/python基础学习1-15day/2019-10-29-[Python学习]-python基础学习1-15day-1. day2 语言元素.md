运算符

Python支持多种运算符，下表大致按照优先级从高到低的顺序列出了所有的运算符，运算符的优先级指的是多个运算符同时出现时，先做什么运算然后再做什么运算。除了我们之前已经用过的赋值运算符和算术运算符，我们稍后会陆续讲到其他运算符的使用。

| 运算符 | 描述 |
| - | - |
| [] [:] | 下标，切片 |
| \*\* | 指数 |
| ~ + - | 按位取反, 正负号 |
| \* / % // | 乘，除，模，整除 |
| + - | 加，减 |
| &gt;&gt; &lt;&lt; | 右移，左移 |
| &amp; | 按位与 |
| ^ | | 按位异或，按位或 |
| &lt;= &lt; &gt; &gt;= | 小于等于，小于，大于，大于等于 |
| == != | 等于，不等于 |
| is is not | 身份运算符 |
| in not in | 成员运算符 |
| not or and | 逻辑运算符 |
| = += -= \*= /= %= //= \*\*= &amp;= ` | = ^= &gt;&gt;= &lt;&lt;=` |


说明： 在实际开发中，如果搞不清楚运算符的优先级，可以使用括号来确保运算的执行顺序。

```javascript
# coding=utf-8
import math

a = 100
b = 12.345
c = 1 + 5j
d = 'hello , world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

########################################################
# 从键盘输入两个数来实现对两个整数的运算
# 字符串中的特定位置需要用输出结果来替换的话，需要使用%来连接，不能使用,
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %d' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

#############################################################
# 运算符
a = 10
b = 3
a += b
a *= a + 2  # a=a*(a+2)
print(a)

##########################################################
# 华氏温度转换为摄氏温度
f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print ('%.1f 华氏度=%.1f摄氏度' % (f, c))

# 输入圆的半径计算计算周长和面积
radius = float(input('请输入圆的半径：'))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print ('周长：%.2f' % perimeter)
print ('面积 : %.2f' % area)

# 判断闰年
year = int(input('请输入年份：'))
is_leap = (year % 4 and year % 100 != 0) or \
          year % 400 == 0
print (is_leap)
```

