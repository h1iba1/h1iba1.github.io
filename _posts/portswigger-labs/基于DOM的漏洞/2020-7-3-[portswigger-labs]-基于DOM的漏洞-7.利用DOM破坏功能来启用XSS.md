网站文章页面可以评论html，此时考虑存储型xss。但是js代码均被dompurify.js过滤

可以破坏dom结构来桡骨dompurify.js的检测



特定博客文章的页面将导入JavaScript文件loadCommentsWithDomPurify.js，其中包含以下代码：

```javascript
let defaultAvatar = window.defaultAvatar || {avatar: '/resources/images/avatarDefault.svg'}
```

defaultAvatar使用此危险模式来实现 该对象，该危险模式包含逻辑OR运算符和全局变量。这使其很容易遭受DOM破坏。



您可以使用锚标记破坏该对象。创建两个具有相同ID的锚会导致将它们分组在DOM集合中。所述name在第二锚定属性包含值"avatar"，这将在揍avatar属性与内容href属性。

请注意，该站点使用DOMPurify筛选器来尝试减少基于DOM的漏洞。但是，DOMPurify允许您使用该cid:协议，该协议不会对双引号进行URL编码。这意味着您可以插入编码的双引号，该双引号将在运行时进行解码。结果，上述注入将使defaultAvatar变量{avatar: ‘cid:"onerror=alert(1)//’}在下次加载页面时被赋予破坏属性。

当您发表第二篇文章时，浏览器将使用新近使用的全局变量，该变量将onerror事件处理程序中的有效负载走私并触发alert()。



poc:

```javascript
<a id=defaultAvatar><a id=defaultAvatar name=avatar href="cid:&quot;onerror=alert(1)//">
```

当返回文章，再次评论时，即可触发xss