'''
Created on 2013. 1. 23.

@author: stmkmk
'''
import time

start = time.time()

for i in range(10):
    for j in range(100):
        print('[%s] => %s' %(i,j))
        
print('Elapsed time :%s' %(time.time() - start))         