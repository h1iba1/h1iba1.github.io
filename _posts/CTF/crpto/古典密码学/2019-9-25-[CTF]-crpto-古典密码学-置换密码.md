

```javascript
# coding=utf-8
# python3.7

# ciphertext_tmp=input("输入明文：")
plaintext_tmp = "attack begins at five"
ciphertext=''
# secret_key=input("请输入密钥：")
secret_key = "cipher"

# 去除输入的空格
plaintext = plaintext_tmp.replace(" ", "")

# 密钥长度
len_sk = len(secret_key)

# 矩阵行数
line = int(len(plaintext) / len(secret_key))

# 定义矩阵
# 密钥长度作为列
# 二维数组，是[列，行]
# 3*2 表示3行2列
matrix = [[0 for i in range(len_sk)] for i in range(line)]
# print(matrix)

tmp1 = 0

# 循环给矩阵填数据
for i in range(line):
    for j in range(len_sk):
        if tmp1>len(plaintext):
            matrix[i][j] =0
        else:
            matrix[i][j] = plaintext[tmp1]
        tmp1 = tmp1 + 1

print(matrix)

secret_key_list = list(secret_key)
secret_key_tmp = list(secret_key)
secret_key_tmp.sort()
# print(secret_key)
# print(secret_key_list)
# print(secret_key_tmp)

matrix2 = [0 for i in range(len_sk)] 

# 得到了置换顺序
for i in range(len_sk):
    matrix2[i] = secret_key_list.index(secret_key_tmp[i])

print(matrix2)  # [0, 4, 3, 1, 2, 5]
# 得到置换后的数组

# 建一个新数组来接受，转换的值
matrix3 = [[0 for i in range(len_sk)] for i in range(line)]
for i in range(line):
    temp2 = 0
    for j in matrix2:
        matrix3[i][temp2] = matrix[i][j]
        temp2 = temp2 + 1

print(matrix3)

# 二维数组转字符串
for i in range(line):
    for j in range(len_sk):
        plaintext += matrix[i][j]
        tmp1 = tmp1 + 1

# attackbeginsatfiveattackbeginsatfive
print(plaintext)
```

