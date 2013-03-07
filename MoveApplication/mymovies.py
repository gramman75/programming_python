#-*- encoding:utf8 -*-

'''
Created on 2013. 3. 7.

@author: stmkmk
'''

'''
1. Main Window를 선언한다.
   super의 init를 호출하고, moviedata의 MoveContaioner를 불러온뒤
   center에 QTableWidge을 위치시킨다.
'''

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import moviedata 

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):        #최초 수행시 자동 수행되는 초기화 함수, 상위 윈도우가 없어  parent=None
        super(MainWindow,self).__init__(parent)  #상속받은 QMainWindow의 Init함수 호출. 이 라인은 기계적으로 추가
        
        self.movies = moviedata.MovieContainer() #self로 선언을 하면 다른 함수에서 사용이 가능
        self.table = QTableWidget()
        self.setCentralWidget(self.table)
        self.updateTable()
        
    
    def updateTable(self, current=None): #Data변경이 발생할 때 마다 호출하여 Table값 변경
        self.table.clear()
        self.table.setRowCount(len(self.movies))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Title","Year","Mins","Acquired","Notes"])
        



'''
2. 아래 코드는 Application 을 수행하는 코드로 거의 대부분 동일하게 Coding하면 됨.
   1,2까지 입력하고 수행하면 window화면에 빈 화면이 나타남.
'''
app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()         
