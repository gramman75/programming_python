'''
Created on 2013. 2. 15.

@author: stmkmk
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class NumberFormatDlg(QDialog):
    def __init__(self, format, parent=None):
        super(NumberFormatDlg,self).__init__(parent)
        
        thousandsepLabel = QLabel('Thousands separator')
        self.thousandsepEdit  = QLineEdit()
        self.thousandsepEdit.setText(format['thousandsep'])
        thousandsepLabel.setBuddy(self.thousandsepEdit)
        
        decimalmarkerLabel = QLabel('Decimal marker')
        self.decimalmarkerEdit = QLineEdit()
        self.decimalmarkerEdit.setText(format['decimalmarker'])
        decimalmarkerLabel.setBuddy(self.decimalmarkerEdit)
        
        decimalplaceLabel = QLabel('Decimal places')
        self.decimalplaceSpin = QSpinBox()
        self.decimalplaceSpin.setRange(0,7)
        self.decimalplaceSpin.setValue(format['decimalplace'])
            
        decimalplaceLabel.setBuddy(self.decimalplaceSpin)
        
        self.redNegativeCheck = QCheckBox('Red negative numbers')
        self.redNegativeCheck.setChecked(format['rednegatives'])
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        
        self.format = format.copy()
        
        layout = QGridLayout()
        
        layout.addWidget(thousandsepLabel,0,0)
        layout.addWidget(self.thousandsepEdit,0,1)
        
        layout.addWidget(decimalmarkerLabel,1,0)        
        layout.addWidget(self.decimalmarkerEdit,1,1)
        
        layout.addWidget(decimalplaceLabel,2,0)
        layout.addWidget(self.decimalplaceSpin,2,1)
        
        layout.addWidget(self.redNegativeCheck,3,0,1,2)
        layout.addWidget(buttonBox, 4, 0, 1, 2)
         
        self.setLayout(layout)
        self.setWindowTitle('Set Number Format(Modal)')
    
        self.connect(buttonBox, SIGNAL('accepted()'), self, SLOT('accept()'))
        self.connect(buttonBox, SIGNAL('rejected()'), self, SLOT('reject()'))

    def accept(self):
        self.format["thousandsep"] = str(self.thousandsepEdit.text())
        self.format["decimalmarker"] = str(self.decimalmarkerEdit.text())
        self.format["decimalplace"] = (self.decimalplaceSpin.value())
        self.format["rednegatives"] = (self.redNegativeCheck.isChecked())
        QDialog.accept(self)
        
    def numberFormat(self):
        return self.format
        
        