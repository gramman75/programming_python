'''
Created on 2013. 4. 7.

@author: gramman
'''
'''
import dbm
file = dbm.open('movie','c')
file['Batman'] = "pow!"
file.close( )
'''
from person import Person
import pickle

a = Person('kim','dev')
f = open(r'D:\project\programming_python\edu\abc.pkl','wb')
pickle.dump(a,f)

