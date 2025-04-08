漏洞环境：

https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-all-standard-tags-blocked



当waf过滤所有js标签时，可以考虑使用自定义标签



前置知识url中#的用处

他的功能是：使窗口定位到页面中的id,class的位置，用法通常是

```javascript
https://www.example.com/index.html#id
```



例如: 

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/6402AB7EB2F041D0AA0C47C47F7771EAclipboard.png)





调用过程中,  可以理解为选中/加载了指定id或者class标签。



 



# 小试牛刀

正如前言所述的情况, 页面运行写入自定义的(非html)标签:

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/B31EE73D00DE40B49D461CB8ECC3F53Eclipboard.png)



于是熟练的配合xss打出一个payload?

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/2C7BB9E1D32E42F290CB170F9A018020clipboard.png)





发现, alert并没有被执行, 似乎少了点什么...



# 符号虽然可以将页面定位到指定id上, 但是自定义的custom标签并没有获得焦点(focus), 所以包含的alert事件并不会被执行。



敲黑板! 划重点! 



# tabindex属性

 html中的tabIndex属性可以设置键盘中的TAB键在控件中的移动顺序,即焦点的顺序。  



 把控件的tabIndex属性设成1到32767的一个值，就可以把这个控件加入到TAB键的序列中。  



 这样，当浏览者使用TAB键在网页控件中移动时，将首先移动到具有最小tabIndex属性值的控件上，最后在具有最大tabIndex属性值的控件上结束移动。   



如果有两个控件的tabIndex属性相同，则以控件在html代码中出现的顺序为准。  



 默认的tabIndex属性为 0 ，将排列在在所有指定tabIndex的控件之后。   



而若把tabIndex属性设为一个负值（如tabIndex="-1"），那么这个链接将被排除在TAB键的序列之外



了解了tabindex的功能之后, 这里就加入tabindex属性配合#符号来使得自定义标签获得焦点:

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/portswigger-labs/xss/images/BB8031CF367B44CA96940D907B4E3AD5clipboard.png)







# 防护措施

1. 将< >标签禁止;



2. html编码实体化



文章来源：

https://blog.csdn.net/angry_program/article/details/106267437

