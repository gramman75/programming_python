#-*- encoding: utf8 -*-
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        
        '''
        이 부분에 Layout Coding 추가
        '''
        self.label = QLabel('Test')
        self.text = QLineEdit()
        self.button = QPushButton('&Ok')
        
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text)
        layout.addWidget(self.button)
        self.setLayout(layout)
        self.connect(self.button, SIGNAL("returnPressed()"), self.aaa)
        

    def aaa(self):
        QMessageBox.information(self, self.tr("About This Example"),
self.tr("This example shows how signals and slots are used to\n"
"communication between objects in Python and C++."))
            
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
        