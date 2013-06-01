'''
Created on 2013. 2. 15.

@author: stmkmk
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, string, random, math
import formatdlg1_self

class Form(QDialog):
    MAX_ROW = 60
    MAX_COL = 26
    
    def __init__(self, parent=None):
        super(Form,self).__init__(parent)
        
        self.numbers = {}
        self.format = {'thousandsep' : ",",
                        'decimalmarker' : ".",
                        'decimalplace' : 2,
                        'rednegatives' : False}
        
        for x in range(self.MAX_ROW):
            for y in range(self.MAX_COL):
                self.numbers[(x,y)] = (random.random() * 10000) - 5000
                        
        self.table = QTableWidget()
        
        modalButton = QPushButton('Set Number Format...(&Modal)')
        modalessButton = QPushButton('Set Number Format...(Modale&ss)')
        liveButton = QPushButton('Set Number Format...(&Live)')
        
        buttonBox = QHBoxLayout()
        buttonBox.addWidget(modalButton)
        buttonBox.addWidget(modalessButton)
        buttonBox.addWidget(liveButton)
        
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addLayout(buttonBox)
        self.setLayout(layout)
        self.setWindowTitle('Numbers')
        self.refreshTable()
        
        self.connect(modalButton, SIGNAL('clicked()'), self.numberFormatDlg1)

    def numberFormatDlg1(self):
        dlg = formatdlg1_self.NumberFormatDlg(self.format, self)
        if dlg.exec_():
            self.format = dlg.numberFormat()
            self.refreshTable()
        
        
    
    def refreshTable(self):
        self.table.setColumnCount(self.MAX_COL)
        self.table.setRowCount(self.MAX_ROW)        
        self.table.setHorizontalHeaderLabels(list(string.ascii_uppercase))
        
        for x in range(self.MAX_ROW):
            for y in range(self.MAX_COL):
                
                value = self.numbers[(x,y)]
                
                value = round(value,int(self.format['decimalplace']))
                whole, fraction = str(value).split('.')
                
                
                                
                sign = '-' if int(whole) < 0 else ""
                whole = str(abs(int(whole)))
                digits =[]
                for i, digit in enumerate(reversed(whole)):
                    if i and i %3 == 0:
                        digits.insert(0,self.format['thousandsep'])
                        digits.insert(0,digit)
                    else:
                        digits.insert(0,digit)
                
                if self.format['decimalplace']:
                    fraction = self.format['decimalmarker']+fraction
                else:
                    fraction =""
                    
                text ="{0}{1}{2}".format(sign,''.join(digits),fraction)
                                                    
                item = QTableWidgetItem(text)
                if sign and self.format["rednegatives"]:
                    item.setBackgroundColor(Qt.red)
                    
                item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)
                self.table.setItem(x,y,item)
                
                
app = QApplication(sys.argv)
form = Form()        
form.show()
app.exec_()
        
        
        