#!/usr/lib/python
# -*- coding: utf-8 -*-

import requests
import sys
import os
import ybpy_tool
configList = ('yhzz16_user','yhzz16_pasd','yhzz16_ser')
usercon = ybpy_tool.conf_read(configList)
yh_headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Referer: http://www.cicihappy.com/'
           'Accept - Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN',
           'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
           'Content-Type':' application/x-www-form-urlencoded'
           'Connection':'Keep-Alive'}
postdata = {'v':'2','username':usercon['yhzz16_user'],'password':usercon['yhzz16_pasd'],'universe':usercon['yhzz16_ser']}
posturl = 'http://u16.cicihappy.com/ogame/login.php'
res = requests.Session()
html_data = res.post(posturl,data=postdata,headers=yh_headers)
html_data.encoding = 'gbk'
print html_data.text
html_tz = res.get("http://u16.cicihappy.com/ogame/imperium.php",headers=yh_headers)
print html_tz.text

