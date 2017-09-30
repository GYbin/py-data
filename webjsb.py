#!/usr/bin/python
#-*- coding: UTF-8 -*-

import socket
HOST = '' 
PORT = 9898 
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
 
    http_response = """
	HTTP/1.1 200 OK
 
	Hello, World!
	"""
    client_connection.sendall(http_response)
    client_connection.close()

