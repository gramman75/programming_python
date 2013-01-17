'''
Created on 2013. 1. 16.

@author: stmkmk
'''
class Person:
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job
        
    def __str__(self):
        return '<%s => %s>' % (self.__class__.__name__, self.name)
    
class Manager(Person):
    def __init__(self, name, age, pay=0):
        Person.__init__(self, name, age, pay, 'Manager')
        
        
    
