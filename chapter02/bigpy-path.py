#-*- encoding:utf8 -*-

'''
Created on 2013. 1. 25.

@author: stmkmk
'''
import os, sys


try:
    pythonPath = sys.argv[1]
except IndexError:
    pythonPath = sys.path
    
allFile =[]
visited =[]

target = open('c:\\target.txt','w')

for dir in pythonPath:
    for (thisDir, subsHere, filesHere) in os.walk(r'D:\clearcase\stmkmk_view\ERP_OVS\Doc'):
        '''
        try:
            print(thisDir)
        except UnicodeEncodeError:
            print(thisDir.encode())
            
        '''
        thisDir = os.path.normcase(thisDir)
        if thisDir in visited:
            continue
        else:
            visited.append(thisDir)
        
        for file in filesHere:
            if file.endswith('.doc'):
                fullName = os.path.join(thisDir,file)
                fileSize = os.path.getsize(fullName)                
                #fileLine = len(open(fullName,'rb').readlines())
              
                
                #allFile.append( (fileSize, fileLine,fullName))         
                
                target.write(fullName+'\r')
        
        
                      


