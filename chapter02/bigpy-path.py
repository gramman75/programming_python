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

for dir in pythonPath:
    for (thisDir, subsHere, filesHere) in os.walk(dir):
        
        try:
            print(thisDir)
        except UnicodeEncodeError:
            print(thisDir.encode())
            
        
        thisDir = os.path.normcase(thisDir)
        if thisDir in visited:
            continue
        else:
            visited.append(thisDir)
        
        for file in filesHere:
            if file.endswith('.py'):
                fullName = os.path.join(thisDir,file)
                fileSize = os.path.getsize(fullName)                
                fileLine = len(open(fullName,'rb').readlines())
                allFile.append( (fileSize, fileLine,fullName))               


allFile.sort()
print(allFile[-2:])

allFile.sort(key= lambda x : x[1])
print(allFile[-2:])