'''
Created on 2013. 1. 15.

@author: stmkmk
'''
from make_db_file import loadDbase, storeDbase

db = loadDbase()
db['tom']['pay'] = 100
storeDbase(db)

