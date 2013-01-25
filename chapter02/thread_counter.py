'''
Created on 2013. 1. 22.

@author: stmkmk
'''

import _thread as thread, time
def counter(myId, count): # function run in threads
    for i in range(count):
        time.sleep(1)
        mutex.acquire()
        print('[%s] => %s' % (myId, i))
        mutex.release()
            
mutex = thread.allocate_lock()            
for i in range(5): # spawn 5 threads
    thread.start_new_thread(counter, (i, 5)) # each thread loops 5 times

time.sleep(6)
print('Main thread exiting.') # don't exit too early 