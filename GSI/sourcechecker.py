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
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow()
    form.setWindowTitle('Source Checker')
    form.show()
    app.exec_()    