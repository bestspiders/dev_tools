#-*- coding:utf-8 -*-
#author:wangxin
#blog:wooooe.com
import commands
route_info=commands.getstatusoutput('/sbin/route -n')
print route_info[1]