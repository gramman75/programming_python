'''
Created on 2013. 2. 16.

@author: gramman
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import qrc_resources

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False
        
        separator = QAction(self)
        separator.setSeparator(True)
        
        self.imageLabel = QLabel()
        self.imageLabel.setMinimumSize(200, 200)
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setCentralWidget(self.imageLabel)
        
        logDockWidget = QDockWidget('Log', self)
        logDockWidget.setObjectName('LogDockWidget')
        logDockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.listWidget = QListWidget()
        logDockWidget.setWidget(self.listWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, logDockWidget)
        
        self.printer = None
        
        self.sizeLabel = QLabel()
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Ready", 5000)
        
        fileNewAction = self.createAction('&New...', self.fileNew, QKeySequence.New, 'filenew','Create an image file')
        fileOpenAction = self.createAction('&Open...', self.fileOpen, QKeySequence.Open, 'fileopen', 'Open File')
        fileSaveAction = self.createAction('&Save', self.fileSave, QKeySequence.Save, 'filesave', 'Save File')
        fileSaveAsAction = self.createAction('Save As...',self.fileSaveAs, QKeySequence.SaveAs,'filesaveas', 'Save as file')
        filePrintAction = self.createAction('&Print...', self.filePrint, QKeySequence.Print, 'fileprint', 'Print Image')
        fileQuitAction = self.createAction('&Quit', self.close,'Ctrl+Q', 'filequit', 'Close Application')
        
        editZoomAction = self.createAction('Zoom', self.editZoom, 'Alt+Z', 'editzoom', 'Zoom Image')
        editInvertAction = self.createAction('Invert', self.editInvert, 'Ctrl+I', 'editinvert', 'Invert Image', True, 'toggled(bool)')
        editSwapAction = self.createAction('S&wap red and blue', self.editSwap, 'Ctrl+A', 'editswap', 'Swap red and blue', True, 'toggled(bool)')
        
        mirrorGroup = QActionGroup(self)
        editUnmirrorAction = self.createAction('&Unmirror', self.editUnmirror, 'Ctrl+U', 'editunmirror', 'Unmirror image',True, 'toggled(bool)')
        editMirrorhorizAction = self.createAction('&Unmirror', self.editMirrorhoriz, 'Ctrl+U', 'editmirrorhoriz', 'Mirror Horizontally image',True, 'toggled(bool)')
        editMirrorvertAction= self.createAction('&Unmirror', self.editMirrorvert, 'Ctrl+U', 'editmirrorvert', 'Mirror Vertically image',True, 'toggled(bool)')
       
        helpAboutAction = self.createAction('&About Image Changer', self.helpAbout, None, None, 'About this application')
        helpHelpAction = self.createAction('&Help', self.helpHelp, None, None, 'Help this application')
        
        fileMenu = self.menuBar().addMenu('&File')
        editMenu = self.menuBar().addMenu('&Edit')
        helpMenu = self.menuBar().addMenu('&Help')
        self.addActions(fileMenu, (fileNewAction, fileOpenAction,fileSaveAction,fileSaveAsAction, None,filePrintAction,None,fileQuitAction))
        
        self.addActions(editMenu,(editZoomAction, editInvertAction, editSwapAction))
        mirrorMenu = editMenu.addMenu(QIcon(':/editmirror.png'),'&Mirror')
        self.addActions(mirrorMenu, (editUnmirrorAction, editMirrorhorizAction, editMirrorvertAction))
        self.addActions(helpMenu,(helpAboutAction, helpHelpAction))
                        
        
        fileToolbar = self.addToolBar('File')
        fileToolbar.setObjectName('FileToolBar')
        self.addActions(fileToolbar, (fileNewAction, fileOpenAction,fileSaveAsAction))
        
        editToolbar = self.addToolBar('Edit')
        editToolbar.setObjectName('EditToolBar')
        self.addActions(editToolbar, (editInvertAction, editSwapAction,editUnmirrorAction, editMirrorhorizAction, editMirrorvertAction))
        
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
        
        
        settings = QSettings()
        self.recentFiles = settings.value('RecentFiles').toStringList()
        size = settings.value('MainWindow/Size',QVariant(QSize(600,500))).toSize()
        self.resize(size)
        position = settings.value('MainWindow/Position', QVariant(QPoint(0,0))).toPoint()
        self.move(position)
        
    def showImage(self):
        pass
        
    def addActions(self, target, actions):
        for action in actions:
            if action is None:
                target.addSeparator()
            else:
                target.addAction(action)
                
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
        pass
    
    def fileOpen(self):
        pass
    
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
    app.setOrganizationName('Org Name')
    app.setOrganizationDomain('Domain Name')
    app.setApplicationName('App Name')
    app.setWindowIcon(QIcon(':/icon.png'))
    form = MainWindow()
    form.setWindowTitle('App Title')
    form.show()
    app.exec_()