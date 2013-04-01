#-*- encoding:utf8 -*-
'''
Created on 2013. 3. 11.

@author: stmkmk
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        self.__dirty = False
        self.__fname = None
        
        self.status = self.statusBar()
        self.status.setSizeGripEnabled(True)        
        self.status.showMessage("Ready", 5000)
        
        fileNewAction = self.createAction('&New...', self.fileNew, QKeySequence.New,'filenew', u'새로운 파일을 생성합니다.')
        fileOpenAction = self.createAction('&Open...', self.fileOpen, QKeySequence.Open,'fileopen', u'기존 파일을 불러옵니다.')
        fileSaveAction = self.createAction('&Save', self.fileSave, QKeySequence.Save,'filesave', u'변경사항을 저장합니다.')
        fileSaveAsAction = self.createAction('Save As...', self.fileSaveAs, QKeySequence.SaveAs,'filesaveas', u'다른 이름으로 저장합니다.')
        fileQuitAction = self.createAction('&Quit', self.close,'Ctrl+Q', 'filequit', u'프로그램을 종료합니다.')
    
        helpAboutAction = self.createAction('&About Image Changer', self.helpAbout, None, None, 'About this application')
        
        fileMenu = self.menuBar().addMenu('&File')
        helpMenu = self.menuBar().addMenu('&Help')
        
        self.addActions(fileMenu,(fileNewAction, fileOpenAction, fileSaveAction, fileSaveAsAction,None,fileQuitAction))
        self.addActions(helpMenu,(helpAboutAction,))
    
        centerWidget = QLabel()
        self.setCentralWidget(centerWidget)
        self.resize(600, 300)
        
        
        sourceLabel = QLabel('&Source')
        sourceLineEdit = QLineEdit()
        sourceLabel.setBuddy(sourceLineEdit)
        
        
        
        sourcePathLayout = QHBoxLayout()
        sourcePathLayout.addWidget(sourceLabel)
        sourcePathLayout.addWidget(sourceLineEdit)
        
        
        model = QFileSystemModel()
        
        model.setRootPath(sourceLineEdit.text())
        dirTree = QTreeView()
        dirTree.setModel(model)   
        '''     
        dirTree.setColumnWidth(0,150)  
        dirTree.setColumnHidden(1,True)      
        dirTree.setColumnHidden(2,True)      
        dirTree.setColumnHidden(3,True)
        '''      
        sourceLayout = QVBoxLayout()
        sourceLayout.addLayout(sourcePathLayout)
        sourceLayout.addWidget(dirTree)
        
        destLabel = QLabel('&Destination')
        destLineEdit = QLineEdit()
        destLabel.setBuddy(destLineEdit)
        
        keywordLabel = QLabel('&Keyword')
        keywordLineEdit = QLineEdit()
        keywordLabel.setBuddy(keywordLineEdit)
        
        checkLang = QCheckBox('&Checking Korean')
        
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')
        
        destLayout1 = QGridLayout()
        destLayout1.addWidget(destLabel,0,0)
        destLayout1.addWidget(destLineEdit,0,1)
        destLayout1.addWidget(keywordLabel,1,0)
        destLayout1.addWidget(keywordLineEdit,1,1)
        destLayout1.addWidget(checkLang,2,0,1,2)
        
        destButton = QHBoxLayout()
        destButton.addWidget(okButton)   
        destButton.addWidget(cancelButton)   
        
        destLayout = QVBoxLayout()     
        destLayout.addLayout(destLayout1)
        destLayout.addStretch()
        destLayout.addLayout(destButton)
        
               
                            
        #centerFrame = QFrame()
        #centerFrame.setLineWidth(100)
        
        mainLayout = QHBoxLayout()
        mainLayout.addLayout(sourceLayout)
        #layout.addWidget(centerFrame)
        mainLayout.addLayout(destLayout)
        
        layout = QVBoxLayout(centerWidget)        
        self.progressBar = QProgressBar()        
        self.progressBar.setValue(0)
        layout.addLayout(mainLayout)
        layout.addWidget(self.progressBar)
        
        
        
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
    
    def helpAbout(self):
        pass    
    
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
    
app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()        