#!/usr/bin/python
#-*- coding: UTF-8 -*-


import os
import sys
import time


def mkdir(path): #创建目录
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print "创建目录",path
        os.makedirs(path)
        return True
    else:
        print "目录存在",path
        return False

def get_time(ms = 0): #获取毫秒级的时间
    ct = time.time()
    local_time = time.localtime(ct)
    if ms == 0:
        data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        return data_head
    else:
        data_head = time.strftime("%Y%m%d%H%M%S", local_time)
        data_secs = (ct - long(ct)) * 1000
        time_stamp = "%s%03d" % (data_head, data_secs)
        return time_stamp

