'''
Created on 2013. 1. 23.

@author: stmkmk
'''
import _thread as thread
stdoutmutex = thread.allocate_lock()
exitmutexes = [thread.allocate_lock() for i in range(10)]

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' %(myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()

    
for i in range(10):
    thread.start_new(counter, (i,10))
    
for mutex in exitmutexes:
    while not mutex.locked():pass
    
print('main thread exiting.')        