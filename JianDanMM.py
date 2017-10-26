#!/usr/lib/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
import os
import time 
def get_time_stamp(): #获取毫秒级的时间
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y%m%d%H%M%S", local_time)
    data_secs = (ct - long(ct)) * 1000
    time_stamp = "%s%03d" % (data_head, data_secs)
    return time_stamp

def mkdir(path): #煎蛋MM名称创建目录
    path = path.strip()
    isExists = os.path.exists(path)
    if not isExists:
        print "创建目录",path
        os.makedirs(path)    
        return True
    else:
        print "目录存在",path
        return False

def mm_down(name,mmurl_list): #下载照片信息
    if not name:
        return False
    if not mmurl_list:
        return False
    jdmm_dir = "../data/JianDanMM/"+name
    mkdir(jdmm_dir)
    
    for mmurl in mmurl_list:
        mmurl = "https://w"+mmurl
        mmtzm = mmurl[-4:]
        mmdirjpg = jdmm_dir+"/"+get_time_stamp()+mmtzm
        print "开始下载:",mmurl
        urllib.urlretrieve(mmurl,mmdirjpg)
        print "下载完成:",mmdirjpg

def one_jd(txt_str,start_str,end_str):#获取单个煎蛋MM的列祖
    endFind = 0
    str_list = []
    while True :
        startFind = txt_str.find(start_str,endFind)
        if startFind == -1:
            break
        endFind = txt_str.find(end_str,startFind)
        str_list.append(txt_str[startFind:endFind])
    return str_list

def jdmm_name(txt_scr): #获取煎蛋MM的名字
    pattern = re.compile('title=\"防伪码(.*?)>(.*?)</strong>')
    name = re.findall(pattern,txt_scr)
    if name:
        return name[0][1]

def jdmmjpg_url(txt_scr):#获取煎蛋MM照片的地址
    pattern = re.compile(r'href="//w(.*?)" target=')
    mmjp = re.findall(pattern,txt_scr)
    if mmjp:
        return mmjp
for htmlnul in range(114,214):
    url = r"https://jandan.net/ooxx/page-%s#comments" %str(htmlnul)
    page = urllib.urlopen(url)
    html = page.read()
    html_start = "<li id=\""
    html_end = "</li>"
    html_list = one_jd(html,html_start,html_end)
    print "第%s波MM来了" %str(htmlnul)
    for html_txt in html_list:
        mm_down(jdmm_name(html_txt),jdmmjpg_url(html_txt))
    print "这页没有MM了"
print "所有MM发现完毕"


'''for html_txt in html_list:
    fp = open("test.txt","a+")
    fp.write(html_txt)
    fp.close()
print len(html_list)
'''    
