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
    global yhzzxq
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
    yhzzxq['laft_url'] = laft_url
    return 0

def get_laft_lan(laft_data):#打开侧边栏地址，返回html页面
#    if not isinstance(laft_url_dict,dict):
#        print "传入写入参数需要使用Dict类型"
    time.sleep(2)
    global login_Ref
    url_tmp=usercon['geturl']+laft_data
    #usercon['geturl'] 地址前缀
    login_Ref = url_tmp
    print "打开URL：",url_tmp
    html_txt = res.get(url_tmp,headers=headers('get'))
    html_txt.encoding = 'gbk'
    return html_txt.text

def get_laft_lanjz(get_html):#获取建筑信息
    pattern = r'<option selected="selected" value="(.*?)">(.*?)&nbsp;\[(.*?)\]&nbsp;&nbsp;</option>'
    xqgk_tmpwz = re.findall(pattern,get_html)#获取星球位置信息
    print '当前星球位置：'+xqgk_tmpwz[0][2],'名称:' + xqgk_tmpwz[0][1]
    for xqname in yhzzxq:
        if yhzzxq.get(xqname).get('xqwz')==xqgk_tmpwz[0][2] and yhzzxq.get(xqname).get('xqname')==xqgk_tmpwz[0][1]:
            print '当前星球:'+ xqname
            break
    pattern = r'<td class="l">(.*?)ont></a></td>'
    zyjz_tmp = re.findall(pattern,get_html,re.S)
    for zyjz_tmpxx in zyjz_tmp:
        pattern = r'href="infos.php\?gid=(.*?)">(.*?)</a> \((.*?)\)<br>'
        zyjz_list = re.findall(pattern,zyjz_tmpxx)
        if not zyjz_list:
            continue
        print zyjz_list[0][1],zyjz_list[0][2]
        pattern = r'<td class="k".*?href="(.*?)"><.*?>(.*?)</f' #升级链接
        zyjz_sjljurl = re.findall(pattern,zyjz_tmpxx)
        print '升级链接:'+zyjz_sjljurl[0][0]
#        pattern = r'span.*?>(.*?)</span>.*?span.*?>(.*?)</span>'#需要多少资源
        pattern = r'<br>.*?style=.*?>(.*?)</b>.*?style=.*?>(.*?)</b>'#剩余资源
        zyjz_zysytmp = re.findall(pattern,zyjz_tmpxx)
        if not ifziyuanfs(zyjz_zysytmp[0])==0:
            print '资源不够'
            continue
        print '可以升级'

def ifziyuanfs(tmp):#判断是否都是正数
    for ifzy in tmp:
        if not int(ifzy.strip().replace(',','')) >= 0:
            return -1
    return 0


def yhhs_confread_jz(): #读取建筑配置信息
    ConfigFile = "yhzz16.cf"
    configList = ('yhjz_jsm','yhjz_jtm','yhjz_zqm','yhjz_nlm')
    yhzz_jm_zym = ybpy_tool.conf_read(configList,ConfigFile)
    return yhzz_jm_zym

def yhhs_fxxq(get_html):#发现星球
    pattern = r'<option [selected="selected" ]*value="(.*?)">(.*?)&nbsp;\[(.*?)\]&nbsp;&nbsp;</option>'
    xqgk_tmp = re.findall(pattern,get_html)
    global yhzzxq
    numtmp = 0
    print '发现星球：'
    for xqgk_tmpzl in xqgk_tmp:
        numtmp = numtmp+1
        xqname = 'xq'+str(numtmp)
        yhzzxq[xqname]={'xqwz':xqgk_tmpzl[2],'xqname':xqgk_tmpzl[1],'xqline':xqgk_tmpzl[0]}
        print '位置:'+xqgk_tmpzl[2],'名称：'+xqgk_tmpzl[1],'链接：'+xqgk_tmpzl[0]
    return 0

def yhhs_xqgk(get_html):#获取概况
    pattern = r'<div id="[metalx|crystalx|deuteriumx]*"[><font color="#ff0000"]*>(.*?)<[/font><]*/div></td>'
    zy_tmp = re.findall(pattern,get_html)#获取资源信息
    pattern = r'<div id="deuteriumx".*?align="center" width="140"[><font color="#ff0000"]*>(.*?)<[/font><]*/td>.*?<font color="lime">(.*?)</font></td>'
    nl_tmp = re.findall(pattern,get_html,re.S)#获取能量和暗物质
    pattern = r'textContent\[1\].*?\\"#\\">(.*?)  \(<a.*?">(.*?)</a>.*?>(.*?)<'
    xqgk_tmpdq = re.findall(pattern,get_html)#当前星球
    pattern = r'textContent\[5\].*?\[(.*?)\]'
    xqgk_tmpwz = re.findall(pattern,get_html)#获取星球位置信息
    print '当前星球位置：'+xqgk_tmpwz[0]
    print '当前星球大小:'+xqgk_tmpdq[0][0],'使用率'+xqgk_tmpdq[0][1],'最大空间'+xqgk_tmpdq[0][2]
    print "金属："+zy_tmp[0],"晶体："+zy_tmp[1],"重氢："+zy_tmp[2]
    print "能量："+nl_tmp[0][0],"暗物质："+nl_tmp[0][1]
    return 0

postdata = {'v':'2','username':usercon['username'],'password':usercon['passwd'],'universe':usercon['service']}
login_Purl = "http://u16.cicihappy.com/ogame/login.php"
#tmp_a = 0
#while tmp_a >= 2:
#    tmp_a = tmp_a + 1
#    html_data = res.post(login_Purl,data=postdata,headers=headers('post'))
#    if not html_data.text.find('src="leftmenu.php"'):
#        print "尝试登录失败，请查找原因。"
#        time.sleep(2)
#        if tmp_a >= 2
#            exit()
#    else :
#        break
html_data = res.post(login_Purl,data=postdata,headers=headers('post'))
html_data.encoding = 'gbk'
if not html_data.text.find('src="leftmenu.php"'):
    print "尝试登录失败，请查找原因。"
    exit()
login_html=usercon['geturl']+usercon['getfile']
login_Ref = login_html
html_txt = res.get(login_html,headers=headers('get'))#开打游戏第一页
html_txt.encoding = 'gbk'
html_data = html_txt.text
laft_lan_url=laft_lan(html_data)#获取侧边栏。
tmp = get_laft_lan(yhzzxq['laft_url']['gk'])#打开概况
yhhs_fxxq(tmp)#获取发现星球列表
yhhs_xqgk(tmp)#获取当前星球概况信息
tmp = get_laft_lan(yhzzxq['laft_url']['jz'])#获取建筑界面
get_laft_lanjz(tmp)#获取建筑信息



