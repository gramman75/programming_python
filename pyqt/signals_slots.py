'''
Created on 2013. 2. 1.

@author: stmkmk
'''

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        
        maxnum = 1000
        
        dial = QDial()
        dial.setNotchesVisible(True)
        dial.setMaximum(maxnum)
        spinbox = QSpinBox()
        spinbox.setMaximum(maxnum)
        
        layout = QHBoxLayout()
        
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        
        self.setLayout(layout)
        
        self.connect(dial, SIGNAL("valueChanged(int)"),spinbox, SLOT("setValue(int)"))
        self.connect(spinbox, SIGNAL("valueChanged(int)"),dial.setValue)
        
        self.setWindowTitle('Signals and Slots')
app = QApplication(sys.argv)
form = Form()
form.siz
form.show()
app.exec_()            
        