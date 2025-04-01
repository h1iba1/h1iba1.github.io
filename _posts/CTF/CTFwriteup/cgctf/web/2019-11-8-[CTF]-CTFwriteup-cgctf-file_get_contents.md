## 1.查看网页源码

```javascript
<!--$file = $_GET['file'];
if(@file_get_contents($file) == "meizijiu"){
    echo $nctf;
}-->
```

get请求的得到的参数，使用file_get_contents读取要==meizijiu

file_get_contents()使用来读取文件的无法直接接收get请求的参数，所以此时无法使用？file=meizijiu



## 2.采用伪协议

php://input

data://



## 3.1 php://input

payload:?file=data://text/plain;base64,bWVpemlqaXU=



## 3.2data://

3.2.1 base64编码

payload:?file=data://text/plain;base64,bWVpemlqaXU=

