#!/usr/bin/env python
# -*- coding:utf-8 -*-
# _Author_ HW

import os
import sys
import time
import cmd

start_time = int(time.time())
#print("start_time:",start_time)

def ping_ip():
    #读IP列表
    f = open ("ip_list.txt","r")

    ip_yes = open ("ip_yes.txt","w")
    ip_no = open ("ip_no.txt","w")

    count_yes = 0
    count_no = 0

    for ip in f.readlines():
        ip = ip.strip('\n')
        backinfo = os.system("ping -c 2 -W 1 %s" %ip) #每个地址ping 2次,等1秒
        #print(backinfo)

        if backinfo :
            #print("ping %s is fail" %ip)
            ip_no.write(ip + '\n')
            count_no += 1
        else:
            #print("ping %s is true" %ip)
            ip_yes.write(ip + '\n')
            count_yes += 1

    ip_yes.close()
    ip_no.close()
    f.close()
    end_time = int(time.time())

    print("ping通数量: %s" % count_yes)
    print("ping不通数量: %s" % count_no)
    print("用时(s): %s" %(end_time-start_time))

ping_ip()
