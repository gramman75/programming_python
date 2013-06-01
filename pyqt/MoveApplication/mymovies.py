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
import moviedata , qrc_resources

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):        #최초 수행시 자동 수행되는 초기화 함수, 상위 윈도우가 없어  parent=None
        super(MainWindow,self).__init__(parent)  #상속받은 QMainWindow의 Init함수 호출. 이 라인은 기계적으로 추가
        
        self.movies = moviedata.MovieContainer() #self로 선언을 하면 다른 함수에서 사용이 가능
        self.table = QTableWidget()
        self.setCentralWidget(self.table)
        
        # 상태바에 표시될 Label
        
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(True)        
        self.status.showMessage("Ready", 5000)
        
        '''
        5. action을 생성하고 menu와 toolbar에 action 추가
        '''
        fileNewAction = self.createAction('&New...', self.fileNew, QKeySequence.New,'filenew', u'새로운 파일을 생성합니다.')
        fileOpenAction = self.createAction('&Open...', self.fileOpen, QKeySequence.Open,'fileopen', u'기존 파일을 불러옵니다.')
        fileSaveAction = self.createAction('&Save', self.fileSave, QKeySequence.Save,'filesave', u'변경사항을 저장합니다.')
        fileSaveAsAction = self.createAction('Save As...', self.fileSaveAs, QKeySequence.SaveAs,'filesaveas', u'다른 이름으로 저장합니다.')
        fileQuitAction = self.createAction('&Quit', self.close,'Ctrl+Q', 'filequit', u'프로그램을 종료합니다.')
        
        editAddAction = self.createAction('Add...', self.editAdd, 'Ctrl+A','editadd', u'새로운 영화정보를 추가합니다.')
        editDeleteAction = self.createAction('Delete', self.editDelete, 'Ctrl+D','editdelete', u'선택한 영화정보를 삭제합니다.')
        editEditAction = self.createAction('&Edit...', self.editEdit, 'Ctrl+E','editedit', u'선택한 영화정보를 수정합니다.')
        
        
        helpAboutAction = self.createAction('&About Image Changer', self.helpAbout, None, None, 'About this application')
        '''
        6. menu를 생성하고 Action을 추가
        '''
        
        fileMenu = self.menuBar().addMenu('&File')
        editMenu = self.menuBar().addMenu('&Edit')
        helpMenu = self.menuBar().addMenu('&Help')
        
        self.addActions(fileMenu,(fileNewAction, fileOpenAction, fileSaveAction, fileSaveAsAction,None,fileQuitAction))
        self.addActions(editMenu,(editAddAction, editDeleteAction, editEditAction))
        self.addActions(helpMenu,(helpAboutAction,))
        '''
        7. toolbar를 생성하고 action추가 
        '''
        fileToolbar = self.addToolBar('File')
        editToolbar = self.addToolBar('Edit')
        self.addActions(fileToolbar,(fileNewAction, fileOpenAction, fileSaveAction, fileSaveAsAction))
        self.addActions(fileToolbar,(editAddAction, editDeleteAction, editEditAction))
        
        self.updateTable()
        
    def fileNew(self):
        if not self.okToContinue():
            return False
        
    
    def fileOpen(self):
        
        fname = QFileDialog.getOpenFileName(self, "load movie file","*.mqb","mqb")
        if not fname.isEmpty():
            ok, msg = self.movies.load(fname)
            self.status.showMessage(msg,5000)
            self.updateTable()
    
    def fileSave(self):
        if self.movies.__fname is None:
            return self.fileSaveAs()
        else:
            ok, msg = self.movies.save()
            self.status.showMessage(msg, 5000)
            return True
    
    def fileSaveAs(self):
        pass
    
    def editAdd(self):
        pass
    
    def editDelete(self):
        pass
    
    def editEdit(self):
        pass
    
    def helpAbout(self):
        pass
    
    
    
    def updateTable(self, current=None): #Data변경이 발생할 때 마다 호출하여 Table값 변경
        self.table.clear()
        self.table.setRowCount(len(self.movies))
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Title","Year","Mins","Acquired","Notes"])
        
        for row, movie in enumerate(self.movies):
            item = QTableWidgetItem(movie.title)
            self.table.setItem(row,0,item)
            
            item = QTableWidgetItem("{0}".format(movie.year))
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.table.setItem(row,1,item)
            
            item = QTableWidgetItem("{0}".format(movie.minutes))
            item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
            self.table.setItem(row,2,item)
            
            item = QTableWidgetItem(movie.acquired.toString("ddd MMM d, yyyy"))
            self.table.setItem(row,3,item)
            
            item = QTableWidgetItem(movie.notes)
            self.table.setItem(row,4,item)
            self.table.resizeColumnsToContents()
        
        
    
    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal="triggered()"):
        '''
        3. 메뉴나 toolbar에 사용될 Action을 만든다.
           Action 생성을 위한 util method 이다.
           createAction
        '''
        action = QAction(text, self)
        
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        
        if shortcut is not None:
            action.setShortcut(shortcut)
        
        if icon is not None:
            action.setIcon(QIcon(':/%s.png' %icon))
        
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        
        if checkable:
            action.setCheckable(True)
        
        return action
        
    def addActions(self, target, actions):
        '''
        4. menu나 toolbar에 여러개의 Action을 add하기 위한 Util Method
           target : menu나 toolbar
           actions: list type of action objects
        '''        
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
                
    def okToContinue(self):
        if self.movies.__dirty:
            reply = QMessageBox.question(self, "Question", "변경된 내용이 있습니다. 저장하시겠습니까?", QMessageBox.Ok|QMessageBox.No|QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Ok:
                return self.fileSave()
        
        return True
                


'''
2. 아래 코드는 Application 을 수행하는 코드로 거의 대부분 동일하게 Coding하면 됨.
   1,2까지 입력하고 수행하면 window화면에 빈 화면이 나타남.
'''
app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()         
