#-*- coding:utf-8 -*- 
#author:wangxin
#blog:wooooe.com
import re,urllib2,socket,os,optparse,urllib,time,commands
def get_host_ip():
    try:
        sock_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock_conn.connect(('8.8.8.8', 80))
        ip = sock_conn.getsockname()[0]
    finally:
        sock_conn.close()

    return ip

select_number=1024 #本地端口大于多少数值，获取对外的ip和端口
all_connect=commands.getstatusoutput('netstat -anpl|grep ESTABLISHED')
connect_list=all_connect[1].split('\n')
all_ip_info=[]
for every_line in connect_list:
    line_list=every_line.split()
    if re.match('\d+\.\d+\.\d+\.\d+\:\d+',line_list[3]):
        ip_info=line_list[3].split(':')
        if int(ip_info[-1]) >1024:
            all_ip_info.append(line_list[4])
new_ip_list=[]
for every_ip in all_ip_info:
    if every_ip not in new_ip_list:
        new_ip_list.append(every_ip)
        print every_ip
