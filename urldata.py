#!/usr/bin/python
#-*- coding: UTF-8 -*-

import re
import os
html_enter = "\n"

def html_ask():
    htmltou="""HTTP/1.1 200 OK
Date: Sat,31 Dec 2015 23:59:59 GMT
Content-Type:text/html;charset=utf-8
Content-Length: 12200


"""
    return htmltou
def html_tou():
    html_a = '''<html lang="zh-CN" xml:lang="zh-CN">''' + html_enter
    html_b = '''</html>'''+ html_enter
    return html_a,html_b
def html_head(headname="JDJSB"):
    meta = '''<meta http-equiv=Content-Type content="text/html; charset=utf-8" />'''+ html_enter
    head = """<head>
    <meta charset="UTF-8">
    <title>%s</title> %s </head> %s""" %(headname,html_enter,html_enter)
    return meta+head
def html_body():
    post_service = "http://yabin.zgdgz.org:9898"
    post_id = "usrfrom"
    text_name = "Text_Name"
    text_data = "Text_Text"
    body = """<body>
    <form action="%s" method="post" enctype="multipart/form-data"id="%s">
        <p>FileName: <input type="text" name="name" value="%s"/> <input type="submit" value="Submit"></p>
        <textarea cols="60" rows="10" name="text" form="%s"> %s </textarea><br/>
    </form>
</body> %s """ %(post_service,post_id,text_name,post_id,text_data,html_enter)
    return body

def html_file():
    return html_ask()+html_tou()[0]+html_head()+html_body()+html_tou()[1]
#print htmldata















