'''
Created on 2013. 1. 29.

@author: stmkmk
'''

import os, sys, time

maxfileload = 1000000
blksize = 1024 * 500
fcount = 0
dcount = 0

def copyFile(pathFrom, pathTo, maxfileload = maxfileload):
    print('Copying...',pathFrom, 'to', pathTo)
    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom,'rb').read()
        open(pathTo,'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom,'rb')
        fileTo = open(pathTo,'wb')
        while True:
            blkFrom = fileFrom.read(blksize)
            if not blkFrom: break
            fileTo.write(blkFrom)
    
def copyTree(dirFrom, dirTo):
    fcount = dcount = 0
    lists = os.listdir(dirFrom)

    for list in lists:
        pathFrom = os.path.join(dirFrom, list)
        pathTo = os.path.join(dirTo, list)
        
        if not os.path.isdir(pathFrom):
            try:
                copyFile(pathFrom, pathTo)
                fcount += 1
            except:
                print('Error : copy from', pathFrom, 'to', pathTo)
        else:
            if not os.path.exists(pathTo):
                try:
                    os.mkdir(pathTo)
                except:
                    print('Fail to create directory ', pathTo)
            before = copyTree(pathFrom, pathTo)
            fcount += before[0]
            dcount += before[1]
            dcount +=1
        
    return (fcount,dcount)


def getArgs():
    try:
        dirFrom, dirTo = sys.argv[1:]
    except:
        print('Use : cpall from-direcotyr to-directory')
    else:
        if not os.path.exists(dirFrom):
            print('Error : from-directory is not directory')
        elif not os.path.exists(dirTo):
            try:
                os.mkdir(dirTo)
            except:
                print('Error : can not make to-Directory')
        else:
            print('Warning : to-dir already exists')
            if hasattr(os.path, 'samefile'):
                same = os.path.samefile(dirFrom, dirTo)
            else:
                same = os.path.abspath(dirFrom) == os.path.abspath(dirTo)
            
            if same:
                print('Error: dir-from same sa dir-To')
            else:
                return (dirFrom, dirTo)
                

if __name__ =='__main__':
    dirtuple = getArgs()
    if dirtuple:
        print('copying...')
        start = time.clock()
        fcount, dcount = copyTree(*dirtuple)
        
    print('copy file : ',fcount, 'copy directory :', dcount, 'elapsed time ', time.clock()-start)
        