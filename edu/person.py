'''
Created on 2013. 4. 8.

@author: stmkmk
'''
class Person:
    def __init__(self, name, job, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def tax(self):
        return self.pay * 0.10
    
    def info(self):
        return self.name, self.job, self.pay, self.tax()
    
    
        
