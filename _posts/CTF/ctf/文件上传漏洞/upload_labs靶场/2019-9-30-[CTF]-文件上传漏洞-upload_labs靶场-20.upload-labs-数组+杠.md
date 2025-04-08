

```javascript
$is_upload = false;
$msg = null;
if(!empty($_FILES['upload_file'])){
    //检查MIME
    $allow_type = array('image/jpeg','image/png','image/gif');
    if(!in_array($_FILES['upload_file']['type'],$allow_type)){
        $msg = "禁止上传该类型文件!";
    }else{
        //检查文件名
        $file = empty($_POST['save_name']) ? $_FILES['upload_file']['name'] : $_POST['save_name'];
        if (!is_array($file)) {
            $file = explode('.', strtolower($file));
        }

        $ext = end($file);
        $allow_suffix = array('jpg','png','gif');
        if (!in_array($ext, $allow_suffix)) {
            $msg = "禁止上传该后缀文件!";
        }else{
            $file_name = reset($file) . '.' . $file[count($file) - 1];
            $temp_file = $_FILES['upload_file']['tmp_name'];
            $img_path = UPLOAD_PATH . '/' .$file_name;
            if (move_uploaded_file($temp_file, $img_path)) {
                $msg = "文件上传成功！";
                $is_upload = true;
            } else {
                $msg = "文件上传失败！";
            }
        }
    }
}else{
    $msg = "请选择要上传的文件！";
}
```

可以发现$file_name经过reset($file) . '.' . $file[count($file) - 1];处理。

如果上传的是数组的话，会跳过$file = explode('.', strtolower($file));。并且后缀有白名单过滤

$ext = end($file);
$allow_suffix = array('jpg','png','gif');


而最终的文件名后缀取的是$file[count($file) - 1]，因此我们可以让$file为数组。$file[0]为smi1e.php/，也就是reset($file)，然后再令$file[2]为白名单中的jpg。此时end($file)等于jpg，$file[count($file) - 1]为空。而 $file_name = reset($file) . '.' . $file[count($file) - 1];，也就是smi1e.php/.，最终move_uploaded_file会忽略掉/.，最终上传smi1e.php。



## 文件上传成功：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/BADB0EAA996F4022859F616ECF28F893clipboard.png)

## 直接访问：

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/ctf/文件上传漏洞/upload_labs靶场/images/CF0F2C3DF17D4125BEB4283C0E9E07ECclipboard.png)

