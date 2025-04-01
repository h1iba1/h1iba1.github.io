库存查询按钮处，点击时会将url作为参数进行查询

![](images/98461AB49D304D33999DEC5901596DBCclipboard.png)



该行为可能存在ssrf



访问：http://localhost

发现存在/admin目录

![](images/FE6B98D745014B0BB202AD0B6424A5F7clipboard.png)

访问：http://localhost/admin



发现存在删除用户接口



![](images/89C8D27FC199495AB7C429C82DB867F0clipboard.png)

访问：http://localhost/admin/delete?username=wiener即可删除用户

