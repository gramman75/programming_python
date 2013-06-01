'''
Created on 2013. 2. 4.

@author: gramman
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        
        labelPriciple = QLabel('Principle:')
        labelRate = QLabel('Rate:')
        labelYears = QLabel('Years:')
        labelAmount = QLabel('Amount:')
        
        self.spinPriciple = QDoubleSpinBox()
        self.spinPriciple.setRange(1,100000)
        self.spinPriciple.setValue(2000)
        self.spinPriciple.setPrefix('$ ')
        
        self.spinRate  = QDoubleSpinBox()
        self.spinRate.setRange(0,100)
        self.spinRate.setValue(5.0)
        self.spinRate.setSuffix(' %')
        
        self.comboYears = QComboBox()
        self.comboYears.addItems(["{0} year".format(x) for x in range(1,13)])
        
        self.labelResult = QLabel('0')
        
        labelLayout = QVBoxLayout()
        labelLayout.addWidget(labelPriciple)
        labelLayout.addWidget(labelRate)
        labelLayout.addWidget(labelYears)
        labelLayout.addWidget(labelAmount)
        
        editLayout = QVBoxLayout()
        editLayout.addWidget(self.spinPriciple)
        editLayout.addWidget(self.spinRate)
        editLayout.addWidget(self.comboYears)
        editLayout.addWidget(self.labelResult)
        
        layout = QHBoxLayout()
        layout.addLayout(labelLayout)
        layout.addLayout(editLayout)
        
        self.setLayout(layout)
        
        self.connect(self.spinPriciple, SIGNAL('valueChanged(double)'),self.updateui)
        self.connect(self.spinRate, SIGNAL('valueChanged(double)'),self.updateui)
        self.connect(self.comboYears, SIGNAL('currentIndexChanged(int)'),self.updateui)
        
        self.updateui()
        
    def updateui(self):
       
        years = self.comboYears.currentIndex() + 1
        amount = self.spinPriciple.value() * ((1 + (self.spinRate.value() / 100.0)) ** years)
        self.labelResult.setText("$ {0:.2f}".format(amount))
    
    
app = QApplication(sys.argv)
form = Form() 
form.show()
app.exec_()       