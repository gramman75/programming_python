'''
Created on 2013. 1. 28.

@author: stmkmk
'''
import sys, os

kilobyte = 1024
megabyte = kilobyte * 1000
chunkSize = int(1.4 * megabyte)

def split(fromFile, toDir, chuckSize):
    if os.path.exists(toDir):
        q = input('Delete all file %s(y/n) ?' %toDir)
        if q.upper() =='Y':
            for file in os.listdir(path=toDir):
                os.remove(os.path.join(toDir,file))
        else:
            return
    else:
        os.mkdir(toDir)
    
    partNum = 0
    readFile = open(fromFile,'rb')
    while True:
        chuck = readFile.read(chuckSize)
        if not chuck: break
        partNum += 1
        fileObj = open(os.path.join(toDir,('part%04d'%partNum)),'wb')
        fileObj.write(chuck)
        fileObj.close()
    readFile.close()
    return partNum

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            fromFile = input('FileName ?')
            toDir = input('To Dir ?')
            interactive = True
        else:
            interactive = False
            fromFile, toDir = sys.argv[1:3]
            if len(sys.argv) == 4 : chunkSize = sys.argv[3]
        absFrom, absTo = map(os.path.abspath, [fromFile, toDir])
        
        print('Spliting', absFrom, 'to', absTo, 'by', chunkSize)
        
        try:
            parts = split(fromFile, toDir, chunkSize)
        except:
            print('Error during split')
            #print(sys.exc_info()[0], sys.exc_info()[1])
            print(sys.exc_info())
        else:
            print('split finished ', parts,'to', toDir )
            
        
        
        
        
          
            
