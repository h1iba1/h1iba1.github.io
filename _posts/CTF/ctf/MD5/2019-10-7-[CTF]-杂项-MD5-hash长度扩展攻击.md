MD5hash长度扩展攻击：

发动条件：

1.已知待攻击密文MD5值，盐值长度

2.MD5加密内容可控



例如：

```javascript
$adore='***************';//不知道的字符
$now = $_POST['lover'];
setcookie("Heart", md5($adore.'syclover'));
if(isset($now)&&$now!=syclover) {
	if($_COOKIE['Heart'] === md5($adore. urldecode($now))){
		die ($flag);
		}else {
			die('I do not love you! You are not in my heart!');
			}
	}
```

该题：

我们必须满足：

```javascript
md5(***************syclover)=md5(***************syclover1)//此处为强等于
```



借用hashpump工具：

```javascript
1.安装
git clone https://github.com/bwall/HashPump
apt-get install g++ libssl-dev
cd HashPump
make
make install
```



```javascript
Input Signature: 6a1ce5f4dc83320710006a786ac82c17  //md5值
Input Data: syclover                   //盐值
Input Key Length: 15                   //位置内容长度
Input Data to Add: wn                  //任意添加
44967b0cf3086aaeeb6bbc6cf8c40774       //盐值的所得payload加密后得到的值
syclover\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb8
\x00\x00\x00\x00\x00\x00\x00wn
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/MD5/images/5C8B3BB91ED042AEAA8DBC0A88DD0977clipboard.png)



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/MD5/images/F9D56910A66442849A6DC4F03299C89Cclipboard.png)

注：此处的payload：\x需要替换成%



hash长度扩展攻击原理：

https://www.cnblogs.com/p00mj/p/6288337.html

通俗来讲，就是MD5把每512位当作一组进行加密计算，首先有一个初始序列的值（该值是固定的），这个初始序列与信息的第一组512位进行运算，得到一个结果，该结果作为下一组512位的初始序列，再进行同样的运算，依此类推。需要注意的是，最后一个分组的后64位用来显示原消息的总长，是预留的，也就是说，最后一个分组只能有448位。



有一个问题就是，如果要是（加密的信息长度+64）并不是512的整数倍怎么办呢？



MD5的策略是：



最后一个分组如果不足512，则进行填充，填充的策略是：在原消息和原消息总长之间填充01字符串，第一位为1，剩下的全部填充0。



这样其实就有了一个漏洞：



如果给出一个message和该message经过md5加密后的值，我们可以通过手动填充，把消息长度填充到512的整数倍，再根据这个新的字符串，自己计算出md5值（因为有原message的md5值，相当于知道了加密的初始序列），同样可以成功。

