#-*- codingLutf-8 -*-
#author:wangxin
#blog:wooooe.com
import re
dns_options=open('/etc/resolv.conf','r')
dns_info=dns_options.read()
dns_options.close()
dns_list=dns_info.split('\n')
for every_line in dns_list:
    if not re.match('^#',every_line):
        if re.findall('\d+\.\d+\.\d+\.\d+',every_line):
            print every_line