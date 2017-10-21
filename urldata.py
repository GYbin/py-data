#!/usr/bin/python
#-*- coding: UTF-8 -*-

import re
import os
html_enter = "\n"

def html_ask():
    htmltou="""HTTP/1.1 200 OK
#Date: Sat, 31 Dec 2005 23:59:59 GMT
Content-Type:text/html; charset=utf-8
#Content-Length: 12200

"""
    return htmltou

def html_biaodan(post_service = "yabin.zgdgz.org:9898"):
    post_id = "usrfrom"
    text_name = "煎蛋"
    text_data = "Text_Text"
    bd="""    <form action="http://%s" method="post" enctype="multipart/form-data"id="%s">
        <p>FileName: <input type="text" name="name" value="%s"/> <input type="submit" value="Submit"></p>
        <textarea cols="60" rows="10" name="text" form="%s"> %s </textarea><br/>
    </form>
""" %(post_service,post_id,text_name,post_id,text_data)
    return bd

def html_tou():
    html_a = '''<html lang="zh-CN" xml:lang="zh-CN">''' + html_enter
    html_b = '''</html>'''+ html_enter
    return html_a,html_b

def html_head(headname="JDJSB"):
    head = """<meta http-equiv=Content-Type content="text/html; charset=utf-8" />
<head>
    <meta charset="UTF-8">
    <title>%s</title>
<style>
#header {
    background-color:black;
    color:white;
    text-align:center;
    padding:5px;
}
#nav {
    line-height:30px;
    background-color:#eeeeee;
    height:300px;
    width:100px;
    float:left;
    padding:5px;	      
}
#section {
    width:350px;
    float:left;
    padding:10px;	 	 
}
#footer {
    background-color:black;
    color:white;
    clear:both;
    text-align:center;
   padding:5px;	 	 
}
</style>
</head>
""" %(headname)
    return head

def html_body():
    body = """<body>

<div id="header">
<h1>JDJSB</h1>
</div>

<div id="nav">
London<br>
Paris<br>
Tokyo<br>
</div>

<div id="section">
<h2>记事本正文</h2>
%s
</div>

<div id="footer">
By:GYB
</div>
</body> %s """ %(html_biaodan(),html_enter)
    return body

def favicon_ico():
    htmltou="""HTTP/1.1 200 OK
#Date: Sat, 31 Dec 2005 23:59:59 GMT
Content-Type: text/html;：::q
charset=ISO-8859-1
Content-Length: 122

""" 
    return htmltou


def html_file(x):
    headlist=x.split('\r\n')
    headone=headlist[0].split()
    print headlist
    if headone[1]== "/":
        headadd =  headlist[5].split()
        print headadd
        return html_ask()+html_tou()[0]+html_head()+html_body()+html_tou()[1]
    else:
        return favicon_ico()
#print htmldata
'''def html_post(x):
    headlist=x.split('\r\n')
    headone=headlist[0].split()
    print headlist
    if headone[1]== "/":
        headadd =  headlist[7].split()
        print headadd
        return html_ask()+html_tou()[0]+html_head()+html_body(headadd[1])+html_tou()[1]
    else:
        return favicon_ico()
'''

