#!/usr/bin/python
#-*- coding: UTF-8 -*-

import socket
import re
import os
from datetime import datetime
import urldata
HOST = '' 
PORT = 9898 

def ifvale(data,if_data):#搜索列表中字符串，返回字符串位置
    num = 0
    num_list=[]
    for i in data :
        if data[num].find(if_data[0][2:]) > 0:
            num_list.append(str(num))
        num+=1
    return num_list
def postdata(data):#提取POST中提交的信息
    pattern = r"Content-Type: multipart/form-data; boundary=([\s|\S]{38})"
    match = re.findall(pattern,data)
    data_tmp = data.split('\r\n')
    match_num = ifvale(data_tmp,match)
    data_list = data.split(data_tmp[int(match_num[1])])
    #data_name = data_list[1].decode('utf-8')
    #:data_text = data_list[2].decode('utf-8')
    return  data_list[1],data_list[2]
def webhead(x):# 判断报头协议，
    headlist=x.split('\r\n')
    headone=headlist[0].split()
    if headone[0]=="GET":
        #return webheadurl(headone[1])
        return urldata.html_file(x)
    elif headone[0]=="POST":
        post_txt=postdata(x)
        print post_txt[0].decode('utf-8')
        print post_txt[1].decode('utf-8')
        return urldata.html_file(x)
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
    #http_response = openfile(htmlurl)
    http_response = htmlurl
#    print http_response
    client_connection.sendall(http_response)
    datatime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print client_address,datatime
    client_connection.close()

