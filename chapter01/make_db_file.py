'''
Created on 2013. 1. 15.

@author: stmkmk
'''
dbfilename = 'people-file'
ENDDB = 'enddb'
ENDREC = 'endrec'
RECSEP = '=>'


def storeDbase(db, dbfilename=dbfilename):
    fid = open(dbfilename, 'w')
    for key in db:
        print(key, file=fid)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file=fid)
        print(ENDREC, file=fid)
    print(ENDDB, file=fid)
    fid.close()
    
def loadDbase(dbfilename=dbfilename):
    file = open(dbfilename, 'r')
    import sys
    sys.stdin = file
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db
    
if __name__ == '__main__':
    from init_data import db
    storeDbase(db)    
