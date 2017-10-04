#!/usr/bin/python
#coding=UTF-8
import os
import re

def opst(data):
    post_list = data.split('\n')
    post_key = post_list[4][-20:-1]
    pattern = re.compile(r"Content-Disposition: form-data; name=([\s|\S]*?)"+post_key)
    match = pattern.findall(data)
    #print r'%s' %(post_key) 
    print match[0].decode('utf-8'),match[1].decode('utf-8')

op = '''POST / HTTP/1.1
Accept: text/html, application/xhtml+xml, image/jxr, */*
Referer: http://172.16.1.9:9898/
Accept-Language: zh-CN
Content-Type: multipart/form-data; boundary=---------------------------7e1374186032c
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/                                                                    51.0.2704.79 Safari/537.36 Edge/14.14393
Accept-Encoding: gzip, deflate
Host: yabin.zgdgz.org:9898
Content-Length: 261
Connection: Keep-Alive
Cache-Control: no-cache
Cookie: sessionLang=en

-----------------------------7e1374186032c
Content-Disposition: form-data; name="name"

测试的
-----------------------------7e1374186032c
Content-Disposition: form-data; name="text"

此处输入文本
-----------------------------7e1374186032c--
'''
opst(op)
