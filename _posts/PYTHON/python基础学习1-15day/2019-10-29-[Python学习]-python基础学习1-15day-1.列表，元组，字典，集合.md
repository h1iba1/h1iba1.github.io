# 列表，元组，字典，集合的区别

列表：就是数组

元组：类似于数组，但是里面元素不可更改

字典：自定义键值对

集合：一个无序的不重合的元素序列，可自动去重



一些简单实列：

1.列表

```python
#数组在python里叫列表
#一些简单特性
print(['hi']*4)    #['hi', 'hi', 'hi', 'hi']
print(3 in [1,2,3])#元素是否在列表中 #true

#迭代
for x in [1,2,3]:
    print(x,end=" ") #1 2 3

#确定数组长度
print(len([1,2,3])) #3

#python 列表截取与拼接
L=['Google', 'Runoob', 'Taobao']
print(L[2])#输出第三个元素 #Taobo
print(L[-2])#输出从右边起，倒数第二个元素  #Runoob
print(L[1:])#输出第一个元素后面的元素 #['Runoob', 'Taobao']

print(L.append('taobo'))
print(L) #['Google', 'Runoob', 'Taobao', 'taobo']
```



2.元组

```python
#元组和列表类似
#不同点在于元组的元素不能更改
#元组的创建 很简单，只需要在括号中添加元素，或者不同括号也可以
tup1=('1','2','3')
print(tup1) #('1', '2', '3')
tup2='4','5','6'
print(tup2) #('4', '5', '6')

#元组不允许修改，但是可以对整个元组拼接和删除
del tup2
print(tup2) #已经删除了tup2，此时或报错NameError: name 'tup2' is not defined
```



3.字典

```python
d={'key1':1,2:3}
print(d[2]) #3
print(d) #{'key1': 1, 2: 3}
```



4.集合

```python
#集合：一个无序的不重复元素序列
#可以自动去重
parame={'value1','value2','value1'}
print(parame) #{'value2', 'value1'}
```

