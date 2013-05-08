#-*- encoding:utf8 -*-
'''
Created on 2013. 4. 12.

@author: stmkmk
'''
import sys, pygal
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import QSvgWidget


class Form(QDialog):
    def __init__(self,parent=None):
        super(Form, self).__init__(parent)
        
        svgWidget = QSvgWidget(parent)
        test ='안녕하세요'
        test = QString(test)        
        print test
        
        
        label  = QLabel("Bar Chart")
        bar_chart = pygal.Bar()
        bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])   
        svgStr = bar_chart.render()    
        #fname = open(r'D:\project\programming_python\edu\bar_chart.svg')
        #svgStr = fname.read()

        svgWidget.load(QByteArray.fromRawData(svgStr))
        
       
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(svgWidget)        
        
        self.setLayout(layout)
        

app = QApplication(sys.argv)
form = Form()
form.show()        
app.exec_()        
