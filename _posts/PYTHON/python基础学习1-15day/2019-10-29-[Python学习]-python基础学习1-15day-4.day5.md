

```javascript
# coding=utf-8
from random import randint

###########################################
# test1:水仙花数
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    height = num // 100
    if (low * low * low + mid * mid * mid + height * height * height == num):
        print(num)

# test2:数字反转
num = int(input('输入需要反转的数字：'))
reversed_num = 0
while num > 0:
    # num%10 取最后一位
    # num 不断//10缩小
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)

# test3:百钱百鸡
# 100块钱最多20只公鸡，33只母鸡，300只小鸡
# 循环20以内，33以内+小鸡数量=100
for i in range(0, 20):
    for j in range(0, 33):
        if (i * 5 + j * 3 + (100 - i - j) / 3 == 100):
            print("公鸡%d只，母鸡%d只，小鸡%d只", (i, j, 100 - i - j))

# test4:craps 赌博游戏
# 玩家第一次摇出了7，11点玩家胜，摇出2，3，12点庄家胜
# 其他点数玩家继续摇骰，摇出7点庄家胜，摇出和前次一样的点数玩家胜，否则继续摇骰
# money = 1000
# while money > 0:
#     print('你的资产为：', money)
#     needs_go_on = False
#
#     # 可以循环下注，保证下注在资产范围内
#     while True:
#         debt = int(input('请下注：'))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜！')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜')
#         money -= debt
#     else:
#         needs_go_on = True
#     #     控制必须进入下一回合才能进入这个循环
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点', current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了，游戏结束')

# test4斐波那契数列
first = 1
second = 1
num = 1
print(first, end='\t')
print(second, end='\t')
for i in range(0, 20):
    num = first + second
    first = second
    second = num
    print(num, end='\t')
print()
# test5
is_prime_number=False
for x in range(3, 101):
    for y in range(2, x):
        if x % y == 0:
            is_prime_number=False
            continue
        else:
            is_prime_number=True
    if is_prime_number:
        print(x,end='\t')

```

