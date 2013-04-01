'''
Created on 2013. 3. 11.

@author: stmkmk
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys, os

class DirectoryTree(QDialog):
    
    def __init__(self, parent=None):
    
        super(DirectoryTree,self).__init__(parent)
    
        model = QFileSystemModel()        
        model.setRootPath(r'c:\project')
        model.setNameFilterDisables(False)
        dirTree = QTreeView()
        dirTree.setModel(model)
        
        dirTree.setColumnWidth(0,200)
      
        layout = QVBoxLayout()
        layout.addWidget(dirTree)
        
        self.setLayout(layout)
        
app = QApplication(sys.argv)
form = DirectoryTree()        
form.show()
app.exec_()