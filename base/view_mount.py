#-*- codingLutf-8 -*-
#author:wangxin
#blog:wooooe.com
import commands,os,re
if os.path.exists('/sbin/mount'):
    mount_cmd='/sbin/mount'
elif os.path.exists('/usr/bin/mount'):
    mount_cmd='/usr/bin/mount'
elif os.path.exists('/bin/mount'):
    mount_cmd='/bin/mount'
else:
    mount_cmd='mount'
info=commands.getstatusoutput(mount_cmd+' -l')
judge_mount=''
for every_line in info[1].split('\n'):
    line_list=every_line.split()
    parm_list=line_list[-1][1:-1].split(',')
    if re.findall('\d+\.\d+\.\d+\.\d+',line_list[0]):
        judge_mount=judge_mount+every_line+'\n'
    elif 'bind' in parm_list:
        judge_mount=judge_mount+every_line+'\n'
if judge_mount:
    print judge_mount