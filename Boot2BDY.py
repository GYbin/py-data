#!/usr/lib/python
#-*- coding: UTF-8 -*-
import os
import sys
import urllib
import urllib2
import filecmp #比较两个文件是否一样
import ybpy_tool
bfname = ybpy_tool.get_time(1)+".tgz"
bfdir = "../data/Boot2BDY/"
ybpy_tool.mkdir(bfdir)
bfcrl = "tar -cvpf %s%s --exclude=lost+found /boot" %(bfdir,bfname) #不能压缩文件，否则每次生成的备份都不一样
print bfcrl
cliput = os.popen(bfcrl)
bflog = cliput.readlines()
bffiles = bfdir+bfname
bffiled = bfdir+"bf_boot.tgz"
mvcrl = "mv %s %s" %(bffiles,bffiled)
if not os.path.exists(bffiled): 
    cliput = os.popen(mvcrl)
    print "设置上传标志"
else:
    if not filecmp.cmp(bffiles,bffiled):
        print filecmp.cmp(bffiles,bffiled)
        rmcrld = "rm -f "+bffiled
        cliput = os.popen(rmcrld)
        cliput = os.popen(mvcrl)
        print "设置上传表示"
    else:
        print "文件相同"
        rmcrls = "rm -f "+bffiles
        cliput = os.popen(rmcrls)
