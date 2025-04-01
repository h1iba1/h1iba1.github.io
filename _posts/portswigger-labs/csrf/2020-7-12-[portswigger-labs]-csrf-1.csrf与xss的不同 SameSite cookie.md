通常来说xss比csrf更严重



csrf用来诱使用户执行他不想执行的操作

xss用来执行javascript脚本



可以通过添加csrf令牌在一定程度上防御反射型xss，但是此时csrf令牌在url中，可能存在暴露的风险



