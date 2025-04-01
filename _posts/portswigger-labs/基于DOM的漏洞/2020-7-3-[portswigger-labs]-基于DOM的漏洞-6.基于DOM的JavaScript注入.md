哪些接收器会导致基于DOM的JavaScript注入漏洞？

以下是一些可能导致基于DOM的JavaScript注入漏洞的主要接收器：

```javascript
eval()
Function() constructor
setTimeout()
setInterval()
setImmediate()
execCommand()
execScript()
msSetImmediate()
range.createContextualFragment()
crypto.generateCRMFRequest()
```

