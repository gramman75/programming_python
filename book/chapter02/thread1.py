'''
Created on 2013. 1. 22.

@author: stmkmk
'''
import _thread

def child(tid):
    print('Thread ID', tid)
    
def parent():
    i = 0;
    while True:
        i += 1
        _thread.start_new_thread(child,(i,))
        if input() == 'q':break
        
parent()                    