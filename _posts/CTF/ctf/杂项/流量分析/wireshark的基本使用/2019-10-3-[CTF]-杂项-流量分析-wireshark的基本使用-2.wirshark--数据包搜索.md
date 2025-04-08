# 数据包搜索

## 在wireshark界面按ctrl+f，可以进行关键字的搜索：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/A866EE10176E4D1887F67EBB2676BEC8clipboard.png)



wireshark的搜索功能支持表达式，字符串，十六进制等方式进行搜索，通常情况下直接使用字符串方式进行搜索。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/DC61303EF3EA4822B23C4D0A375D2983clipboard.png)



搜索栏的左边下拉，有分组列表，分组详情，分组字节流三个选项，分别对应wireshark界面的三个部分，搜索时选择不同的选项以指定搜索区域：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/54CC0F2E7B0846E4BFD62907FF50D5C0clipboard.png)



## 搜索语法：

搜索指定协议数据包中的内容：http contains "flag"



搜索post请求：http.request.method==post





## 各分组模块介绍：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/1DF7F83F23634B439263A90D911F1B11clipboard.png)





















