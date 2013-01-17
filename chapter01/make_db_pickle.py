'''
Created on 2013. 1. 15.

@author: stmkmk
'''
import pickle
dbfilename = 'people-pickle'

def storeDbase(db, dbfilename=dbfilename):    
    file = open(dbfilename, 'wb')
    pickle.dump(db, file)
    file.close()
    
def loadDbase(dbfilename=dbfilename):
    file = open(dbfilename, 'rb')
    db = pickle.load(file)
    file.close()
    return db

if __name__ == '__main__':
    db = loadDbase()
    print(db)
    
