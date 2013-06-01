'''
Created on 2013. 1. 28.

@author: stmkmk
'''
import os, sys


def join(fromDir, toFile):
    parts = os.listdir(fromDir)
    file = open(os.path.join(fromDir, toFile),'wb')
    for part in parts:
        partPath = os.path.join(fromDir, part)
        fileObj = open(partPath,'rb')
        
        while True:
            chunk = fileObj.read(1024)
            if not chunk: break
            file.write(chunk)
        fileObj.close()
    file.close()
    
if __name__ =='__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use : join.py [from-Dir to-File]')
    else:
        if len(sys.argv) !=3:
            fromDir = input('Directory containing parts file?')
            toFile = input('Name of file to be recreated?')
        else:
            fromDir, toFile = sys.argv[1:3]
        
        try:
            join(fromDir, toFile)
        except:
            print('Error joining part file')
            print(sys.exc_info()[0], sys.exc_info()[1])
        
        print(toFile,'is cratead at', fromDir)
        
            
        
        
        