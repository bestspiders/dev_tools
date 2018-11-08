#-*- coding:utf-8 -*-
#author:wangxin
#blog:wooooe.com
import commands,os
if not os.path.exists('/sbin/route'):
	route_cmd='route'
else:
	route_cmd='/sbin/route'
route_info=commands.getstatusoutput(route_cmd+' -n')
print route_info[1]