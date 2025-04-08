【怎么做】当原始注入遇到困难时，可尝试加载相应脚本，进行绕过，说不定会有意外惊喜。在sqlmap的原命令中加入以下代码，即可使用脚本，进行更加强有力的渗透。

```javascript
--tamper“脚本名称”
```

Part 2

sqlmap版本当前为1.2.7.20，共有57个tamper脚本，与1.0版本相比新增了19个脚本。

| 序号 | 脚本名称 | 注释 |
| - | - | - |
| 1 | 0x2char | 将每个编码后的字符转换为等价表达 |
| 2 | apostrophemask | 单引号替换为Utf8字符 |
| 3 | apostrophenullencode | 替换双引号为%00%27 |
| 4 | appendnullbyte | 有效代码后添加%00 |
| 5 | base64encode | 使用base64编码 |
| 6 | between | 比较符替换为between |
| 7 | bluecoat | 空格替换为随机空白字符，等号替换为like |
| 8 | chardoubleencode | 双url编码 |
| 9 | charencode | 将url编码 |
| 10 | charunicodeencode | 使用unicode编码 |
| 11 | charunicodeescape | 以指定的payload反向编码未编码的字符 |
| 12 | commalesslimit | 改变limit语句的写法 |
| 13 | commalessmid | 改变mid语句的写法 |
| 14 | commentbeforeparentheses | 在括号前加内联注释 |
| 15 | concat2concatws | 替换CONCAT为CONCAT\_WS |
| 16 | equaltolike | 等号替换为like |
| 17 | escapequotes | 双引号替换为\\\\\\\\ |
| 18 | greatest | 大于号替换为greatest |
| 19 | halfversionedmorekeywords | 在每个关键字前加注释 |
| 20 | htmlencode | html编码所有非字母和数字的字符 |
| 21 | ifnull2casewhenisnull | 改变ifnull语句的写法 |
| 22 | ifnull2ifisnull | 替换ifnull为if(isnull(A)) |
| 23 | informationschemacomment | 标示符后添加注释 |
| 24 | least | 替换大于号为least |
| 25 | lowercase | 全部替换为小写值 |
| 26 | modsecurityversioned | 空格替换为查询版本的注释 |
| 27 | modsecurityzeroversioned | 添加完整的查询版本的注释 |
| 28 | multiplespaces | 添加多个空格 |
| 29 | nonrecursivereplacement | 替换预定义的关键字 |
| 30 | overlongutf8 | 将所有字符转义为utf8 |
| 31 | overlongutf8more | 以指定的payload转换所有字符 |
| 32 | percentage | 每个字符前添加% |
| 33 | plus2concat | 将加号替换为concat函数 |
| 34 | plus2fnconcat | 将加号替换为ODBC函数{fn CONCAT()} |
| 35 | randomcase | 字符大小写随机替换 |
| 36 | randomcomments | /\*\*/分割关键字 |
| 37 | securesphere | 添加某字符串 |
| 38 | sp\_password | 追加sp\_password字符串 |
| 39 | space2comment | 空格替换为/\*\*/ |
| 40 | space2dash | 空格替换为–加随机字符 |
| 41 | space2hash | 空格替换为\#加随机字符 |
| 42 | space2morecomment | 空格替换为/\*\*\_\*\*/ |
| 43 | space2morehash | 空格替换为\#加随机字符及换行符 |
| 44 | space2mssqlblank | 空格替换为其他空符号 |
| 45 | space2mssqlhash | 空格替换为%23%0A |
| 46 | space2mysqlblank | 空格替换为其他空白符号 |
| 47 | space2mysqldash | 空格替换为–%0A |
| 48 | space2plus | 空格替换为加号 |
| 49 | space2randomblank | 空格替换为备选字符集中的随机字符 |
| 50 | symboliclogical | AND和OR替换为&amp;&amp;和|| |
| 51 | unionalltounion | union all select替换为union select |
| 52 | unmagicquotes | 宽字符绕过GPC |
| 53 | uppercase | 全部替换为大写值 |
| 54 | varnish | 添加HTTP头 |
| 55 | versionedkeywords | 用注释封装每个非函数的关键字 |
| 56 | versionedmorekeywords | 使用注释绕过 |
| 57 | xforwardedfor | 添加伪造的HTTP头 |


