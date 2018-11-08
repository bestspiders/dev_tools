#-*- coding:utf-8 -*-
import commands,os,re
if os.path.exists('/var/spool/cron/tabs/root'):
    crontab_options=open('/var/spool/cron/tabs/root','r')
    crontab_content=crontab_options.read()
    crontab_options.close()
elif os.path.exists('/var/spool/cron/root'):
    crontab_options=open('/var/spool/cron/root','r')
    crontab_content=crontab_options.read()
    crontab_options.close()
all_content=''
for every_line in crontab_content.split('\n'):
    if not  re.findall(' *#',every_line):
        if re.findall('\*+',every_line):
            all_content=all_content+every_line+'\n'
print all_content