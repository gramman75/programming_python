'''
Created on 2013. 2. 16.

@author: gramman
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        
        self.image = QImage()
        self.dirty = False
        self.filename = None
        self.mirroredvertically = False
        self.mirroredhorizontally = False
        
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
        
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()
