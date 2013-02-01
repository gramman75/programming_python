'''
Created on 2013. 2. 1.

@author: stmkmk
'''

import urllib, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        
        self.currency =  {'대한민국' : 'KRW',
                     '미국' :'USD',
                     '중국':'CNY',
                     '유로':'EUR'                
                     }
        
        cur = list(self.currency.keys())
        
        equalLabel = QLabel('=')
        
        self.fromCurrency = QComboBox()
        self.fromCurrency.addItems(cur)
        self.fromAmount = QLineEdit()
        
        self.toCurrency = QComboBox()
        self.toCurrency.addItems(cur)
        self.toAmount = QLineEdit()
        
        self.cal = QPushButton("계산")
               
        
        
        fromLayout = QVBoxLayout()
        fromLayout.addWidget(self.fromCurrency)
        fromLayout.addWidget(self.fromAmount)
        
        
        toLayout = QVBoxLayout()
        toLayout.addWidget(self.toCurrency)
        toLayout.addWidget(self.toAmount)
        
        layout = QHBoxLayout()
        layout.addLayout(fromLayout)
        layout.addWidget(equalLabel)
        layout.addLayout(toLayout)
                        
        self.setLayout(layout)    
        
        self.connect(self.fromAmount, SIGNAL("returnPressed()"), self.updateui)
        #self.connect(self.toAmount, SIGNAL("textChanged()"), self.updateui)
    
    def updateui(self):
        print('abc')
        fromCur = self.currency[self.fromCurrency.currentText()]
        toCur = self.currency[self.toCurrency.currentText()]
        fromAmt = self.fromAmount.text()
        
        url = r"http://www.google.com/ig/calculator?hl=KR&q=%s%s=?%s" %(fromAmt, fromCur, toCur)
        print(url)
        #resp = urllib.request.urlopen(url)
        self.toAmount.setText('123') 
        
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
       
        

        
