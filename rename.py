#!/usr/lib/python
# -*- coding: utf-8 -*-
#家装照片处理
import os
import sys
import re
dirusr = './'
oslist = os.listdir(dirusr)
patter = r'\.jpg'


###### 遍历l目录
for dirpath,dirnames,filenames in os.walk(path):
    for file in filenames:
        fullpath=os.path.join(dirpath,file)
        jpg = fullpath[-8:]
        if re.findall(patter,jpg)
           if
            print fullpath

###################################
for mlname in oslist: #修改名称
    print mlname
    namelist = mlname.split("平")
    namelist[0] = namelist[0].strip()
    newname = namelist[0] + 'pm'
    os.rename(mlname,newname)


###################
a = 0  ##移动文件
oslist = os.listdir(dirusr)
for mlanme in oslist:
    filelist = os.listdir(dirusr+mlanme+'/')
    for filename in filelist :
        jpg = filename[-8:]
        if re.findall(patter,jpg):
             a = 1  #查找到顶文件
    if a == 1 : #查找到后执行操作
        a = 0  #还原到之前状态
        os.mkdir(dirusr+mlanme+'/'+"1")
        for filename in filelist:
            if re.findall(patter,jpg):
                os.rename(dirusr+mlanme+'/'+filename,dirusr+mlanme+'/'+ '1/'+filename)

########################################

#从另一目录向该目录复制
def bjml(mllist,ifname):#比较lm目录
    for bjaa in mllist :
        if bjaa == ifname:
           return 0
    return -1

tmplist = os.listdir(dirusr+'tmp/')
for mlname in tmplist:
    infotmp = mlname.split("平")
    try :
        int(infotmp[0])
    except :
        print "目录错误"
        continue
    nuwname = infotmp[0]+'pm' #新目录名称
    flist = os.listdir(dirusr)
    if bjml(flist,nuwname):
        os.mkdir(dirusr+nuwname+"/")
        os.rename(dirusr+'tmp/'+ mlname,dirusr+nuwname+"/"+"1")
        continue
    abc = os.listdir(dirusr+nuwname+'/')
    file_num =  len(abc)+1
    os.rename(dirusr+'tmp/'+ mlname,dirusr+nuwname+'/'+str(file_num))


######################################
#修改文件名称
patter = "\.jpg"
oslist = os.listdir(dirusr)
for mlanme in oslist:
    sqlist = os.listdir(dirusr+mlanme+'/')
    for nlanme in sqlist:
        fname = os.listdir(dirusr+mlanme+'/'+nlanme+'/')
        namenum = 1
        for faname in fname:
            if re.findall(patter,faname):
                oldurl = dirusr+mlanme+'/'+nlanme+'/'
                nuwname = oldurl+mlanme+'_'+nlanme+'_'+str(namenum)+".jpg"
                os.rename(oldurl+faname,nuwname)
                namenum += 1
------------------------------------------------



def TXWJ(GJZ = '欧'):

GJZ = r'\d*平.*'
bsdir = './BieShu/'
oslist = os.listdir(bsdir)
for mlanme in oslist:
    xdname = re.findall(GJZ,mlanme)
    if xdname:
            os.rename(bsdir+mlanme,'./tmp/'+mlanme)

#######################################################
#挑选文件
def TXWJ(GJZ = '欧'):
    bsdir = './BieShu/'
    oslist = os.listdir(bsdir)
    for mlanme in oslist:
        xdname = re.findall(GJZ,mlanme)
        if xdname:
            os.rename(bsdir+mlanme,'./tmp/'+mlanme)

--------------------------------
修改目录名字

def XGMLM(GJZ = 'XianDJY'):
    a = 1
    bsdir = './BieShu/'
    oslist = os.listdir(bsdir)
    for mlanme in oslist:
        openfl = open(bsdir+mlanme+'/'+mlanme+".txt","a+")
        openfl.close()
        os.rename(bsdir+mlanme,bsdir+GJZ+'_'+str(a))
        a += 1


-------------------------
修改文件名字
def XGMZ():
    a = 0
    patter = "\.jpg"
    bsdir = './BieShu/'
    oslist = os.listdir(bsdir)
    for mlanme in oslist:
        emlname = os.listdir(bsdir+mlanme+'/')
        a = 1
        for emlist in emlname :
            xdname = re.findall(patter,emlist)
            if xdname:
                nwenaue = bsdir+mlanme+'/'+mlanme+'_'+str(a)+".jpg"
                os.rename(bsdir+mlanme+'/'+emlist,nwenaue)
                a += 1




