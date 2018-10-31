#-*- coding:utf-8 -*-
#author:wangxin
#blog:wooooe.com
import commands
mount_info=commands.getstatusoutput('/sbin/mount -l')
print mount_info[1]