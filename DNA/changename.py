#-*- encoding:utf8 -*-
'''
Created on 2013. 4. 16.

@author: stmkmk
'''
import sys, os, glob

ROOT_DIR =r"D:\t"
#ROOT_DIR = r"D:\t"

filelist = glob.glob(os.path.join(ROOT_DIR,'*.pck"
file in filelist:
    fileName = ",".join(file.split(".")[:-1])+".pls"
    print file
    print fileName
    os.rename(file, os.path.join(ROOT_DIR,fileName))
