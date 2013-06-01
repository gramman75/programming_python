#-*- encoding:utf8 -*-

'''
Created on 2013. 3. 7.

@author: stmkmk
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import bisect


class Movie():
    '''
    Movie 객체
    '''
    def __init__(self, title=None, year=None, minutes=0, acquired=None, notes=None):
        self.title = title
        self.year = year
        self.minutes = minutes
        self.acquired = acquired if acquired is not None else QDate.currentDate()
        self.notes = notes

class MovieContainer():
    '''
    Movie 객체에 대한 속성과 Method(save, load, count ...)
    '''
    
    MAGIC_NUMBER = 0x3051E
    FILE_VERSION = 100
    def __init__(self):
        '''
        초기 사용 변수
        __movieFromID = {} : id : Movie 객체를 저장
        '''
        self.__fname = QString()    
        self.__movies =[]              #[key, movie]가 list로 보관됨.
        self.__movieFromId = {}        # id : Movive가 Dictionary로 보관됨.
        self.__dirty = False           # data변경시 True
        
    def __len__(self):
        return len(self.__movies)
    
    def __iter__(self):
        for pair in iter(self.__movies):
            yield pair[1]
    
    def filename(self):
        return self.__fname
    
    def setFilename(self, fname):
        self.__fname = fname
    
    def clear(self, clearFilename=True):
        '''
        모든 Data를 Clear
        '''
        self.__movies = [] 
        self.__movieFromId = {} 
        if clearFilename:
            self.__fname = QString()
        self.__dirty = False
        
        
    def add(self, movie):
        '''
        1. Movie object를 __movies에 추가
        '''
        if id(movie) in self.__movieFromId:
            return False
        
        key = self.key(movie.title, movie.year)
        bisect.insort_left(self.__movies, [key, movie])
        self.__movieFromId[id(movie)] = movie
        self.__dirty = True
        return True
        
    def delete(self, movie):
        '''
        2. movie object를 __movies에서 삭제
        '''
        if id(movie) not in self.__movieFromId:
            return False
        key = self.key(movie.title, movie.year)
        i = bisect.bisect_left(self.__movies, key)
        del self.__movies[i]
        del self.__movieFromId[id(movie)]
        self.__dirty = True
        return True
    
    def updateMovie(self, movie, title, year, minutes = None, notes=None):
        '''
        3. movie object를 수정함.
           title과 year가 수정되었을 경우에는 재정렬
        '''
        if minutes is not None:
            movie.minutes = minutes
            
        if notes is not None:
            movie.notes = notes
            
        if movie.title != title or movie.year != year:
            key = self.key(title, year)
            i =  bisect.bisect_left(self.__movies, [key,movie])
            self.__movies[i][0] = self.key(title, year)
            movie.title = title
            movie.year = year
            self.__movies.sort()
        
        self.__dirty = True
    
    def save(self, fname=QString()):
        '''
        4. 확장자에 따라 저장방법 분기
        '''
        if not fname.isEmpty():
            self.__fname = fname
        
        if self.__fname.endswith('.mqb'):
            self.saveQDataStream()
            
    def load(self,fname=QString()):
        '''
        5. 확장자에 따라 Load방법 분기
        '''
        if not fname.isEmpty():
            self.__fname = fname
        
        if self.__fname.endsWith('.mqb'):
            return self.loadQDataStream()   
        
        return False, "Failed to load: invalid file extension"       
               
    def saveQDataStream(self):
        '''
        6. QDataStream을 이용하여 저장
        '''
        
        fh = None
        error = None
        
        try:
            '''
            6.1 File Open
            '''
            fh = QFile(self.__fname)
            if not fh.open(QIODevice.WriteOnly):
                raise IOError, unicode(fh.errorString())
            '''
            6.2 Stream생성
            '''
            stream = QDataStream(fh)
            '''
            6.3 Binary파일 쓰기
            '''
            stream.writeInt32(MovieContainer.MAGIC_NUMBER)
            stream.writeInt32(MovieContainer.FILE_VERSION)
            '''
            6.3 Strem 버전
            '''
            stream.setVersion(QDataStream.Qt_4_2)
            
            '''
            6.4 Binary File읽기, String << or >> 사용
            ''' 
            
            for key, movie in self.__movies:
                stream << movie.title
                stream.writeInt16(movie.minutes)
                stream.writeInt16(movie.year)
                stream << movie.acquired << movie.notes
        except (IOError, OSError), e:
            error = "Failed to save : %s" %e
        finally:
            if fh is not None:
                fh.close()
            if error is not None:
                return False, error
            self.__dirty = False
        return True, "Saved %d movie record to %s" %(len(self.__movies), self.__fname)
        
    def loadQDataStream(self):
        
        error = None
        fh = None
        
        try:
            
            fh = QFile(self.__fname)
            if not fh.open(QIODevice.ReadOnly):
                raise IOError, unicode(fh.errorString())
            stream = QDataStream(fh)
            magic = stream.readInt32()
            
            if magic != MovieContainer.MAGIC_NUMBER:
                raise IOError, "Unrecongnized file type"
            
            version = stream.readInt32()
            
            if version < MovieContainer.FILE_VERSION:
                raise IOError, "old and unreadable file format"
            elif version > MovieContainer.FILE_VERSION:
                raise IOError, "new and unreadable file format"
            
            stream.setVersion(QDataStream.Qt_4_3)
            
            
            while not stream.atEnd():
                
                title = QString()
                print title
                acquired = QDate()
                notes = QString()
                
                stream >> title
                year = stream.readInt16()
                minutes = stream.readInt16()
                stream >> acquired >> notes
                self.add(Movie(title, year, minutes, acquired, notes))

        except (IOError, OSError), e:
            error = "Failed to load : %s" %e
        finally :
            if fh is not None:
                fh.close()
            if error is not None:
                return False, error
            self.__dirty = False
        
        
        print "movies count : %d" % (len(self.__movies))
        print "movies count : %s" % QFileInfo(self.__fname).fileName()
        
        return True, "Load %d movie record to %s" %(len(self.__movies), QFileInfo(self.__fname).fileName() ) 
              
    
    def key(self, title, year):
        text = unicode(title).lower()
        
        if text.startswith("a "):
            text = text[2:]
        elif text.startswith("the "):
            text = text[4:]
        elif text.startswith("an "):
            text = text[3:]
        
        parts = text.split(" ",1)
        if parts[0].isdigit():
            text = "%08d" %int(parts[0])
            text += text + parts[1]
        return "%s\t%d" %(text.replace(" ", ""), year)
            
        
        
        return None 

def intFromQStr():
    pass

def encodedNewLines():
    pass

def decodedNewLines():
    pass


    