'''
Created on 2013. 3. 22.

@author: stmkmk
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    def __init__(self, list, name,parent=None):
        super(Form,self).__init__(parent)
        
        self.title = name
        
        self.listItem = QListWidget()
        for itemName in list:
            item = QListWidgetItem(itemName)
            self.listItem.addItem(item)
        
        buttonLayout = QVBoxLayout()
        
        for text, slot in (('&Add,..', self.add),
                            ('&Edit...',self.edit),
                            ('&Remove...', self.remove),
                            ('&Up', self.up),
                            ('&Down',self.down),
                            ('&Sort',self.sort),
                            ('&Close', self.close)
                            ):
            button = QPushButton(text)
            self.connect(button, SIGNAL("clicked()"), slot)
            buttonLayout.addWidget(button)
        
        layout = QHBoxLayout()
        layout.addWidget(self.listItem)
        layout.addLayout(buttonLayout)
        
        self.setLayout(layout)
        self.setWindowTitle(name)
                         
    def add(self):
        row = self.listItem.currentRow()
        text, ok = QInputDialog.getText(self,self.title, self.title)
        if ok and text is not None:
            self.listItem.insertItem(row, QListWidgetItem(text))
    
    def edit(self):
        row = self.listItem.currentRow()
        item = self.listItem.item(row)
        text, ok = QInputDialog.getText(self, self.title, self.title, QLineEdit.Normal, item.text())
        if ok and  text is not None:
            item.setText(text)
    def remove(self):
        pass
    
    def up(self):
        pass
    
    def down(self):
        pass
    
    def sort(self):
        pass
    
    def close(self):
        pass

fruit = ["Banana", "Apple", "Elderberry", "Clementine", "Fig",
        "Guava", "Mango", "Honeydew Melon", "Date", "Watermelon",
        "Tangerine", "Ugli Fruit", "Juniperberry", "Kiwi", "Lemon",
        "Nectarine", "Plum", "Raspberry", "Strawberry", "Orange"]
app =QApplication(sys.argv)
form = Form(fruit, 'Fruit')
form.show()
app.exec_()        
        