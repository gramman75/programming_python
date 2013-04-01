'''
Created on 2013. 3. 27.

@author: stmkmk
'''
import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ships

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        
        listLabel = QLabel('&List')
        self.listWidget=QListWidget()
        listLabel.setBuddy(self.listWidget)
        listLayout = QVBoxLayout()
        listLayout.addWidget(listLabel)
        listLayout.addWidget(self.listWidget)
        
        
        tableLabel = QLabel('&Table')
        self.tableWidget = QTableWidget()
        tableLabel.setBuddy(self.tableWidget)
        tableLayout = QVBoxLayout()
        tableLayout.addWidget(tableLabel)
        tableLayout.addWidget(self.tableWidget)
        
        treeLabel = QLabel('Tre&e')
        self.treeWidget = QTreeWidget()
        treeLabel.setBuddy(self.treeWidget)
        treeLayout = QVBoxLayout()
        treeLayout.addWidget(treeLabel)
        treeLayout.addWidget(self.treeWidget)
        
        addButton = QPushButton('&Add Ship')
        removeButton = QPushButton('&Remove Ship')
        quitButton = QPushButton('&Quit')        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(addButton)
        buttonLayout.addWidget(removeButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(quitButton)
        
        itemLayout = QHBoxLayout()
        itemLayout.addLayout(listLayout)
        itemLayout.addLayout(tableLayout)
        itemLayout.addLayout(treeLayout)        
        
        layout = QVBoxLayout()
        layout.addLayout(itemLayout)
        layout.addLayout(buttonLayout)
        
        self.setLayout(layout)
    
        self.ships = ships.ShipContainer("ships.data")
        
        self.initialLoad()
        
    def initialLoad(self):
        if not QFile.exists(self.ships.filename):
            for ship in self.ships.generateFakeShips():
                self.ships.addShip(ship)
                
            self.ships.dirty = False
        else:
            try:
                self.ships.load()
            except IOError as e:
                QMessageBox.warning(self, "Ships - Error","Fail to Load : {0}".format(e))
        
        self.populateList()
        self.populateTable()
        self.populateTree()
            
    def populateList(self, selectedShip=None):
        selected = None
        self.listWidget.clear()
        
        for ship in self.ships.inOrder():            
            item = QListWidgetItem(QString("%1 of %2/%3 (%L4)").arg(ship.name).arg(ship.owner).arg(ship.country).arg(ship.teu))
            self.listWidget.addItem(item)
            
            if selectedShip is not None and selectedShip == id(ship):
                selected = item
                
        if selected is not None:
            selected.setSelected(True)
            self.listWidget.setCurrentItem(selected)
            
        
    def populateTable(self, selectedShip=None):
        selected = None
        self.tableWidget.clear()
        
        headers = ["Name","Owner","Country","Description","TEU"]
        
        
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setRowCount(len(self.ships))
        
        self.tableWidget.setHorizontalHeaderLabels(headers)
        
        for row, ship in enumerate(self.ships):
            item = QTableWidgetItem(ship.name)
            item.setData(Qt.UserRole, QVariant(int(id(ship))))
            self.tableWidget.setItem(row, 0, item)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(ship.owner))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(ship.country))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(ship.description))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(ship.teu))
            
    
    def populateTree(self):
        pass

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()        
        
        