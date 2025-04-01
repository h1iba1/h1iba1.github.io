

![](images/619C9045B9CD444692FC613FFDC5197A93ffdda9-7931-4753-aee3-0c05df7bc9b5.bmp)



图片文字提示：转成埃塞克码，其实就是ascii码....

# 1.把图片中的数字提取出来。



# 2. 有提示是八进制



# 3.一个数为一组从八进制转成十进制太小，尝试两个数一组，也是乱码，当三个数为一组时，得到有意义的明文



```python
exp.py
import binascii

import libnum

# 11111 4157 16614 5123 14514 3165 16215 1164 17112 6145 16217 1115 16514 3150

value='111114157166145123145143165162151164171126145162171115165143150'
length=len(value)
print(length)

arr=[]
for i in range(length//3):
    arr.append(int(value[i*3:i*3+3],8))

flag=""
for i in range(len(arr)):
    flag+=chr(arr[i])


print("flag{"+flag+"}")

```





