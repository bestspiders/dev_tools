# netstat_1024.py <br>
**Python ENV:** 2.4+ <br>
获取监听本地端口大于1024的 访问外部ip和端口<br>
```
select_number=1024
```
修改为你判断的端口
# netstat_all.py <br>
**Python ENV:** 2.4+ <br>
获取所有连接数
# view_app.py <br>
**Python ENV:** 2.4+ <br>
获取所有应用进程数量,可判断的应用为tomcat,jar包,nginx,httpd,redis,memcache,kafka,zookeeper,ftp
# view_dns.py <br>
获取所有的dns<br>
# view_mount.py<br>
获取所有的挂载
# view_route.py<br>
获取所有的路由
# view_version.py<br>
**Python ENV:** 2.6+<br>
参考了此脚本编写https://github.com/nixawk/nmap_vscan/blob/master/nmap_vscan/vscan.py<br>
获取所有应用版本<br>
# copy_file<br>
**Python ENV:** 2.4+<br>
**PHP ENV:** 7.0+<br>
此为分布式复制文件系统<br>
将copy_file文件夹放置于网站根目录<br>
修改change_status.php、copy_copy_copy.php的数据库连接账号和密码，默认数据库phoenix。<br>
将desc_table.sql导入phoenix。<br>
数据库结构
```
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| host      | varchar(20) | YES  |     | NULL    |                |
| tag_name  | varchar(30) | YES  |     | NULL    |                |
| status    | int(1)      | YES  |     | NULL    |                |
| copy_src  | longtext    | YES  |     | NULL    |                |
| copy_dest | longtext    | YES  |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```
host为执行此任务的主机ip<br>
tag_name为一次任务的标签（自定义)<br>
status为任务状态（0为未开始，1为进行中，2为已完成，3为源文件不存在）<br>
copy_src为复制源文件绝对路径<br>
copy_dest为复制目的绝对路径<br>
只可以复制文件，如果是文件夹则会创建，如果文件目录不存在则会创建<br>
copy_magic.py
```
    post_data={'tag_name':"test_host",'host':get_host_ip()}#需修改tag_name
    copy_main_url="http://0.0.0.0/copy_life/copy_copy_copy.php"#修改为你的ip
    post_url='http://0.0.0.0/copy_life/change_status.php'#修改为你的ip
    proxy_ip=''#有则填写
```
