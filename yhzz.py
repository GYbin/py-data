#!/usr/lib/python
# -*- coding: utf-8 -*-

#import requests
#import sys
#import os

postdata = {'v':'2','username':'lib','password':'pasd','universe':'u11.cicihappy.com'}
posturl = 'http://u11.cicihappy.com/ogame/login.php'
r = requests.post(posturl,data=postdata)
print r.text

