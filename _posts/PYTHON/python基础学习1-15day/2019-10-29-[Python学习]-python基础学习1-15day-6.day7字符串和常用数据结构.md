```python
# coding=utf-8
# python中',",''' '''' 包围起来的符号均为字串
s1 = 'hello,world'
s2 = "hello,world"
s3 = """
hello,
world!
"""

print(s1, s2, s3)  # hello,world hello,world

# 转义字符\
s1 = '\'hello,world!\''
s2 = '\n\\hello,world!\\\n'

print(s1, s2, end=' ')

# 还可以在\后面跟上一个八进制或者十六进制表示字符
# 也可以跟上unicode字符编码来表示字符
s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
# 'hello,world!'
# \hello,world!\

# 可以通过在字符串前面加上r来让字符串\不转义
s1 = r'\'hello,world!\''  # \'hello,world!\'
s2 = r'\n\\hello,world!\\\n'  # \n\\hello,world!\\\n
print(s1, s2, end='')

# python运算符：
# + 实现字符串的拼接
# * 重复一个字符串的内容
# [][:]
s1 = 'hello' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('11' in s1)
print('good' in s1)
str2='abc123456'

# 从字符串中取出指定位置的字符（下标运算）
print(str2[2]) #c
# 字符串切片（从指定的开始索引到指定的结束索引）
print(str2[2:5]) #c12
print(str2[2:]) #c123456
print(str2[2::2]) #c246 间隔为2
print(str2[::2]) #ac246 取偶数位
print(str2[::-1]) #倒序输出
print(str2[-3:-1]) #45

##########################################################
# 其他一系列字符串处理方法
str1='hello,world'
#通过内置函数len计算字符串长度
print(len(str1)) #11

# 获得字符串每个单词首字母大写的拷贝
print(str1.title()) #Hello,World

# 从字符串中查找字串所在位置
print(str1.find('or')) #7
print(str1.find('shit')) #-1

# 与find类似但找不到字串是会引发异常
print(str1.index('or')) # 7
# print(str1.index('shit'))

# 检查字符串是否以指定的字符串开头
print(str1.startswith('He')) # False
print(str1.startswith('he1')) # False

# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!')) # False

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(20,'*')) # *********hello,world*********

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(20,' ')) #                hello,world

str2='abc123456'
# 检查字符串是否有数字构成
print(str2.isdigit()) # False

# 检查字符串是否以数字和字母构成
print(str2.isalnum()) #True

str3='  1406249263@qq.com   '
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip()) #1406249263@qq.com

# 再有列表的情况下，为什么还要创造元组,元组的值不可更改，是线程安全的
# 并且元组在创建时间和占用的空间上都优于列表
# 在不需要对元素进行，添加，修改，删除时，可以考虑元组

# 集合
# python中的集合和数学上的集合是一致的
# 不允许元素重复，可以交集，并集，差集，运算
# 创建集合的字面量语法
set1={1,2,3,3,3,2}
print(set1) #{1,2,3},排除了重复的元素
print('Length=',len(set1))

# 创建集合的构造器语法
set2=set(range(1,10))
set3=set((1,2,3,3,2,1))
print(set2,set3)
# 创建集合的推导语法（推到式也可以用于推导集合）
set4={num for num in range(1,100) if num%3 == 0 or num%5==0}
print(set4)

# 向集合中添加元素和删除元素
set1.add(4)# 增
set1.add(5)
set2.update([11,12])#改
set2.discard(5)#删
if 4 in set2:
    set2.remove(4)#删
print(set1,set2)
print(set1,set2)
print(set3.pop())#弹出原本输出的
print(set3)

# 集合交集，并集，差集，对称差运算
print(set1,set2)
print(set1 & set2)#交集
print(set1 | set2)# 并集
print(set1-set2)#差集
print(set1^set2)# 对称差
print(set2<=set1)
print(set3<=set1)

# 字典
scores={'驼昊':95,'白元芳':78,'狄仁杰':82}
print(scores)
# 创建字典的构造器语法
items1=dict(one=1,two=2,three=3,four=4)
print(items1)
# 通过zip函数将两个序列压成字典
items2=dict(zip(['a','b','c'],'123'))
print(items2)
# 创建字典的推导式语法
items3={num:num ** 2 for num in range(1,10)}
print(items1,items2,items3)
# 通过键可以获取字典中对应的值
print(scores['驼昊'])
print(scores['狄仁杰'])
# 对字典中的所有值进行遍历
for key in scores:
    print(f'{key}:{scores[key]}')

# 更新字典的元素
scores['白元芳']=65
scores['诸葛王朗']=71
scores.update(冷面=67,方启鹤=85)
print(scores)

if '武则天' in scores:
    print(scores['武则天'])

# get方法获取对应的值
print(scores.get('武则天',60))

# 删除字典中的元素
print(scores.popitem())
print(scores.pop('驼昊',100))

# 清空字典
scores.clear()
print(scores)

##########practice:##################

# coding=utf-8
# 需要在终端中执行

# test1在屏幕上显示跑马灯文字
import os
import time
import random


def main():
    content = '123456'
    while True:
        os.system('cls')  # os.system('clear')
        # 清理屏幕的输出
        print(content)
        #         休眠0.2秒
        time.sleep(0.2)
        content = content[1:] + content[0]


# test2 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

def generate_code(code_len=4):
    """

    :param code_len:验证码的长度（默认四个字符）
    :return:由大小写英文字母和数字构成的随机验证码
    """
    all_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos=len(all_chars)-1
    code=''
    for _ in range(code_len):
        index=random.randint(0,last_pos)
        code+=all_chars[index]
    return code

# 设计一个函数，返回给定文件的后缀名

def get_suffix(filename,has_dot=False):
    """

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件后缀名
    """
    pos=filename.rfind('.')
    # 如果后缀名为空，返回空
    if 0 <pos <len(filename) -1:

        # 如果false index=pos
        index=pos if has_dot else pos+1
        # 返回index后的字符串，这里相当于字符串切片
        return filename[index:]
    else:
        return ''



if __name__ == '__main__':
    # main()
    print(generate_code())
    print(get_suffix('index.php'))

```