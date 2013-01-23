'''
Created on 2013. 1. 23.

@author: stmkmk
'''
import threading, time


class MyThread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)
    
    def run(self):
        for i in range(self.count):
            #time.sleep(1)
            print('[%s] => %s' %(self.getName(), i))            
start = time.time()
stdoutmutex = threading.Lock()
threads =[]
for i in range(10):
    thread = MyThread(i,100,stdoutmutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    
print('Elapsed time :%s' %(time.time() - start))    