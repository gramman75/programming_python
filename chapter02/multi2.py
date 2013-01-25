'''
Created on 2013. 1. 24.

@author: stmkmk
'''
from multiprocessing import Process, Pipe
import time

def sender(pipe):
    pipe.send('ABC')
    pipe.close()
    
def talker(pipe):
    pipe.send('takler')
    reply = pipe.recv()
    print('talker reply %s' %reply)
    
if __name__=='__main__':
    parentEnd, childEnd = Pipe()
    Process(target=sender, args=(childEnd,)).start()
    reply = parentEnd.recv()
    print('parent recv %s' %reply)
    parentEnd.close()
    
    parentEnd, childEnd = Pipe()
    p = Process(target=talker, args=(childEnd,))
    p.start()
    reply = parentEnd.recv()
    print('parent recv %s' %reply)
    
    parentEnd.send('parent send')
    p.join()
    print('parent exit')