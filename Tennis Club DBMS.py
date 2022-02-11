from PyQt5 import QtCore, QtGui, QtWidgets
import base64
from PyQt5.QtGui import QIcon
from logging import exception
from re import L
from PyQt5.sip import delete

import mysql.connector as sqltor
#from PyQt5.QtWidgets import QMessageBox

password=password

conn=sqltor.connect(host="localhost", user="root", password=password, database="tennis")
cur=conn.cursor()



#Increase window size
class Ui_MainWindow(object):

    def display(self):
        conn=sqltor.connect(host="localhost", user="root", password=password, database="tennis")
        cur=conn.cursor()
        query='select * from club'
        cur.execute(query)
        data=cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(data):
            self.tableWidget.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(column_data)))

    

    
    def search(self):
        conn=sqltor.connect(host="localhost", user="root", password=password, database="tennis")
        cur=conn.cursor()
        search_value=self.input_PID.text()
        if search_value!=None:
            print(search_value)
            query='select * from club where PID="{}" ;'.format(search_value)
            cur.execute(query)
            data=cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(column_data)))
    
    def update(self):
        
        conn=sqltor.connect(host="localhost", user="root", password=password, database="tennis")
        cur=conn.cursor()
        update_value=self.input_PID.text()
        if update_value!=None:
            print(update_value)
            query='select * from club where PID="{}" ;'.format(update_value)
            cur.execute(query)
            data=cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(column_data)))

        PID = self.input_PID.text()
        Name = self.input_Name.text()
        Age=int(self.input_Age.text())
        Titles=self.input_Titles.text()
        Sex=self.input_Sex.text()
        cur.execute("SET SQL_SAFE_UPDATES=0")
        update_clause="update club set Name='{}',Age='{}',Titles='{}',Sex='{}' where PID='{}';".format(Name,Age,Titles,Sex,PID)
        cur.execute(update_clause)
        conn.commit()
    
    def insert(self):
        conn=sqltor.connect(host="localhost", user="root", password=password, database="tennis")
        cur=conn.cursor()

        PID = self.input_PID.text()
        Name = self.input_Name.text()
        Age=self.input_Age.text()
        Titles=self.input_Titles.text()
        Sex=self.input_Sex.text()
        
        insert_clause="insert into club values({},'{}',{},{},'{}')".format(PID,Name,Age,Titles,Sex)
        cur.execute(insert_clause)
        conn.commit()


        cur=conn.cursor()
        final_value=self.input_PID.text()
        if final_value!=None:
            print(final_value)
            query='select * from club where PID="{}" ;'.format(final_value)
            cur.execute(query)
            data=cur.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    self.tableWidget.setItem(row_number,column_number, QtWidgets.QTableWidgetItem(str(column_data)))
        
    def delete(self):
        conn=sqltor.connect(host="localhost", user="root", password=password, database="tennis")
        cur=conn.cursor()

        PID = self.input_PID.text()

        cur.execute("select * from club where PID={} ".format(PID))
        data=cur.fetchone()
        #print(data)
        if data!=None:
                cur.execute("SET SQL_SAFE_UPDATES=0")
                cur.execute("delete from club where PID={} ".format(PID))
                conn.commit()
                conn.close()
        self.display()

        







    def setupUi(self, MainWindow):

        MainWindow.setObjectName("The Tennis Club")
        MainWindow.resize(587, 583)
        #MainWindow.setWindowIcon(QtGui.QIcon('SQL_Project_Logo.icns'))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-color: rgb(179, 23, 171);\n"
