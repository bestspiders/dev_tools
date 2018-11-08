#-*- coding:utf-8 -*-
import os,re
if os.path.exists('/etc/sysctl.conf'):
    all_content=''
    sysctl_options=open('/etc/sysctl.conf','r')
    for every_line in sysctl_options:
        if not re.findall(' *#',every_line):
            if re.findall('.*=',every_line):
                all_content=all_content+every_line
    print all_content