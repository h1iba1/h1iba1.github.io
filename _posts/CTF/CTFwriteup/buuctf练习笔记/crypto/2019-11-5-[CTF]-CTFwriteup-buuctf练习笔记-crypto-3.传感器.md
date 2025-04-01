参考链接：

https://www.xmsec.cc/manchester-encode/

https://skysec.top/2017/07/10/%E6%9B%BC%E5%88%87%E6%96%AF%E7%89%B9%E4%B8%8E%E5%B7%AE%E5%88%86%E6%9B%BC%E5%88%87%E6%96%AF%E7%89%B9/#%E7%AC%AC%E4%B9%9D%E5%B1%8A%E5%85%A8%E5%9B%BD%E5%A4%A7%E5%AD%A6%E7%94%9F%E7%AB%9E%E8%B5%9B-%E2%80%94%E2%80%94%E2%80%94-%E4%BC%A0%E6%84%9F%E5%99%A81



Wiki

曼彻斯特编码（Manchester Encoding），也叫做相位编码（ Phase Encode，简写PE），是一个同步时钟编码技术，被物理层使用来编码一个同步位流的时钟和数据。它在以太网媒介系统中的应用属于数据通信中的两种位同步方法里的自同步法（另一种是外同步法），即接收方利用包含有同步信号的特殊编码从信号自身提取同步信号来锁定自己的时钟脉冲频率，达到同步目的。

Encode and Decode

IEEE 802.4（令牌总线）和低速版的IEEE 802.3（以太网）中规定, 按照这样的说法, 01电平跳变表示1, 10的电平跳变表示0。

Ideas

5555555595555A65556AA696AA6666666955转为二进制，根据01->1,10->0。可得到

0101->11

0110->10

1010->00

1001->01

decode得到

11111111 11111111 01111111 11001011 11111000 00100110 00001010 10101010 10011111

bin->hex，对比ID并不重合，根据八位倒序传输协议将二进制每八位reverse，转hex即可



```javascript
char = "5555555595555A65556AA696AA6666666955"
result = char.replace("5","0101").replace("6","0110").replace("9","1001").replace("A","1010")
num = len(result)
print result

flag = ""
flag_final = ""
# 一次读取字符串的两个字符
for i in range(0,num,2):
    if result[i:i+2] == "01" :
        flag += "1"
    if result[i:i+2] == "10" :
        flag += "0"

print flag

for j in range(0,len(flag),8):
    flag_final += hex(int(flag[j:j+8][::-1],2))[2:]
print flag_final.upper()
```



flag：FFFFFED31F645055F9