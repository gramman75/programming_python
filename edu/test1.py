'''
Created on 2013. 3. 21.

@author: stmkmk


'''

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        self.browser = QTextBrowser()
        self.lineEdit = QLineEdit()
        
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineEdit)
        
        self.setLayout(layout)
        
        self.connect(self.lineEdit, SIGNAL("returnPressed()"), self.updateui)
        
    def updateui(self):
        a = self.lineEdit.text()
        self.browser.setText(a)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
