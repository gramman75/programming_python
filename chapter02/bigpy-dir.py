'''
Created on 2013. 1. 25.

@author: stmkmk
'''
import glob, os, sys

if sys.platform.startswith('win'):
    dirname = r'c:\python33\lib'
else:
    dirname = '/usr/lib/python'
    
allsizes =[]        

for (thisDir, subsHere, filesDir) in os.walk(dirname):
    for file in filesDir:
        if file.endswith('.py'):
            fullName = os.path.join(thisDir,file)
            fileSize = os.path.getsize(fullName)
            allsizes.append((fileSize, fullName))

allsizes.sort()

print(allsizes[-2:])
        
    