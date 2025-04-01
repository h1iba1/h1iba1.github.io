1.条件：操作用户必须要有导入导出文件的权限

执行：

```javascript
mysql> show global variables like '%secure_file_priv%';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| secure_file_priv | NULL  |
+------------------+-------+
1 row in set (0.00 sec)
```



secure_file_priv参数用于限制LOAD DATA, SELECT …OUTFILE, LOAD_FILE()传到哪个指定目录。



- secure_file_priv 为 NULL 时，表示限制mysqld不允许导入或导出。

- secure_file_priv 为 /tmp 时，表示限制mysqld只能在/tmp目录中执行导入导出，其他目录不  

               能执行。

- secure_file_priv 没有值时，表示不限制mysqld在任意目录的导入导出。



mysql5.7以上版本默认secure_file_priv为null。可通过mysql.ini修改。

添加：

```javascript
secure_file_priv=''
```

