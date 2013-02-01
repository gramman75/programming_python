'''
Created on 2013. 2. 1.

@author: stmkmk
'''

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class ZeroSpinBox(QSpinBox):
    zeroCount = 0
    def __init__(self, parent=None):
        super(ZeroSpinBox,self).__init__(parent)
        self.connect(self, SIGNAL("valueChanged(int)"),self.checkZero)
        
    def checkZero(self):
        if self.value() == 0:
            self.zeroCount+=1
            self.emit(SIGNAL("atzero"), self.zeroCount)
            
class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        dial = QDial()
        spinbox = ZeroSpinBox()
        
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        
        self.setLayout(layout)
        
        self.connect(dial, SIGNAL("valueChanged(int)"),spinbox, SLOT("setValue(int)"))
        self.connect(spinbox, SIGNAL("valueChanged(int)"),dial.setValue)
        self.connect(spinbox, SIGNAL("atzero"),self.anounce)
    
    def anounce(self, zeroCount):        
        print('Zero Count :', zeroCount)
                    
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()        