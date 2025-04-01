

```javascript
# 获取用户输入十进制数
dec = int(input("输入数字："))
 
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))
```



```javascript
16进制转10进制: int('0x10', 16)  ==>  16
```



16进制转字符串：

```javascript
binascii.a2b_hex(【16进制字符串】).decode("utf8")
```

