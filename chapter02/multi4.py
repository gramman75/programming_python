'''
Created on 2013. 1. 25.

@author: stmkmk
'''
import time, os, queue
from multiprocessing import Process, Queue

class Counter(Process):
    def __init__(self, start, queue):
        self.state = start
        self.post  = queue
        Process.__init__(self)
        
    def run(self):
        for i in range(3):
            #time.sleep(1)
            self.state+= 1
            print('child put %s %s' %(self.pid, self.state))
            self.post.put([self.pid, self.state])
        print('child %s end' %os.getpid())

if __name__=='__main__':
    print('start %s' %os.getpid())
    
    expected = 9
    
    post = Queue()
    p = Counter(0,post)
    q = Counter(10,post)
    r = Counter(100,post)
    
    p.start()
    q.start()
    r.start()
    
    
    p.join()
    q.join()
    r.join()
    
       
    while expected:
    
        try:
            data = post.get(block=False)
        except queue.Empty:
            print('No data...')
        else:
            print('posted :',data)
            expected -=1
    
    
    print('end process %s' %os.getpid())
    
    
            
        
        