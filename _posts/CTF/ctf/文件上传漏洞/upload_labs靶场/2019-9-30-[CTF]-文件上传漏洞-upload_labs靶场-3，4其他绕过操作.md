3.利用操作系统特性

3.1首先更改上传文件文件名为：

phpinfo.php.::$DATA,文件上传成功

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/76A1913FD983479BBCD4FFA9CA920B1Bclipboard.png)

文件下生成一个heibai.php.文件，但是却无法直接访问

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/F0C0EFA8703B4352A455DACBC61F597Dclipboard.png)

3.2紧接着修改文件后缀为.php>，上传成功（此处也可以用.php<,.php"，.php\）

详情看这里：

http://www.bendawang.site/2017/05/29/-%E7%BB%AD%E7%AF%87-%E4%B8%80%E4%B8%AAWindows%E4%B8%8B%E7%9A%84%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E7%9A%84%E5%B0%8Ftrick/

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/6E4281A423FB43DDADA613AD62F073FAclipboard.png)

此时在upload文件下生成一个heibai.php文件。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/13655F531A754681A9A197372F7122A9clipboard.png)

在浏览器中访问，heibai.php文件和heibai.php.文件都能成功访问！！！(好神奇）

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/79170C84A9E4474788EDB20D0ACDFA97clipboard.png)

4.修改文件后缀为php%aa (url解码)

将%aa放到bp的Decode中进行url解码。（此处的%aa可用%b2,%b3等代替）

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/C859FAEF3A664A7CA3973F4A247DAF06clipboard.png)

将解码的内容复制到repeater中，重放攻击。文件上传成功。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/DC2AE56A2BEB4DEDBCF0A8C4589AC72Dclipboard.png)

此时去访问heibai.php文件访问成功。（好神奇，师傅们的思路真多）

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/0AC4A3E01DD143A1BED9A91278EB556Fclipboard.png)

参考链接：

https://fuping.site/2018/06/04/upload-labs-writeup/      labas3,labs4