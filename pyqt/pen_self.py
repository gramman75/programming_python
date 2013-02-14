'''
Created on 2013. 2. 14.

@author: stmkmk
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        self.width = 1
        self.beveled = False
        self.style = "Solid"
        
        self.label = QLabel()
        
        inlineButton = QPushButton('Inline')
        classButton = QPushButton('class')
        
        layout = QVBoxLayout()
        layout.addWidget(inlineButton)
        layout.addWidget(classButton)
        layout.addWidget(self.label)
        
        self.setLayout(layout)
        
        self.connect(inlineButton, SIGNAL('clicked()'), self.inLineProperty)

        self.updateData()
    
    def updateData(self):
        self.label.setText('Width = {0}<BR>Style={1}<BR>Beveled ={2}'.format(self.width, self.style, self.beveled))
        
    def inLineProperty(self):
        
        widthLabel = QLabel('&Width : ')
        widthSpin = QSpinBox()
        widthSpin.setRange(1,24)
        widthLabel.setBuddy(widthSpin)
        widthSpin.setValue(self.width)
        
        bevelCheck = QCheckBox('&Beveled edges')
        bevelCheck.setCheckState(self.beveled)
        
        styleLabel = QLabel('&Style :')
        styleCombo = QComboBox()
        styleLabel.setBuddy(styleCombo)
        styleCombo.addItems(['Dot','Underline','Bold','Solid'])
        styleCombo.setCurrentIndex(styleCombo.findText(self.style))
        
        okButton = QPushButton('&Ok')
        cancelButton = QPushButton('&Cancel')
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addStretch()
        buttonLayout.addWidget(okButton)
        buttonLayout.addWidget(cancelButton)
        
        layout = QGridLayout()
        layout.addWidget(widthLabel, 0,0)
        layout.addWidget(widthSpin, 0, 1)
        layout.addWidget(bevelCheck,0,2)
        
        layout.addWidget(styleLabel,1,0)
        layout.addWidget(styleCombo,1,1,1,2)
        
        layout.addLayout(buttonLayout,2,0,1,3)
        
        form = QDialog()
        form.setLayout(layout)
        
        self.connect(okButton, SIGNAL('clicked()'),form,SLOT('accept()'))
        self.connect(cancelButton, SIGNAL('clicked()'),form,SLOT('reject()'))
        
        if form.exec_():
            print('a')
            self.width = widthSpin.value()
            self.style = styleCombo.currentText()
            self.beveled = bevelCheck.isChecked()
            self.updateData()

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()        