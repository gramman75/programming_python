'''
Created on 2013. 1. 31.

@author: stmkmk
'''

import sys
from math import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit("Type an expression and press Enter")
        self.lineEdit.selectAll()
        
        
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        
        
        self.setLayout(layout)
        self.lineEdit.setFocus()
        
        self.connect(self.lineEdit, SIGNAL("returnPressed()"), self.updateui)
        self.setWindowTitle("Calculate")

        
        
    def updateui(self):
        try:
            text = self.lineEdit.text()
            self.browser.append("%s = <b>%s</b>" %(text, eval(str(text))))
        except:
            self.browser.append("%s = <font color=red><b>%s</b></font>" %(text, "Invalid"))
        finally:
            self.lineEdit.selectAll()


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)
form = Form()
form.show()
app.exec_()                