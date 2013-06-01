'''
Created on 2013. 1. 17.

@author: stmkmk
'''
import shelve
fieldnames = ['name','age','pay','job']
maxfield = max(len(f) for f in fieldnames)
db = shelve.open('people-class')


while True:
    key = input('Key=> ')
    if not key:
        break 
    try:
        record = db[key]
    except:
        print('No such key %s' %key)
    else:
        for field in fieldnames:
            print(field.ljust(maxfield),' => ',getattr(record,field))
    

