#-*- encoding:utf8 -*-
'''
Created on 2013. 5. 31.

@author: stmkmk
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        
        fileNewAction = self.createAction('&New...',self.fileNew, QKeySequence.New, 'filenew','Create New File')
        fileOpenAction = self.createAction('&Open...',self.fileOpen, QKeySequence.Open,'fileopen','Open File' )
        fileSaveAction = self.createAction('&Save',self.fileSave, QKeySequence.Save, 'filesave', 'Save Feil')
        fileSaveAsAction = self.createAction('Save As...', self.fileSaveAs, QKeySequence.SaveAs,'filesaveas','Save As')
        filePrefAction = self.createAction('Preference',self.filePref, None,'filepref','환경설정')
        fileQuitAction = self.createAction('&Quit', self.fileQuit, QKeySequence.Quit,'filequit')
        
        fileMenu = self.menuBar().addMenu('&File')
        
        self.addActions(fileMenu,(fileNewAction, fileOpenAction, None, fileSaveAction, fileSaveAsAction, None, filePrefAction, None, fileQuitAction))
    
    
        centerWidget = QLabel()
        self.setCentralWidget(centerWidget)
        self.resize(500,500)

        # Source Directory 
        sourceLabel = QLabel('&Source Directory')
        self.sourceEdit  = QLineEdit()
        sourceLabel.setBuddy(self.sourceEdit)
        sourceToolBtn = QToolButton()
        sourceToolBtn.setArrowType(Qt.UpArrow)
        self.includeCheckBox = QCheckBox('include directory')
        self.connect(sourceToolBtn, SIGNAL("clicked()"), self.selectSourceDir)
        
        ''' 
        sourceLayout = QHBoxLayout()
        sourceLayout.addWidget(sourceLabel)
        sourceLayout.addWidget(self.sourceEdit)
        sourceLayout.addWidget(sourceToolBtn)
        '''
        
        # Destination Directory
        destLabel = QLabel('&Destination Directory')
        self.destEdit = QLineEdit()
        destLabel.setBuddy(self.destEdit)
        destToolBtn = QToolButton()
        destToolBtn.setArrowType(Qt.UpArrow)
        self.convertCheckBox = QCheckBox('Convert fmb to txt')
        self.connect(destToolBtn, SIGNAL("clicked()"), self.selectDestDir)
        '''
        destLayout= QHBoxLayout()
        destLayout.addWidget(destLabel)
        destLayout.addWidget(self.destEdit)
        destLayout.addWidget(destToolBtn) 
        '''
        
        basicLayout = QGridLayout()
        basicLayout.addWidget(sourceLabel,0,0)
        basicLayout.addWidget(self.sourceEdit,0,1) 
        basicLayout.addWidget(sourceToolBtn,0,2)
        basicLayout.addWidget(self.includeCheckBox,1,1)
        
        
        basicLayout.addWidget(destLabel,2,0)
        basicLayout.addWidget(self.destEdit,2,1)
        basicLayout.addWidget(destToolBtn,2,2)
        basicLayout.addWidget(self.convertCheckBox,3,1)
        layout = QVBoxLayout(centerWidget)
        
        
        # Search Condition
        
        self.directRadioBtn = QRadioButton('Direct Input')
        self.fileRadioBtn = QRadioButton('Select File')
        searchLabel = QLabel('Search Word')
        self.searchEdit = QLineEdit()
        searchToolBtn = QToolButton()
        searchToolBtn.setArrowType(Qt.UpArrow)
        self.searchKorCheckBox = QCheckBox('Search Korean')
        
        
        
        searchLayout = QGridLayout()
        searchLayout.addWidget(self.directRadioBtn, 0,1)
        searchLayout.addWidget(self.fileRadioBtn,0,2)
        searchLayout.addWidget(searchLabel,1,0)
        searchLayout.addWidget(self.searchEdit,1,1,1,2)
        searchLayout.addWidget(searchToolBtn,1,3)
        searchLayout.addWidget(self.searchKorCheckBox,2,1)
        
        searchGroupBox = QGroupBox('Search Condition')
        searchGroupBox.setLayout(searchLayout)

        # Search basis
        startWithLabel = QLabel('Prefix')
        self.startWithEdit = QLineEdit()
        endWithLabel = QLabel('Suffix')
        self.endWithEdit = QLineEdit()
        includeWithLabel = QLabel('Include')
        self.includeWithEdit = QLineEdit()

        basisLayout = QGridLayout()
        basisLayout.addWidget(startWithLabel,0,0)
        basisLayout.addWidget(self.startWithEdit,0,1)
        basisLayout.addWidget(endWithLabel,1,0)
        basisLayout.addWidget(self.endWithEdit,1,1)
        basisLayout.addWidget(includeWithLabel,2,0)
        basisLayout.addWidget(self.includeWithEdit,2,1)

        basisGroupBox = QGroupBox('Search Basis')
        basisGroupBox.setLayout(basisLayout)

        self.searchingFileLabel = QLabel('Searching....')

        self.progressBar = QProgressBar()
        self.progressBar.setValue(50)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)

        layout.setMargin(40)
        
        layout.addLayout(basicLayout)
        layout.addWidget(searchGroupBox)
        layout.addItem(QSpacerItem(30,30))
        layout.addWidget(basisGroupBox)
        # layout.addItem(QSpacerItem(30,30))
        layout.addWidget(self.searchingFileLabel)
        layout.addWidget(self.progressBar)
        
    def selectSourceDir(self):
        dname = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.sourceEdit.setText(dname)
        
    def selectDestDir(self):
        dname = QFileDialog.getExistingDirectory(self, 'Select Directory')
        self.destEdit.setText(dname)
        
    def fileNew(self):
        pass
    
    def fileOpen(self):
        pass
    
    def fileSave(self):
        pass
    
    def fileSaveAs(self):
        pass
    
    def filePref(self):
        pass
    
    def fileQuit(self):
        pass
        
    def addActions(self, target, actions):
        '''
        Menu에 Action추가
        '''
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
    
    
    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal='triggered()'):
        '''
        Action생성
        (self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal='triggered()'):
        '''
        action = QAction(text, self)
        
        if slot is not None:
            self.connect(action, SIGNAL(signal), slot)
        
        if shortcut is not None:
            action.setShortcut(shortcut)
            
        if icon is not None:
            action.setIcon(QIcon(':/%s.png' % icon))
        
        if tip is not None:
            action.setToolTip(tip)
            action.setStatusTip(tip)
        
        if checkable:
            action.setCheckable(True)
            
        return action
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    #form.resize(400,500)
    #form.setFixedHeight(500)
    form.setFixedSize(QSize(400,500))
    form.setWindowTitle('Source Checker')
    form.show()
    app.exec_()    