'''
Created on 2013. 1. 24.

@author: stmkmk
'''
import os, threading
from multiprocessing import Process, Lock, Pipe
count = 0

def counter(pipeout):
    global count
    count = count + 1
    os.write(pipeout, 111)
    
if __name__=='__main__':
    pipein, pipeout = Pipe()
    
    p = Process(target=counter, args=(pipeout,))
    #p = threading.Thread(target=counter, args=())
    p.start()
    line = os.read(pipein, 32)
    p.join()
    print(line)



'''
import os
from multiprocessing import Process, Lock

def whoami(label, lock):
    with lock:
        print('[%s] => %s' %(os.getpid(), label))
        
if __name__ =='__main__':
    lock = Lock()
    whoami('Function Call', lock)
    
    p = Process(target=whoami, args=('spawned child', lock))
    p.start()
    p.join()
    
    for i in range(5):
        Process(target=whoami, args=(('run process %s' %i),lock)).start()
    
    with lock:
        print('Main process exit')
'''        