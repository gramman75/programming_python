'''
Created on 2013. 1. 16.

@author: stmkmk
'''
from person_start import Person, Manager
import shelve

dbfilename = 'people-class'

def storeDbase(dbfilename=dbfilename):
    tom = Person('Tom', 33, 1000)
    kim = Manager('Kim', 38, 2000)
    bob = Manager('Bob', 38, 3000)
    sue = Manager('Sue', 38, 4000)
    db = shelve.open(dbfilename)
    db['tom'] = tom
    db['kim'] = kim
    db['bob'] = bob
    db['sue'] = sue
    db.close()
    
def loadDbase(dbfilename=dbfilename):
    db=shelve.open(dbfilename)
    return db

if __name__=='__main__':
    storeDbase()
    db = loadDbase()
    for key in db:
        print(key+'=>'+str(db[key]))
    