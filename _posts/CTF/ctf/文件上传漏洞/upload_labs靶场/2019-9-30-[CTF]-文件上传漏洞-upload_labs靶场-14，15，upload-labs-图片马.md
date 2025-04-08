和labs13一样上传图片马即可获取。

labs14和labs15和labs13的不同点在于：

labs14：

采用getimagesize()函数：

getimagesize(string $filename):

获取图片的大小，如果获取的图片，不是有效图片则返回flase，自4.3.0起还可以获取图片类型。

代码如下：

```javascript
function isImage($filename){
    $types = '.jpeg|.png|.gif';
    if(file_exists($filename)){
        $info = getimagesize($filename);
        $ext = image_type_to_extension($info[2]);
        if(stripos($types,$ext)>=0){
            return $ext;
        }else{
            return false;
        }
    }else{
        return false;
    }
}
```



labs15:

采用exif_imagetype()函数：

读取一个图片的第一个字节，并检查其签名，如果发现了恰当的签名则返回一个对应的常量，否则返回flase。

labs15函数代码如下：

```javascript
function isImage($filename){
    //需要开启php_exif模块
    $image_type = exif_imagetype($filename);
    switch ($image_type) {
        case IMAGETYPE_GIF:
            return "gif";
            break;
        case IMAGETYPE_JPEG:
            return "jpg";
            break;
        case IMAGETYPE_PNG:
            return "png";
            break;    
        default:
            return false;
            break;
    }
}
```



这两个函数都可以直接用图片马绕过，图片马制作方式见labs13.













