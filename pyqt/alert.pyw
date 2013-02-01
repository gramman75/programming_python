'''
Created on 2013. 1. 30.

@author: stmkmk
'''
import sys, time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)

try:
    message = 'Alert'
    due = QTime.currentTime()
    if len(sys.argv) <2:
        raise ValueError

    hours, mins = sys.argv[1].split(':')
    due = QTime(int(hours), int(mins))
    
    if not due.isValid():
        raise ValueError
    
    if len(sys.argv) > 2:
        message = "".join(sys.argv[2:])
        

except ValueError:
    message = "Usage : alert.pvw HH:MM [other message]"
    
while QTime.currentTime() < due:
    time.sleep(10)        
    
label = QLabel('<font color=blue size=200><b>{0}</b></font>'.format(message)) 
label.setWindowFlags(Qt.SplashScreen)
label.show()

QTimer.singleShot(10000, app.quit)   
app.exec_()