#-*- encoding:utf8 -*-
'''
Created on 2013. 2. 16.

@author: gramman
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys, os
import qrc_resources, newimagedlg

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False
        
        # Popup메뉴에서 사용할 separator
        separator = QAction(self)
        separator.setSeparator(True)
        
        # Image가 Load될 Label
        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu) #popup메뉴 사용
        self.setCentralWidget(self.imageLabel)
        
        #Window내의 개별 화면 
        logDockWidget = QDockWidget('Log', self)
        logDockWidget.setObjectName('LogDockWidget')
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)
        
        self.printer = None
        
        # 상태바에 표시될 Label
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)
        
        # File메뉴 Action
        fileNewAction = self.createAction('&New...', self.fileNew, QKeySequence.New, 'filenew','Create an image file')
        fileOpenAction = self.createAction('&Open...', self.fileOpen, QKeySequence.Open, 'fileopen', 'Open File')
        fileSaveAction = self.createAction('&Save', self.fileSave, QKeySequence.Save, 'filesave', 'Save File')
        fileSaveAsAction = self.createAction('Save As...',self.fileSaveAs, QKeySequence.SaveAs,'filesaveas', 'Save as file')
        filePrintAction = self.createAction('&Print...', self.filePrint, QKeySequence.Print, 'fileprint', 'Print Image')
        fileQuitAction = self.createAction('&Quit', self.close,'Ctrl+Q', 'filequit', 'Close Application')
        
        # Edit메뉴 Action
        editZoomAction = self.createAction('Zoom', self.editZoom, 'Alt+Z', 'editzoom', 'Zoom Image')
        editInvertAction = self.createAction('Invert', self.editInvert, 'Ctrl+I', 'editinvert', 'Invert Image', True, 'toggled(bool)')
        editSwapAction = self.createAction('S&wap red and blue', self.editSwap, 'Ctrl+A', 'editswap', 'Swap red and blue', True, 'toggled(bool)')
        
        mirrorGroup = QActionGroup(self)
        editUnmirrorAction = self.createAction('&Unmirror', self.editUnmirror, 'Ctrl+U', 'editunmirror', 'Unmirror image',True, 'toggled(bool)')
        editMirrorhorizAction = self.createAction('&Unmirror', self.editMirrorhoriz, 'Ctrl+U', 'editmirrorhoriz', 'Mirror Horizontally image',True, 'toggled(bool)')
        editMirrorvertAction= self.createAction('&Unmirror', self.editMirrorvert, 'Ctrl+U', 'editmirrorvert', 'Mirror Vertically image',True, 'toggled(bool)')
        
        #Help메뉴 Action
        helpAboutAction = self.createAction('&About Image Changer', self.helpAbout, None, None, 'About this application')
        helpHelpAction = self.createAction('&Help', self.helpHelp, None, None, 'Help this application')
        
        #메뉴바에 Top Level메뉴 생성
        self.fileMenu = self.menuBar().addMenu('&File')
        self.connect(self.fileMenu, SIGNAL("aboutToShow()"),self.updateFileMenu)
        editMenu = self.menuBar().addMenu('&Edit')
        helpMenu = self.menuBar().addMenu('&Help')
        
        #Top Menu에 Action추가
        #self.addActions(self.fileMenu, (fileNewAction, fileOpenAction,fileSaveAction,fileSaveAsAction, None,filePrintAction,None,fileQuitAction))
        self.fileMenuActions =(fileNewAction, fileOpenAction,fileSaveAction,fileSaveAsAction, None,filePrintAction,None,fileQuitAction)
        self.addActions(editMenu,(editZoomAction, editInvertAction, editSwapAction))
        #Edit메뉴에 submenu생성
        mirrorMenu = editMenu.addMenu(QIcon(':/editmirror.png'),'&Mirror')
        
        #sub메뉴에 Action추가
        self.addActions(mirrorMenu, (editUnmirrorAction, editMirrorhorizAction, editMirrorvertAction))
        self.addActions(helpMenu,(helpAboutAction, helpHelpAction))
                        
        #Toolbar생성
        fileToolbar = self.addToolBar('File')
        fileToolbar.setObjectName('FileToolBar')
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction,fileSaveAsAction))
        
        editToolbar = self.addToolBar('Edit')
        editToolbar.setObjectName('EditToolBar')
        self.addActions(editToolbar, (editInvertAction, editSwapAction,editUnmirrorAction, editMirrorhorizAction, editMirrorvertAction))
        
        #Toolbar에 widjet추가
        self.zoomSpinBox = QSpinBox()
        self.zoomSpinBox.setSuffix('%')
        self.zoomSpinBox.setRange(1,400)
        self.zoomSpinBox.setValue(100)
        self.zoomSpinBox.setToolTip('Zoom the image')
        self.zoomSpinBox.setStatusTip('Zoom the image')
        self.zoomSpinBox.setFocusPolicy(Qt.NoFocus)
        self.connect(self.zoomSpinBox, SIGNAL('valueChanged(int)'),self.showImage)
                     
        editToolbar.addWidget(self.zoomSpinBox)
        
        self.addActions(self.imageLabel, (editInvertAction, editSwapAction, separator,editUnmirrorAction, editMirrorhorizAction, editMirrorvertAction))
        
        #setting value Load하여 적용
        settings = QSettings()
        self.recentFiles = settings.value("RecentFiles").toStringList()
        self.restoreGeometry(
                settings.value("MainWindow/Geometry").toByteArray())
        self.restoreState(settings.value("MainWindow/State").toByteArray())
        
        self.setWindowTitle("Image Changer")
        self.updateFileMenu()
        QTimer.singleShot(0, self.loadInitialFile)
    
    # Open, Close시에 변경 내용 저장 여부 확인
    def okToContinue(self): 
        if self.dirty:
            reply = QMessageBox.question(self, 'Image Changer', 'Save unsaved changes?', 
                                         QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if reply == QMessageBox.Cancel:
                return False
            elif reply == QMessageBox.Ok:
                return self.fileSave()
        return True
    
    # Application종료시 호출 
    def closeEvent(self, event):
                
        if self.okToContinue():
            settings = QSettings()
            fileName = QVariant(QString(self.fileName)) if self.filename is not None else QVariant()
            settings.setValue('LastFile',fileName)
            recentFiles = QVariant(self.recentFiles) if self.recentFiles else QVariant()
            settings.setValue('RecentFiles',recentFiles)
            settings.setValue('MainWindow/Size',QVariant(self.size()))
            settings.setValue('MainWindow/Position', QVariant(self.pos()))
            settings.setValue('MainWindow/State',QVariant(self.saveState()))
            settings.setValue('MainWindow/Geometry',QVariant(self.saveGeometry()))
        else:
            event.ignore()
            
    def updateFileMenu(self):
        self.fileMenu.clear()
        self.addActions(self.fileMenu, self.fileMenuActions[:-1])

        current = QString(self.filename) if self.filename is not None else None
        recentFiles =[]
        for fname in self.recentFiles:
            if fname != current and QFile(fname).exists():
                recentFiles.append(fname)
        
        if recentFiles:
            self.fileMenu.addSeparator()
            for i, fname in enumerate(recentFiles):
                action = QAction(QIcon(':/icon.png'),'%d %s' %(i+1, QFile(fname).fileName()),self)
                action.setData(QVariant(fname))
                self.connect(action, SIGNAL('triggered()'), self.loadFile)
                self.fileMenu.addAction(action)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.fileMenuActions[-1])
        
    def addRecentFile(self, fname):
        if fname is None:
            return
        if not self.recentFiles.contains(fname):
            self.recentFiles.prepend(QString(fname))
            while self.recentFiles.count() > 9:
                self.recentFiles.takeLast()    
            
    # Application 실행시 마지막 파일 Load
    def loadInitialFile(self):
        settings = QSettings()
        lastFile = str(settings.value('LastFile').toString())
        if lastFile and QFile.exists(lastFile):
            self.loadFile(lastFile)

    def loadFile(self, fname=None):
        pass
            
    def showImage(self):
        pass
    
    # Menu에 Action추가    
    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
    
    #Action 생성             
    def createAction(self, text, slot=None, shortcut=None, icon=None, tip=None, checkable=False, signal='triggered()'):
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

    def fileNew(self):
        if not self.okToContinue():
            return
        
        dialog = newimagedlg.NewImageDlg(self)
        if dialog.exec_():
            self.image = QImage()
            self.image = dialog.image()
            self.dirty = True
            self.filename = None
            self.showImage()
            self.sizeLabel.setText('%s x %s' %(self.image.width(), self.image.height()))            
            self.updateStatus('Crete New Image')
        
    def updateStatus(self, message):
        self.statusBar().showMessage(message, 5000)
        self.listWidget.addItems(message)
        if self.filename is not None:
            self.setWindowTitle('Image Changer %s' %self.filename)
        elif not self.image.isNull():
            self.setWindowTitle('Image Changer - Unnamed')
        else:
            self.setAcceptDrops(w)
        
        
        
    
    def fileOpen(self):
        if not self.okToContinue():
            return
        #directory = QFileDialog.getExistingDirectory(self,'Select Directory','.')
        dir = os.path.dirname(self.fileName) if self.filename is not None else '.'
        formats = ['*.%s' % unicode(format).lower() for format in QImageReader.supportedImageFormats()]
        fname = QFileDialog.getOpenFileName(self, 'Open Image', dir,"Image files (%s)" % " ".join(formats))
        
        if fname:
            self.loadFile(fname) 
        

    def fileSave(self):
        pass
    
    def fileSaveAs(self):
        pass
    
    def filePrint(self):
        pass
        
    def close(self):
        pass
    
    def editZoom(self):
        pass
    
    def editInvert(self):
        pass
    
    def editSwap(self):
        pass
    
    def editUnmirror(self):
        pass
    
    def editMirrorhoriz(self):
        pass
    
    def editMirrorvert(self):
        pass
    
    def helpAbout(self):
        pass
    
    def helpHelp(self):
        pass
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    app.setOrganizationName('Org Name') #HKEY_CURRENT_USER\Software\Org Name QSetting Default Name
    app.setOrganizationDomain('Domain Name')
    app.setApplicationName('App Name')
    app.setWindowIcon(QIcon(':/icon.png'))
    form = MainWindow()
    form.setWindowTitle('App Title')
    form.show()
    app.exec_()