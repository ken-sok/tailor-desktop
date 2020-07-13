from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
#import sqlite3
import time
import os
#from final1 import *
from connection import connection, cursor, close_connection
from psycopg2.extensions import AsIs
class InsertDialog(QDialog):
    def openWindow(self):
        self.Window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        

    def __init__(self, *args, **kwargs):
        super(InsertDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Register")

        self.setWindowTitle("Add Customer")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        self.setWindowTitle("Insert Customer Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        
        layout = QVBoxLayout()

        #change here ################################################################
        self.nameinput = QLineEdit()
        self.nameinput.setPlaceholderText("Name")
        layout.addWidget(self.nameinput)

        self.mobileinput = QLineEdit()
        self.mobileinput.setPlaceholderText("Mobile No.")
        layout.addWidget(self.mobileinput)

        self.addressinput = QLineEdit()
        self.addressinput.setPlaceholderText("Address")
        layout.addWidget(self.addressinput)

        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    
    
        
    

class SearchDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(SearchDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Search")

        self.setWindowTitle("Search user")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.searchcustomer)
        layout = QVBoxLayout()

        self.searchinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.searchinput.setValidator(self.onlyInt)
        self.searchinput.setPlaceholderText("Customer ID")
        layout.addWidget(self.searchinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)
############################################################################
    def searchcustomer(self):

        searchrol = ""
        searchrol = self.searchinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            result = self.c.execute("SELECT * from customer WHERE roll="+str(searchrol))
            row = result.fetchone()
            serachresult = "Rollno : "+str(row[0])+'\n'+"Name : "+str(row[1])+'\n'+"Measurement : "+str(row[3])+'\n'+"Address : "+str(row[4])
            QMessageBox.information(QMessageBox(), 'Successful', serachresult)
            self.conn.commit()
            self.c.close()
            self.conn.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Find customer from the database.')

class DeleteDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(DeleteDialog, self).__init__(*args, **kwargs)

        self.QBtn = QPushButton()
        self.QBtn.setText("Delete")

        self.setWindowTitle("Delete Customer")
        self.setFixedWidth(300)
        self.setFixedHeight(100)
        self.QBtn.clicked.connect(self.deletecustomer)
        layout = QVBoxLayout()

        self.deleteinput = QLineEdit()
        self.onlyInt = QIntValidator()
        self.deleteinput.setValidator(self.onlyInt)
        self.deleteinput.setPlaceholderText("Customer ID")
        layout.addWidget(self.deleteinput)
        layout.addWidget(self.QBtn)
        self.setLayout(layout)

    def deletecustomer(self):

        delrol = ""
        delrol = self.deleteinput.text()
        try:
            self.conn = sqlite3.connect("database.db")
            self.c = self.conn.cursor()
            self.c.execute("DELETE from customer WHERE roll="+str(delrol))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            QMessageBox.information(QMessageBox(),'Successful','Deleted From Table Successful')
            self.close()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Could not Delete customer from the database.')
########################################################################################################################

class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowIcon(QIcon('icon/g2.png'))  #window icon

        '''
        self.conn = sqlite3.connect("database.db")
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS customer(roll INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,mobile INTEGER,address TEXT)")
        self.c.close()
        '''
        file_menu = self.menuBar().addMenu("&File")

        help_menu = self.menuBar().addMenu("&About")
        self.setWindowTitle("All Order List")
        self.setMinimumSize(800, 600)

        self.tableWidget = QTableWidget()
        self.setCentralWidget(self.tableWidget)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        
        self.tableWidget.setHorizontalHeaderLabels(("Order ID", "Price", "Customer Name", "Customer ID", "Staff","Date Ordered", "Deadline", "Progress"))
        self.tableWidget.cellClicked.connect(self.getDataComboBox)

        toolbar = QToolBar()

        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        statusbar = QStatusBar()
        self.setStatusBar(statusbar)

        btn_ac_adduser = QAction(QIcon("icon/add1.jpg"), "Add Customer", self)   #add customer icon
        btn_ac_adduser.triggered.connect(self.insert)
        btn_ac_adduser.setStatusTip("Add Customer")
        toolbar.addAction(btn_ac_adduser)

        btn_ac_refresh = QAction(QIcon("icon/r3.png"),"Refresh",self)   #refresh icon
        btn_ac_refresh.triggered.connect(self.loaddata)
        btn_ac_refresh.setStatusTip("Refresh Table")
        toolbar.addAction(btn_ac_refresh)

        btn_ac_search = QAction(QIcon("icon/s1.png"), "Search", self)  #search icon
        btn_ac_search.triggered.connect(self.search)
        btn_ac_search.setStatusTip("Search User")
        toolbar.addAction(btn_ac_search)

        btn_ac_delete = QAction(QIcon("icon/d1.png"), "Delete", self)
        btn_ac_delete.triggered.connect(self.delete)
        btn_ac_delete.setStatusTip("Delete User")
        toolbar.addAction(btn_ac_delete)
        ''''
        data_action = QAction(QIcon("data.png"),"Insert Data", self)
        data_action.triggered.connect(self.open)
        file_menu.addAction(data_action)
        '''
        adduser_action = QAction(QIcon("icon/add1.jpg"),"Insert Customer", self)
        adduser_action.triggered.connect(self.insert)
        file_menu.addAction(adduser_action)

        searchuser_action = QAction(QIcon("icon/s1.png"), "Search Customer", self)
        searchuser_action.triggered.connect(self.search)
        file_menu.addAction(searchuser_action)

        deluser_action = QAction(QIcon("icon/d1.png"), "Delete", self)
        deluser_action.triggered.connect(self.delete)
        file_menu.addAction(deluser_action)


        about_action = QAction(QIcon("icon/i1.png"),"Developer", self)  #info icon
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        #set font size 
        

    def loaddata(self):
        

        #table_name = 'orders'
        print("Table Before updating record ")
        
        sql_select_query = 'SELECT "ID" ,price,customer_name, customer_id, staff, date_ordered, deadline FROM %s'
        record_to_query = (AsIs("orders"),)
        cursor.execute(sql_select_query, record_to_query)
        all_rows = cursor.fetchall()

        
        

        for row in all_rows:
            print(row)

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(all_rows):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                print(str(data))
                self.tableWidget.setItem(row_number, column_number,QTableWidgetItem(str(data)))
                self.tableWidget.setRowHeight(row_number, 50)
                if (column_number == 2): 
                    font = QtGui.QFont()
                    font.setPointSize(30)
                    self.tableWidget.setFont(font)
                '''
                #combo box
                combo_box_options = [("0%",1),("25%",2),("50%",3),("75%",4), ("100%",5)]
                #value_in_db = [1, 2, 3, 4, 5]
                combo = QComboBox()
                combo.setCurrentIndex(0) 
                
                for (t, i) in combo_box_options:
                    combo.addItem(t,i)
                    combo.currentIndexChanged.connect(self.selectionchange)
                    self.tableWidget.setCellWidget(row_number,7,combo)
                ''' 

        for row_number in range(0,len(all_rows)): 
            #combo box
            combo_box_options1 = ["0%","25%","50%","75%", "100%"]
            #combo_box_options2 = [1,2,3,4,5]
            #combo_box_options = [("0%",1),("25%",2),("50%",3),("75%",4), ("100%",5)]
            #value_in_db = [1, 2, 3, 4, 5]
            combo = QComboBox()

            #get current index from db
            combo.setCurrentIndex(0) 
            #for (t, i) in combo_box_options:
            combo.addItems(combo_box_options1)
            combo.currentIndexChanged.connect(self.getDataComboBox)
            self.tableWidget.setCellWidget(row_number,7,combo)
                

                
        
    def handlePaintRequest(self, printer):
        document = QTextDocument()
        cursor = QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QTextCursor.NextCell)
                
                

        document.print_(printer)

    def insert(self):
        dlg = InsertDialog()
        dlg.exec_()

    def delete(self):
        dlg = DeleteDialog()
        dlg.exec_()

    def search(self):
        dlg = SearchDialog()
        dlg.exec_()

    def about(self):
        dlg = AboutDialog()
        dlg.exec_()

    
    def getDataComboBox(self, index):
        print(index)
        #print(row_number)
        rows = sorted(set(index.row() for index in
                      self.tableWidget.selectedIndexes()))
        for row in rows:
            #print('Row %d is selected' % row)
            #send new progress to database 
            print(index)
app = QApplication(sys.argv)
if(QDialog.Accepted == True):
    window = MainWindow()
    window.show()
    window.loaddata()
sys.exit(app.exec_())
