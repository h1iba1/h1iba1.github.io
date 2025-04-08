# 考察知识点：

## 1.Java 任意文件读取

## 2. java配置文件web.xml读取



# 1.访问help

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/DB69E4D03DB8471EAC4CAB5C9F6E1C0Eclipboard.png)

# 2. 感觉是文件读取，改为post请求

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/4E00125D5DDC41548B7BEB90F3487272clipboard.png)

# 3. 尝试读取java的配置文件

找到flag文件所在位置

![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/DD8E65A9D6CD485683EE941C3BDE9608clipboard.png)



# 4.尝试读取flag文件

java编译的class文件存放在classes文件下：

然后访问flag，因为时目录，所以需要将.换位/

所以访问：

 /Download?filename=WEB-INF/classes/com/wm/ctf/FlagController.class



![](https://raw.githubusercontent.com/h1iba1/h1iba1.github.io/refs/heads/master/_posts/CTF/CTFwriteup/buuctf练习笔记/images/A56B4F64BBE449D6A1428C5450F3D3FFclipboard.png)

base64解码即可得到flag