'''
Created on 2013. 1. 29.

@author: stmkmk
'''
import sys, os, glob, time
from subprocess import Popen, PIPE

def debug(*args):
    print('[Trace] :',args)
    
def quiet(*args):
    pass    

trace = quiet

testDir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
forcegen = len(sys.argv) > 2

scriptDir = os.path.join(testDir,'Scripts','*.py')
trace(scriptDir)
testFiles = glob.glob(scriptDir)
testFiles.sort()
trace(testFiles)


numfail=0
print('Starting :', time.asctime())
for testPath in testFiles:
    testFile = os.path.basename(testPath)
    
    inFile = testFile.replace('py','in')
    inPath = os.path.join(testDir,'Inputs',inFile)
    inData = open(inPath,'rb').read() if os.path.exists(inPath) else b''
    
    argFile = testFile.replace('py','args')
    argPath = os.path.join(testDir,'Args',argFile)
    trace(argPath)
    argData = open(argPath).read() if os.path.exists(argPath) else ''
    
    outFile = testFile.replace('py','out')
    outPath = os.path.join(testDir,'Outputs',outFile)
    outPathBad = outPath+'.out'
    if os.path.exists(outPathBad): os.remove(outPathBad)
    
    errFile = testFile.replace('py','err')
    errPath = os.path.join(testDir,'Errors',errFile)
    if os.path.exists(errPath): os.remove(errPath)
    
    pypath = sys.executable
    command = '%s %s %s' %(pypath, testPath, argData)
    
    trace(command)
    
    process = Popen(command, shell=False, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    process.stdin.write(inData)
    process.stdin.close()
    
    outData = process.stdout.read()
    errData = process.stderr.read()
    exitstatus = process.wait()
    
    if exitstatus !=0:
        print('Error Status :', testFile, exitstatus)
        
    if errData:
        print('Error Stream :', testFile, errData)
        open(errPath,'wb').write(errData)
    
    if exitstatus or errData:
        numfail += 1
        open(outPathBad,'wb').write(outData)
    elif not os.path.exists(outPath) or forcegen:
        print('generating :', outPath)
        open(outPath,'wb').write(outData)
    else:
        priorout = open(outPath,'rb').read()
        if priorout == outData:
            print('passed:', testFile)
        else:
            numfail +=1
            print('Failed Output :',testFile)
            open(outPathBad,'wb').write(outData)
            
print('Finished : ', time.asctime())            
print('%s tested, %s test is failed' %(len(testFiles),numfail))            
        