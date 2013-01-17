'''
Created on 2013. 1. 15.

@author: stmkmk
'''
from make_db_pickle import storeDbase, loadDbase

db = loadDbase()
db['tom']['pay'] = 12000
storeDbase(db)

db = loadDbase()
print(db)
