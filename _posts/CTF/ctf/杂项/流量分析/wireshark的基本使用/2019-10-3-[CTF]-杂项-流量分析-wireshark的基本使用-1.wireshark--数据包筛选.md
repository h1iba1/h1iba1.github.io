wireshark 的基本使用方法分为数据包筛选，数据包搜索，数据包还原，数据提取四个部分。



# 1.数据包筛选



# 1.1筛选ip，源IP筛选

```javascript
ip.src==ip地址
```



例如：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/ADA67BCF7ABF47DF9492731084F55141clipboard.png)

# 或者手动操作：

点击任意一个合适的ip右键选中-->作为过滤器应用-->选中

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/2715DFC2C40F4A94A90BB851BBAC1DEAclipboard.png)



# 1.2 目的ip筛选

```javascript
ip.dst==ip地址
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/杂项/流量分析/wireshark的基本使用/images/8B8F88BE6AF2432CB9404A4A2E360572clipboard.png)



目的ip的筛选也可以：右键选中-->作为过滤器应用-->选中



其他的筛选语法：

## mac地址的筛选：

```javascript
   eth.dst ==A0:00:00:04:C5:84 筛选目标mac地址

   eth.addr==A0:00:00:04:C5:84 筛选MAC地址
```



## 端口筛选：

```javascript
   tcp.dstport == 80  筛选tcp协议的目标端口为80的流量包

   tcp.srcport == 80  筛选tcp协议的源端口为80的流量包

   udp.srcport == 80  筛选udp协议的源端口为80的流量包
```



## 包长度筛选：

```javascript
    udp.length ==20   筛选长度为20的udp流量包

    tcp.len >=20  筛选长度大于20的tcp流量包

    ip.len ==20  筛选长度为20的IP流量包

    frame.len ==20 筛选长度为20的整个流量包
```



## http请求的筛选：

```javascript
请求方法为GET：http.request.method==“GET”        筛选HTTP请求方法为GET的 流量包

请求方法为POST：http.request.method==“POST”      筛选HTTP请求方法为POST的流量包

指定URI：http.request.uri==“/img/logo-edu.gif”  筛选HTTP请求的URL为/img/logo-edu.gif的流量包

请求或相应中包含特定内容：http contains “FLAG”    筛选HTTP内容为/FLAG的流量包
```



