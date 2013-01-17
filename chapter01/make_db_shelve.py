'''
Created on 2013. 1. 15.

@author: stmkmk
'''
from init_data import tom, bob
import shelve

dbfilename = 'people-shelve'

def storeDbase(db, dbfilename=dbfilename):
    db = shelve.open(dbfilename)
    db['tom'] = tom
    db['bob'] = bob
    db.close()
    
def loadDbase(dbfilename=dbfilename):
    db = shelve.open(dbfilename)
    return db

if __name__ == '__main__':
    db = loadDbase()
    for key in db:
        print(key + '=>' + repr(db[key]))
    