"file:///System/Library/Fonts/Supplemental/Phosphate.ttc")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 551, 261))
        self.tableWidget.setStyleSheet("font: 22pt \"Phosphate\";\n"
"gridline-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")

        
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(10)

        #self.tableWidget.verticalHeader().hide()
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()

        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.btn_display = QtWidgets.QPushButton(self.centralwidget)
        self.btn_display.setGeometry(QtCore.QRect(60, 290, 75, 26))
        self.btn_display.setStyleSheet("font: 20pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.btn_display.setObjectName("btn_display")
        self.btn_display.clicked.connect(self.display)
        
        self.btn_insert = QtWidgets.QPushButton(self.centralwidget)
        self.btn_insert.setGeometry(QtCore.QRect(160, 290, 75, 26))
        self.btn_insert.setStyleSheet("font: 20pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.btn_insert.setObjectName("btn_insert")
        self.btn_insert.clicked.connect(self.insert)
        
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(260, 290, 75, 26))
        self.btn_search.setStyleSheet("font: 20pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.search)
        
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(360, 290, 75, 26))
        self.btn_update.setStyleSheet("font: 20pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.btn_update.setObjectName("btn_update")
        self.btn_update.clicked.connect(self.update)
        
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(460, 290, 75, 26))
        self.btn_delete.setStyleSheet("font: 20pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.clicked.connect(self.delete)
        
        
        
        
        
        self.input_PID = QtWidgets.QLineEdit(self.centralwidget)
        self.input_PID.setGeometry(QtCore.QRect(170, 340, 271, 21))
        self.input_PID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_PID.setText("")
        self.input_PID.setObjectName("input_PID")
        
        self.input_Name = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Name.setGeometry(QtCore.QRect(170, 380, 271, 21))
        self.input_Name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_Name.setText("")
        self.input_Name.setObjectName("input_Name")
        
        self.input_Age = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Age.setGeometry(QtCore.QRect(170, 420, 271, 21))
        self.input_Age.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_Age.setText("")
        self.input_Age.setObjectName("input_Age")
        
        self.input_Titles = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Titles.setGeometry(QtCore.QRect(170, 460, 271, 21))
        self.input_Titles.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_Titles.setText("")
        self.input_Titles.setObjectName("input_Titles")
        
        self.input_Sex = QtWidgets.QLineEdit(self.centralwidget)
        self.input_Sex.setGeometry(QtCore.QRect(170, 500, 271, 21))
        self.input_Sex.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_Sex.setText("")
        self.input_Sex.setObjectName("input_Sex")
        
        
        
        
        
        
        self.label_PID = QtWidgets.QLabel(self.centralwidget)
        self.label_PID.setGeometry(QtCore.QRect(60, 340, 31, 21))
        self.label_PID.setStyleSheet("font: 18pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.label_PID.setObjectName("label_PID")
        
        self.label_Name = QtWidgets.QLabel(self.centralwidget)
        self.label_Name.setGeometry(QtCore.QRect(60, 380, 51, 21))
        self.label_Name.setStyleSheet("font: 18pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.label_Name.setObjectName("label_Name")
        
        self.label_Age = QtWidgets.QLabel(self.centralwidget)
        self.label_Age.setGeometry(QtCore.QRect(60, 420, 51, 21))
        self.label_Age.setStyleSheet("font: 18pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.label_Age.setObjectName("label_Age")
        
        self.label_Titles = QtWidgets.QLabel(self.centralwidget)
        self.label_Titles.setGeometry(QtCore.QRect(60, 460, 51, 21))
        self.label_Titles.setStyleSheet("font: 18pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.label_Titles.setObjectName("label_Titles")
        
        self.label_Sex = QtWidgets.QLabel(self.centralwidget)
        self.label_Sex.setGeometry(QtCore.QRect(60, 500, 41, 21))
        self.label_Sex.setStyleSheet("font: 18pt \"Phosphate\";\n"
"color: rgb(255, 255, 255);")
        self.label_Sex.setObjectName("label_Sex")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.label_PID.setBuddy(self.input_PID)
        self.label_Name.setBuddy(self.input_Name)
        self.label_Age.setBuddy(self.input_Age)
        self.label_Titles.setBuddy(self.input_Titles)
        self.label_Sex.setBuddy(self.input_Sex)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("The Tennis Club", "The Tennis Club"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("The Tennis Club", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("The Tennis Club", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("The Tennis Club", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("The Tennis Club", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("The Tennis Club", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("The Tennis Club", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("The Tennis Club", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("The Tennis Club", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("The Tennis Club", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("The Tennis Club", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("The Tennis Club", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("The Tennis Club", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("The Tennis Club", "Age"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("The Tennis Club", "Titles"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("The Tennis Club", "Sex"))
        self.btn_display.setText(_translate("The Tennis Club", "Display"))
        self.btn_insert.setText(_translate("The Tennis Club", "Insert"))
        self.btn_search.setText(_translate("The Tennis Club", "Search"))
        self.btn_update.setText(_translate("The Tennis Club", "Update"))
        self.btn_delete.setText(_translate("The Tennis Club", "Delete"))
        self.label_PID.setText(_translate("The Tennis Club", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">PID</span></p></body></html>"))
        self.label_Name.setText(_translate("The Tennis Club", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Name</span></p></body></html>"))
        self.label_Age.setText(_translate("The Tennis Club", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Age</span></p></body></html>"))
        self.label_Titles.setText(_translate("The Tennis Club", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Titles</span></p></body></html>"))
        self.label_Sex.setText(_translate("The Tennis Club", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Sex</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    app.setWindowIcon(QIcon('/Users/Deepa/Downloads/Projects/SQL_Project/trials_for_sql/Finalized_stuff/GUI/Tennis Club Logo.png'))
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
