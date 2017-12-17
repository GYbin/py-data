#!/usr/lib/python
# -*- coding: utf-8 -*-
import sqlite3
import os
import sys
import logging
sys.path.append('./ybpy_tool/')
import ybpy_tool
ybpy_tool.log_config()

def find_sqltable(sqlcur,tabname):#判断是否有表
    cmd = 'SELECT name FROM sqlite_master WHERE name = "%s"' %tabname
    ybpy_tool.logger.debug('查询命令:%s',cmd)
    tablelist = sqlcur.execute(cmd).fetchall()
    for tname in tablelist:
        try:
           iftab = tname.index(tabname)
        except:
           iftab = -1
        if not iftab == -1 :
           return 0
    return -1

def find_sqlname(sqlcur,tabname):#查询Email_Ser 表中是否有数据
    cmd ='SELECT rowid FROM Email_Ser Where Etxt="%s"' %tabname
    tablelist = sqlcur.execute(cmd).fetchall()
    if tablelist:
        return 0 , tablelist
    else:
        return -1 ,cmd

def ftab_data(sqlcur,tabname):
    cmd = 'SELECT %s FROM %s Where %s="%s"'%(tabname[0],tabname[1],tabname[2],tabname[3])
    tablelist = sqlcur.execute(cmd).fetchall()
    if tablelist:
        return 0,tablelist
    else:
        return -1,cmd

def add_sqltable(sqlcur,tabname,content): # 创建表
     cmd = 'CREATE TABLE %s(%s)'%(tabname,content)
     iftab = 0
     try:
        dis = sqlcur.execute(cmd).fetchall()
     except:
        iftab = -1
     if not iftab == -1:
        return 0
     else:
        return -1

def ins_name(sqlcur,valuse):#添加记录
    cmd = 'INSERT INTO %s (%s) VALUES (%s)' %(valuse[0],valuse[1],valuse[2])
    iftab = 0
    try:
        dis = sqlcur.execute(cmd).fetchall()
    except:
        iftab = -1
    if not iftab == -1:
        return 0 , dis
    else:
        return -1 , cmd
def update_data(sqlcur,valuse):
    cmd = 'UPDATE %s SET %s = "%s" WHERE %s = "%s" '\
           %(valuse[0],valuse[1],valuse[2],valuse[3],valuse[4])
    iftab = 0
    try:
        dis = sqlcur.execute(cmd).fetchall()
    except:
        iftab = -1
    if not iftab == -1:
        return 0 , dis
    else:
        return -1 , cmd

dir_db = './db/'
dir_log = './log/'
dir_error =  './error/'
dir_data = './data/'
error_file = './errlinke.txt'
file_LYname = 'LY.txt'
emconn = sqlite3.connect(dir_db + 'Yb_Email.db')
paconn = sqlite3.connect(dir_db + 'Yb_Passwd.db')
daconn = sqlite3.connect(dir_db + 'Yb_Data.db')
emcur = emconn.cursor() #email 数据打开
pacur = paconn.cursor() #passwd 数据打开

if find_sqltable(emcur,'Email_Ser'):
    add_stab = 'ETxt TEXT NOT NULL , SerLink VARCHAR(12),Unum VARCHAR(12)'
    if add_sqltable(emconn,'Email_Ser',add_stab):
        print "数据表建立失败"


filelist = ybpy_tool.get_fname(file_LYname,dir_data)
dataLY = ybpy_tool.conf_read(['LY'],file_LYname,dir_data) #设置来源
LY = dataLY['LY'].decode('utf-8')
data_line = "1"
a = 0
b = 0
while data_line :
    if data_line == -1 or data_line == 0:
       break
    data_line = ybpy_tool.file_rline(dir_data+filelist[0][0])
    data_lines = data_line.strip()
    data_linspl = data_lines.split('\t')
    if ybpy_tool.chec_code({'passwd':data_linspl[1],'email':data_linspl[0]}):
        ybpy_tool.file_write(data_line,error_file)  #错误行写入
        continue
    email_list = data_linspl[0].split('@') #分解email和passwd
    email_list[1] = email_list[1].lower()
    emfind_info = 'rowid,SerLink',"Email_Ser" ,'ETxt',email_list[1]
    emser_info = ftab_data(emcur,emfind_info)
    if  emser_info[0] :
        emins_info = 'Email_Ser','ETxt','"%s"' %(email_list[1])
        emser_info = ins_name(emcur,emins_info)
        if emser_info[0]:
            print "插入数据失败"
            break
        emser_info = ftab_data(emcur,emfind_info)
        if not emser_info[1][0][1] :
            tmp = 'E'+ str(emser_info[1][0][0])
            emupdata_info = 'Email_Ser','SerLink',tmp ,'rowid',emser_info[1][0][0]
            emser_info = update_data(emcur,emupdata_info)
            if emser_info[0] :
                 print "插入数据失败"
                 break
            emser_info = ftab_data(emcur,emfind_info)
        if find_sqltable(emcur,emser_info[1][0][1]):
            add_stab = 'UserNam  VARCHAR(24) NOT NULL,SerLJ VARCHAR(12) NOT NULL,Passwd TEXT,LY NTEXT'
            if add_sqltable(emconn,emser_info[1][0][1],add_stab):
                print "表建立失败"
                break

#    emserinfo = find_sqlname(emcur,eminfo[0])
    emfind_info = 'rowid,Passwd,LY',emser_info[1][0][1] ,'UserNam',email_list[0]
    tableinfo = ftab_data(emcur,emfind_info)
    if tableinfo[0] :
        emins_info = emser_info[1][0][1],'UserNam,SerLJ,LY','"%s","%s","%s"' %(email_list[0],emser_info[1][0][1],LY)
        if ins_name(emconn,emins_info)[0]:
            print "错误"

    a += 1
    b += 1
    print a
    if b >= 1000:
        b = 0
        emconn.commit()
print "结束"


#############密码处理##############

def add_email_tabl(cur,tab_name):
    cmd = 'CREATE TABLE %s
    (Name TEXT NOT NULL,
    Sid INT(16) NOT NULL,
    LY TEXT NOT NULL)'%tab_name
    cur.execute(cmd)
    cur.commit()
def emailif(cur,email):
    mailsp = email.split('@')
    cmd = 'SELECT rowid,ETxt,SerLink FROM Email_Ser Where Etxt="%s"' %mailsp[1]
    tmp = cur.execute(cmd).fetchall()
    if len(tmp)>2:
       添加记录
    else:
       添加表单
       添加记录


