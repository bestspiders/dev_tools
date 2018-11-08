#-*- coding:utf-8 -*-
#author:wangxin
#blog:wooooe.com
#查看有哪些应用，并统计各自进程数
import commands,re,socket
def get_host_ip():
    try:
        sock_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_conn.connect(('8.8.8.8', 80))
        ip = sock_conn.getsockname()[0]
    finally:
        sock_conn.close()

    return ip
info=commands.getstatusoutput('ps -ef|grep -v grep')
now_ip=get_host_ip()
tomcat_number,jar_number,nginx_number,httpd_number,redis_number,memcache_number,kafka_number,zookeeper_number,ftp_number=0,0,0,0,0,0,0,0,0
for every_line in info[1].split('\n'):
    line_list=re.split(' +',every_line)
    if 'tomcat' in ' '.join(line_list[7:]) or 'catalina' in ' '.join(line_list[7:]) or 'Catalina' in ' '.join(line_list[7:]):
        tomcat_number+=1
    if '-jar' in ' '.join(line_list[7:]):
        jar_number+=1
    if 'nginx' in ' '.join(line_list[7:]):
        nginx_number+=1
    if 'httpd' in ' '.join(line_list[7:]):
        httpd_number+=1
    if 'redis' in ' '.join(line_list[7:]):
        redis_number+=1
    if 'memcache' in ' '.join(line_list[7:]):
        memcache_number+=1
    if 'kafka' in ' '.join(line_list[7:]):
        kafka_number+=1
    if 'zoo.cfg' in ' '.join(line_list[7:]):
        zookeeper_number+=1
    if 'ftp' in ' '.join(line_list[7:]):
        ftp_number+=1
if tomcat_number>0:
    print now_ip+':tomcat:'+str(tomcat_number)
if jar_number>0:
    print now_ip+':jar包:'+str(jar_number)
if nginx_number>0:
    print now_ip+':nginx:'+str(nginx_number)
if httpd_number>0:
    print now_ip+':httpd:'+str(httpd_number)
if redis_number>0:
    print now_ip+':redis:'+str(redis_number)
if memcache_number>0:
    print now_ip+':memcache:'+str(memcache_number)
if kafka_number>0:
    print now_ip+':kafka:'+str(kafka_number)
if zookeeper_number>0:
    print now_ip+':zookeeper:'+str(zookeeper_number)
if ftp_number>0:
    print now_ip+':ftp:'+str(ftp_number)