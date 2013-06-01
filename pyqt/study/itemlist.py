'''
Created on 2013. 2. 15.

@author: stmkmk
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys


class Form(QDialog):
    def __init__(self, stringList, name, parent=None):
        super(Form, self).__init__(parent)
        
        self.name = name
        
        self.listBox = QListWidget()    
        self.listBox.addItems(stringList)
        self.listBox.setCurrentRow(0)
        
        buttonBox = QVBoxLayout()
        for text, slot in (('&Add...', self.add),
                            ('&Edit...',self.edit),
                            ('&Remove...',self.remove),
                            ('&Up', self.up),
                            ('&Down',self.down),
                            ('&Sort',self.sortItem),
                            ('&Close', self.accept)):
            button = QPushButton(text)
            buttonBox.addWidget(button)
            self.connect(button, SIGNAL('clicked()'),slot)
                                  
        layout = QHBoxLayout()
        layout.addWidget(self.listBox)
        layout.addLayout(buttonBox)
        self.setLayout(layout)
        self.setWindowTitle('Edit Fruit List')
        
    
    def add(self):
        row = self.listBox.currentRow()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and not string.isEmpty():
            self.listBox.insertItem(row, string)
    
    def edit(self):
        row = self.listBox.currentRow()
        item = self.listBox.item(row)
        title = 'Edit {0}'.format(self.name)
        string, ok =QInputDialog.getText(self, title, title, QLineEdit.Normal,str(item.text()))
        if ok and not string.isEmpty():
            item.setText(string)
    
    def remove(self):
        row = self.listBox.currentRow()
        item = self.listBox.item(row)
        
        if item is None:
            return
        
        reply = QMessageBox.question(self, "Remove {0}".format(self.name), "Remove {0} '{1}'?".format(self.name, str(item.text())),
                                     QMessageBox.Ok|QMessageBox.No)
        if reply == QMessageBox.Ok:
            item = self.listBox.takeItem(row)
            del item
    
    def up(self):
        row = self.listBox.currentRow()
        if row >=1:
            item = self.listBox.takeItem(row)
            self.listBox.insertItem(row-1, item)
            self.listBox.setCurrentItem(item)
    
    def down(self):
        row = self.listBox.currentRow()
        if row < self.listBox.count() -1:
            item = self.listBox.takeItem(row)
            self.listBox.insertItem(row+1, item)
            self.listBox.setCurrentItem(item)
    
    def sortItem(self):
        self.listBox.sortItems()
    
    def accept(self):
        QDialog.accept(self)
        
    
if __name__ =='__main__':
    fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
        "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
        "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi", "Lemon",
        "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]
    app = QApplication(sys.argv)
    form = Form(fruit,'Fruit')
    form.show()
    app.exec_()
    