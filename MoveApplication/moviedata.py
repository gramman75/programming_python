#-*- encoding:utf8 -*-

'''
Created on 2013. 3. 7.

@author: stmkmk
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *



class Movie():
    '''
    Movie 객체
    '''
    def __init__(self, title=None, year=None, mins=0, acquired=None, notes=None):
        self.title = title
        self.year = year
        self.mins = mins
        self.acquired = acquired if acquired is not None else QDate.currentDate()
        self.notes = notes

class MovieContainer():
    '''
    Movie 객체에 대한 속성과 Method(save, load, count ...)
    '''
    def __init__(self):
        '''
        초기 사용 변수
        __movieFromID = {} : id : Movie 객체를 저장
        '''
        self.__fname = QString()    
        self.__movies =[]
        self.__movieFromId = {}
        self.__dirty = False
        
    def __len__(self):
        return len(self.__movies)
    
    def clear(self, clearFilename=True):
        '''
        모든 Data를 Clear
        '''
        self.__movies = []
        self.__movieFromId = {}
        if clearFilename:
            self.__fname = QString()
        self.__dirty = False
        
        
    

def intFromQStr():
    pass

def encodedNewLines():
    pass

def decodedNewLines():
    pass


    