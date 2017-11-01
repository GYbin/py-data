#!/usr/lib/python
# -*- coding: utf-8 -*-

import requests
import sys
import os
import ybpy_tool
configList = ('yhzz_username','yhzz_passwd','yhzz_ser')
usercon = ybpy_tool.conf_read(configList)
username = usercon['yhzz_username']
passwd = usercon['yhzz_passwd']
ser_login = usercon['yhzz_ser']
yh_headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
           'Accept - Encoding':'gzip, deflate',
           'Accept-Language':'zh-CN',
           'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
           'Connection':'Keep-Alive'}
postdata = {'v':'2','username':username,'password':passwd,'universe':ser_login}
posturl = 'http://u11.cicihappy.com/ogame/login.php'
res = requests.Session()
html_data = res.post(posturl,data=postdata,headers=yh_headers)
print html_data.text
html_tz = res.get("http://u11.cicihappy.com/ogame/imperium.php",headers=yh_headers)
print html_tz.text

