
'''
Created on 2013. 1. 25.

@author: stmkmk
'''
from multiprocessing import Process, Value, Array
import os

procs = 3
count = 0

def showdata(label, val, arr):
    global count
    msg = '%-12s : pid = %s , count = %s, val = %s, array = %s'
    print(msg %(label, os.getpid(),count, val.value, list(arr)))
    
def updater(val, arr):
    global count
    count += 1
    val.value += 1
    for i in range(3):arr[i] +=1
    
if __name__=='__main__':
    scalar = Value('i',0)
    vector = Array('d', procs)
    
    #Parent Process에서 수행
    showdata('parent', scalar, vector)
    
    #child Process에서 수행
    p = Process(target = showdata, args=('child',scalar, vector))
    p.start()
    p.join()
    
    # Process를 하나씩 순서대로 수행
    print('\nProcess 순차 수행')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=showdata, args=('child %s' %i, scalar, vector))
        p.start()
        p.join()
    showdata('parent', scalar, vector)
        
    # Process를 병렬로 수행
    print('\nProcess 병렬 수행')
    ps =[]
    for i in range(procs):
        count += 1
        scalar.value +=1
        vector[i] += 1
        p = Process(target=showdata, args=('child %s' %i, scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    
    # Child Process에서 순차처리 Update
    print('\nChild Process에서 순차처리 Update')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
    showdata('parent', scalar, vector)
    
    # Child Process에서 병렬처리 Update
    print('\nChild Process에서 병렬처리 Update')
    ps =[]
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    showdata('parent', scalar, vector)
        
    
        