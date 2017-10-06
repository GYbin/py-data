#!/usr/bin/python
#-*- coding: UTF-8 -*-

import socket
import re
import os
from datetime import datetime
HOST = '' 
PORT = 9898 

def openfile(x):
    of = open(x,'r')
    of_text=of.read()
   # print of_text
    return of_text

def webheadurl(x):
    #print x
    if x== "/":
        headurl = "." + x + "inx.html"
    else:
        headurl = "."+x
    return headurl

def postdata(data):#提取POST中提交的信息
    post_list = data.split('\n')
    post_key = post_list[4][-20:-1]
    pattern = r"Content-Disposition: form-data; name=([\s|\S]*?)"+post_key
    match = re.findall(pattern,data)
   # print match
    data_name = match[0].decode('utf-8')
    data_text = match[1].decode('utf-8')
    textname = data_name.split('\r\n')
    return  textname[2]
def webhead(x):# 判断报头协议，
    headlist=x.split('\r\n')
    headone=headlist[0].split()
    if headone[0]=="GET":
        return webheadurl(headone[1])
    elif headone[0]=="POST":
        postdata(x)
        return "./inx.html"
    else:
        print "提交错误"
        return '-1'

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#AF_INET（又称 PF_INET）是 IPv4 网络协议的套接字类型，AF_INET6 则是 IPv6 的
#SOCK_STREAM   是有保障的（即能保证数据正确传送到对方）面向连接的SOCKET,是基于TCP的
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#S.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 这里value设置为1
#SO_REUSEADDR 当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。
#通常来说，只有经过系统定义一段时间后，才能被重用。
listen_socket.bind((HOST, PORT))

listen_socket.listen(10)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    if request == 'e':
        break
    elif not request :
        continue
    htmlurl = webhead(request)
    http_response = openfile(htmlurl)
    client_connection.sendall(http_response)
    datatime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print datatime
    client_connection.close()

