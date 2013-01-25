'''
Created on 2013. 1. 23.

@author: stmkmk
'''
import threading, time
count = 0

def adder():
    global count
    count = count + 1
    time.sleep(.5)
    count = count + 1
    #print(count)

threads = []    
for i in range(100):
    thread = threading.Thread(target = adder, args=())
    thread.start()
    threads.append(thread)
    
for thread in threads:
    thread.join()
    
print(count)            