#-*- coding:utf-8 -*-
#author:wangxin
#blog:wooooe.com
import commands
all_connect=commands.getstatusoutput('netstat -anpl|grep ESTABLISHED')
print all_connect[1]
