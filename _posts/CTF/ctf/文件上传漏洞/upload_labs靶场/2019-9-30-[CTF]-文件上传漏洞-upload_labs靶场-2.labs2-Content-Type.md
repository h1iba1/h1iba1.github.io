直接phpinfo.php上传文件显示：

![](images/15D6B38A2C2A4122B2C45A8D9F956C0Cclipboard.png)

抓包：

1.更改文件后缀名为gif，上传失败

![](images/2EAA4D200B0445F4AF0C3F2207034557clipboard.png)

2.更改Content-Type:为image/gif。报错已消失。查看目录下已有，phpinfo.php文件

![](images/B8705B8A953E479CAA36D24D3F9D88E2clipboard.png)

