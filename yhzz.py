#!/usr/lib/python
# -*- coding: utf-8 -*-

import requests
import sys
import os
import ybpy_tool
import re
import time
reload(sys)
yhzzxq={}
sys.setdefaultencoding('utf-8')
ConfigFile = "yhzz16.cf"
configList = ('username','passwd','service','geturl','getfile','head_Ref')
usercon = ybpy_tool.conf_read(configList,ConfigFile)
login_Ref = ''
res = requests.Session()
def headers(proto="get"): #发送的头文件定义
    if login_Ref:
        head_Ref = login_Ref
    else:
        head_Ref = usercon['head_Ref']
    if proto=='get':
        get_headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Referer':head_Ref,
            'Accept - Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Content-Type':'application/x-www-form-urlencoded'}
        return get_headers
    elif proto =='post':
        post_headers = {'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
            'Referer':head_Ref,
            'Accept - Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Content-Type':'application/x-www-form-urlencoded'}
        return post_headers
    else:
        print "协议错误"
        return -1

def laft_lan(html): #获取侧边栏选项地址
    laft_bs={'gk':'概 况','jz':'建 筑','yj':'研 究',
              'cc':'船 厂','fy':'防 御','lm':'联 盟',
              'jd':'舰 队','xx':'消 息','ybyh':'外部银河',
              'xqsz':'星球设置','kjs':'科技树'}
    laft_url={'gk':'','jz':'','yj':'',
              'cc':'','fy':'','lm':'',
              'jd':'','xx':'','ybyh':'',
              'xqsz':'','kjs':''}
    pattern = r'<!-- LEFTMENU -->(.*?)<!-- END LEFTMENU -->'
    html_tmp = re.findall(pattern,html,re.S)
    pattern = r'<li class="menubutton_table">(.*?)</li>'
    html_tmp = re.findall(pattern,html_tmp[0],re.S)
    for laft_bskey in laft_bs:
        for urldata_tmp in html_tmp:
            pattern = r'<span class="textlabel">(.*?)</span>'
            urlname_tmp = re.findall(pattern,urldata_tmp)
            if not urlname_tmp:
                continue
            if urlname_tmp[0]==laft_bs[laft_bskey]:
                pattern = r'<a href=\"(.*?)" class="menubutton'
                lafturl_tmp = re.findall(pattern,urldata_tmp)
                laft_url[laft_bskey]=lafturl_tmp[0]
    return laft_url

def get_laft_lan(laft_data):
#    if not isinstance(laft_url_dict,dict):
#        print "传入写入参数需要使用Dict类型"
    time.sleep(2)
    global login_Ref
    url_tmp=usercon['geturl']+laft_lan_url[laft_data]
    login_Ref = url_tmp
    html_txt = res.get(url_tmp,headers=headers('get'))
    html_txt.encoding = 'gbk'
    if laft_data=='gk':
        get_laft_langk(html_txt.text)
    elif laft_data=='jz':
        return html_txt.text
        get_laft_lanjz(html_txt.text)
    else:
        return html_txt.text
    #get_laft_langk(html_txt.text)


def get_laft_lanjz(get_html):
    pattern = r'<td class="l">(.*?)</font></a></td>'
    zyjz_tmp = re.findall(pattern,get_html,re.S)
    for zyjz_tmpxx in zyjz_tmp:
        pattern = r'href="infos.php\?gid=(.*?)">(.*?)</a> \((.*?)\)<br>'
        zyjz_list = re.findall(pattern,zyjz_tmpxx) 
        print zyjz_list[0][1],zyjz_list[0][2]


def get_laft_langk(get_html):
    pattern = r'<div id="[metalx|crystalx|deuteriumx]*"[><font color="#ff0000"]*>(.*?)<[/font><]*/div></td>'
    zy_tmp = re.findall(pattern,get_html)
    pattern = r'<div id="deuteriumx".*?align="center" width="140"[><font color="#ff0000"]*>(.*?)<[/font><]*/td>.*?<font color="lime">(.*?)</font></td>'
    nl_tmp = re.findall(pattern,get_html,re.S)
    pattern = r'<option [selected="selected" ]*value="(.*?)">(.*?)&nbsp;\[(.*?)\]&nbsp;&nbsp;</option>'
    xqgk_tmp = re.findall(pattern,get_html)
    pattern = r'textContent\[1\].*?\\"#\\">(.*?)  \(<a.*?">(.*?)</a>.*?>(.*?)<'
    xqgk_tmpdq = re.findall(pattern,get_html)
    pattern = r'textContent\[5\].*?\[(.*?)\]'
    xqgk_tmpwz = re.findall(pattern,get_html)
    print '发现星球：'
    global yhzzxq
    numtmp = 0
    for xqgk_tmpzl in xqgk_tmp:
        numtmp = numtmp+1
        xqname = xq+str(numtmp)
        yhzzxq[xqname]={'xqwz':xqgk_tmpzl[2],'xqname':xqgk_tmpzl[1],'xqline':xqgk_tmpzl[0]}
        print '位置:'+xqgk_tmpzl[2],'名称：'+xqgk_tmpzl[1],'链接：'+xqgk_tmpzl[0]
    print '当前星球位置：'+xqgk_tmpwz[0]
    print '当前星球大小:'+xqgk_tmpdq[0][0],'使用率'+xqgk_tmpdq[0][1],'最大空间'+xqgk_tmpdq[0][2]
    print "金属："+zy_tmp[0],"晶体："+zy_tmp[1],"重氢："+zy_tmp[2]
    print "能量："+nl_tmp[0][0],"暗物质："+nl_tmp[0][1]
    return 0

postdata = {'v':'2','username':usercon['username'],'password':usercon['passwd'],'universe':usercon['service']}
login_Purl = "http://u16.cicihappy.com/ogame/login.php"
html_data = res.post(login_Purl,data=postdata,headers=headers('post'))
html_data.encoding = 'gbk'
if not html_data.text.find('src="leftmenu.php"'):
    print "尝试登录失败，请查找原因。"
    exit()
login_html=usercon['geturl']+usercon['getfile']
login_Ref = login_html
html_txt = res.get(login_html,headers=headers('get'))
html_txt.encoding = 'gbk'
html_data = html_txt.text
laft_lan_url=laft_lan(html_data)
tmp = get_laft_lan('gk')


