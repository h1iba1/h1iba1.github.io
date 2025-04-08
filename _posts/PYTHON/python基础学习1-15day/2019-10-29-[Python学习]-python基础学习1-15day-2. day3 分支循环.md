```python
循环分支：
if ...else...不需要使用括号，使用缩进来控制执行
if...else...可以嵌套
elif=else if

```



```javascript
# coding=utf-8

#####################################
# 用户身份验证
username = input('请输入用户名: ')
password = input('请输入密码: ')

if username == 'admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败')

######################################################
#         3x - 5  (x > 1)
# f(x) =  x + 2   (-1 <= x <= 1)
#         5x + 3  (x < -1)

x = float(input('请输入x: '))
if x > 1:
    y = 3 * x - 5
elif x < -1:
    y = x + 2
else:
    y = 5 * x + 3
print(y)

################################################################
# 嵌套写法
x = float(input('请输入x: '))
if x > 1:
    y = 3 * x - 5
else:
    if x < -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(y)

##################################################################
# test1:百分制程序转换为等级制程序
score = float(input('请输入成绩： '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'c'
elif score >= 60:
    grade = 'D'
else:
    grade='E'
print('对应的等级为：', grade)

####################################################################
# 英制单位英寸与公制单位厘米互换
value = float(input('请输入长度'))
unit = input('请输入单位')
if unit == 'in' or unit == '英寸':
    print('%f英寸=%f厘米' % (value, value * 2.54))
elif unit == 'CM' or unit == '厘米':
    print('%f厘米=%f英寸' % (value, value / 2.54))
else:
    print('请输入有效单位')

####################################################################
# 输入三条变，如果能构成三角形就计算周长和面积
a = float(input('请输入边长a: '))
b = float(input('请输入边长b: '))
c = float(input('请输入边长c: '))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    # %f float型
    print("周长为: %f", perimeter)
    p = (a + b + c) / 2
    # **指数 这里为根号2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("面积为：%f", area)
else:
    print("不能构成面积")
```

