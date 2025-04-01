# True XML cookbook
## 考察知识点：
### 1.xxe
### 2.内网探测

#### 1.题目提示xml，想到xxe

#### 2.构造xxe

![image](images/3D67B0179ACB4C47A25B04425A1E5233True%20XML%20cookbook1.png)

#### 3.读一些关键文件

如/etc.hosts,/proc/net/arp

![image](images/417A744A37D74E8B8A1373F45B0900FFTrue%20XML%20cookbook2.png)

#### 4.利用xxe依次探测，内网ip

在访问192.168.1.8时，得到flag

![image](images/B2F46BDEADE34550A9382AD8868DF5AFTrue%20XML%20cookbook3.png)