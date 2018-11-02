#-*- coding:utf-8 -*-
import re
first_nas=open('first.dat','w')
second_nas=open('second.dat','w')
third_nas=open('third.dat','w')
fourt_nas=open('fourth.dat','w')
all_match_ip=[]
all_ip=[]
with open('hosts.dat','r') as rb_host:
    k=1
    for every_line in rb_host:
        if re.match('\d+\.\d+\.\d+\.\d+',every_line):
            ip= re.findall('\d+\.\d+\.\d+\.\d+',every_line)
            print k
            if  divmod(k,4)[1]==0:
            	first_nas.write(ip[0]+'\n') 
            	all_match_ip.append(ip[0])
            elif divmod(k,3)[1]==0:
            	second_nas.write(ip[0]+'\n') 
            	all_match_ip.append(ip[0])
            elif divmod(k,2)[1]==0:
            	third_nas.write(ip[0]+'\n') 
            	all_match_ip.append(ip[0])
            all_ip.append(ip[0])
            k+=1
for every_ip in all_ip:
	if not every_ip in all_match_ip:
		fourt_nas.write(every_ip+'\n')