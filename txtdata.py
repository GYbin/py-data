#!/usr/bin/python
#-*- coding: UTF-8 -*-
import re
import os
import sys

#pydir = os.getcwd()
#print pydir
txt_path=r'./data_txt'
txt_name=os.walk(txt_path)
for file_data in txt_name:
    print file_data
