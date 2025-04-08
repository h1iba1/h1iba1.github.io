# 1. 什么是XML？

XML代表“可扩展标记语言”。XML是一种设计用于存储和传输数据的语言。像HTML一样，XML使用标签和数据的树状结构。与HTML不同，XML不使用预定义标签，因此可以给标签指定描述数据的名称。在Web的早期历史中，XML成为一种流行的数据传输格式（“ AJAX”中的“ X”代表“ XML”）。但是，现在它的受欢迎程度已下降，而不再支持JSON格式。

2. 什么是XML实体？

XML实体是一种表示XML文档中的数据项的方式，而不是使用数据本身。XML语言规范内置了各种实体。例如，实体&lt;和&gt;代表字符<和>。这些是用于表示XML标签的元字符，因此，当它们出现在数据中时，通常必须使用它们的实体来表示它们。

3. 什么是文件类型定义？

XML文档类型定义（DTD）包含一些声明，这些声明可以定义XML文档的结构，可以包含的数据值的类型以及其他项。DTD DOCTYPE在XML文档开始处的可选元素中声明。DTD可以完全独立于文档本身（称为“内部DTD”），也可以从其他位置加载（称为“外部DTD”），也可以将两者混合使用。

4. 什么是XML自定义实体？

XML允许在DTD中定义自定义实体。例如：

<!DOCTYPE foo [ <!ENTITY myentity "my entity value" > ]>

此定义意味着&myentity;XML文档中实体引用的任何用法都将被定义的值“ my entity value” 替换。

5. 什么是XML外部实体？

XML外部实体是一种自定义实体，其定义位于声明它们的DTD之外。

外部实体的声明使用SYSTEM关键字，并且必须指定一个URL，从该URL可以加载实体的值。例如：

<!DOCTYPE foo [ <!ENTITY ext SYSTEM "http://normal-website.com" > ]>

URL可以使用该file://协议，因此可以从文件加载外部实体。例如：

<!DOCTYPE foo [ <!ENTITY ext SYSTEM "file:///path/to/file" > ]>

XML外部实体提供了引发XML外部实体攻击的主要方法。