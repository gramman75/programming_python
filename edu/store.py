'''
Created on 2013. 4. 7.

@author: gramman
'''
import dbm
file = dbm.open('movie','c')
file['Batman'] = "pow!"
file.close( )