# 非对称加密。

alice给baobo一把锁（公钥）将数据（明文）加密，alice想查看明文，必须使用钥匙（私钥).



# 加密过程：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/DFDD7C3902114290A975C20681EA6EB1clipboard.png)

m的e次方与N取余得到c。



# 解密过程：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/A5F1BED3C5F546A3A375E6B259660DFAclipboard.png)

知道C,e,N却很难计算出m.



# 经过简单的数学推导：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/D2C3A91F24E14A3E8EFD37BA49920714clipboard.png)

## 一定存在一个整数d,使c得d次方与n取模得到m

## 此时：

## e和n组成公钥。

## d和n做成私钥。





# 难点：

如何由e算出d，





欧拉函数：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/FEAAA63DE28D43DE85AE868531746902clipboard.png)



得到e和d得关系：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/98E3DD5C8E6B4A0FBFEA146433730268clipboard.png)

k在此处的作用是为了使d为整数





# 实列：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/64CBDB82673E4014B6A51E92F8937B70clipboard.png)

N为两个素数53和59的乘积，为3127.

### alice 选取e=3，此时3和3127组成公钥（3，3127）



fai n计算出来为3016.



计算私钥，此时d等于2011

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/4DF3D4A94410403A9950B676EB4DB57Fclipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/6FFA83660ABB4AEEA91B583B627A9520clipboard.png)

### 所以此时私钥为（2011，3127）



## alice把私钥发给了baobo，此时鲍勃使用私钥对89加密得到C为1394

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/8808341971FB425CA70932C6400BF0A6clipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/CB4DE532FBED4789B5CB890737CEDE5Aclipboard.png)

alice收到密文之后可以对密文解密：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/EDA986C2B1734B5AB613E9FB055F38F2clipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/crpto/RSA/images/05AE22381F4849BDA9DDA8BE38669C62clipboard.png)

### 把密文取d的幂，再与3127取模得到明文。







