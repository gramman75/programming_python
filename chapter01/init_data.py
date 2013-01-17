#-*- encoding:utf8 -*-

'''
Created on 2013. 1. 10.

@author: stmkmk
'''


bob = {'name' : 'Bob Smith', 'age' : 42, 'pay' : 30000, 'job' : 'dev'}
sue = {'name' : 'Sue Jones', 'age' : 44, 'pay' : 50000, 'job' : 'hdw'}
tom = {'name' : 'Tom',       'age' : 50, 'pay' : 0,     'job' : 'none'}

db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>\n',db[key])

