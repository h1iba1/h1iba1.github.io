
<h1 id="1%E6%8B%89%E5%8F%96%E9%95%9C%E5%83%8F">1.拉取镜像</h1>
<h2 id="mysql">mysql</h2>



<pre class="wp-block-code"><code>docker pull mysql:5.7.32</code></pre>


<h2 id="wordpress">wordpress</h2>



<pre class="wp-block-code"><code>docker pull wordpress</code></pre>


<h1 id="2-%E5%90%AF%E5%8A%A8%E9%95%9C%E5%83%8F">2. 启动镜像</h1>


<h2 id="mysql-1">mysql</h2>



<pre class="wp-block-code"><code>docker run --name mysql-wordpress -d -v /wordpress/mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD="root" mysql:5.7.32</code></pre>


<h2 id="wordpress-1">wordpress</h2>



<pre class="wp-block-code"><code>docker run --name wordpress -d -p 80:80 --link mysql-wordpress:mysql -v /wordpress/wordpress-html:/var/www/html wordpress</code></pre>


<h1 id="3%E5%A4%87%E4%BB%BD">3.备份</h1>


<p>-v 参数表示将容器的某个目录挂载到本地，相当于将容器的数据存储到了本地。此时我们要做博客备份或者迁移只需要打包/wordpress文件到新主机。在需要迁移的主机上运行上面启动镜像的命令即可。</p>



## 踩坑:

## 1.插件安装需要ftp账号

docker新建一个ftp账号太麻烦，可以进入wordpress容器，使用wget下载插件到/wp-content/plugins/目录下unzip解压，再在插件页刷新即可。



## 2.图片上传显示无法移动文件到/uploads目录下

这是因为/uploads目录的所属用户为root，而apache的用户为www-data

```shell
#查看apche所属用户
ps aux | grep apache

#更改uploads/目录所属用户
chmos -R www-data uploads/
```



<h1 id="%E5%8F%82%E8%80%83%E6%96%87%E7%AB%A0">参考文章</h1>



<p><a href="https://developer.aliyun.com/article/583768">https://developer.aliyun.com/article/583768</a></p>