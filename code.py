# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'code.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import openpyxl as xl
import pandas as pd


class dataframe:
    def __init__(self):
        data = {
            'col x': list('ABCD'),
            'col y': list('EFGH'), }
        self.value = pd.DataFrame(data)


y = 'no'


class path:
    def __init__(self, value):
        self.value = value


df = dataframe()
Path = path('')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QPushButton{\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #050a0e;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: black;\n"
                                 "    font-size: 26px;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: lightblue;;\n"
                                 "}\n"
                                 "QPushButton:hover{\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #050a0e;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #d3dae3;\n"
                                 "    font-size: 26px;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: #1c1f1f;\n"
                                 "}\n"
                                 "QPushButton:pressed{\n"
                                 "    font-size:26px;\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #050a0e;\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #d3dae3;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: #2c2f2f;\n"
                                 "}\n"
                                 "QPushButton:disabled{\n"
                                 "    border-style: solid;\n"
                                 "    border-top-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                 "    border-right-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(217, 217, 217), stop:1 rgb(227, 227, 227));\n"
                                 "    border-left-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.5, stop:0 rgb(227, 227, 227), stop:1 rgb(217, 217, 217));\n"
                                 "    border-bottom-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgb(215, 215, 215), stop:1 rgb(222, 222, 222));\n"
                                 "    border-width: 1px;\n"
                                 "    border-radius: 5px;\n"
                                 "    color: #808086;\n"
                                 "    padding: 2px;\n"
                                 "    background-color: rgb(142,142,142);\n"
                                 "}\n"
                                 "QLineEdit {\n"
                                 "    border-width: 1px;\n"
                                 "    border-style: solid;\n"
                                 "    border-color: #4fa08b;\n"
                                 "    background-color: #222b2e;\n"
                                 "    color: #d3dae3;\n"
                                 "}"
                                 "QLable {\n"
                                 "    font-size: 26px;\n"
                                 "    color: #d3dae3;\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.MyTable = QtWidgets.QTableWidget(self.centralwidget)
        self.MyTable.setGeometry(QtCore.QRect(140, 270, 600, 200))
        self.MyTable.setObjectName("MyTable")
        ###############here my work ###########################
        self.MyTable.setColumnCount(3)
        self.MyTable.setRowCount(4)

        ####################################################
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.MyTable.setHorizontalHeaderItem(2, item)
        self.BrowseExcelButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseExcelButton.setGeometry(QtCore.QRect(260, 60, 144, 44))
        self.BrowseExcelButton.setObjectName("BrowseExcelButton")
        self.FirtLineButton = QtWidgets.QPushButton(self.centralwidget)
        self.FirtLineButton.setGeometry(QtCore.QRect(170, 140, 321, 81))
        self.FirtLineButton.setObjectName("FirtLineButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 500, 721, 100))
        self.label.setObjectName("label")
        self.label.setStyleSheet(
            "font-size:18px;"
        )
        ###############here my work ###########################
        self.BrowseExcelButton.clicked.connect(lambda: self.push(0))
        self.FirtLineButton.clicked.connect(lambda: self.push(1))
        ####################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        item = self.MyTable.verticalHeaderItem(0)
        self.retranslateUi(MainWindow, item, 'no')
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(40)
        font.setStrikeOut(False)

    def push(self, x):
        if (x == 0):
            self.OpenDialogBox()
        else:
            self.ShowFirstLine(Path.value)

    def ShowFirstLine(self, link):
        df.value = pd.read_excel(link)
        nRows, nColumn = df.value.shape

        self.MyTable.setColumnCount(nColumn)
        self.MyTable.setRowCount(nRows)
        print(self.MyTable.rowCount())
        for i in range(0, self.MyTable.rowCount()):
            for j in range(0, self.MyTable.columnCount()):
                self.MyTable.setItem(
                    i, j, QtWidgets.QTableWidgetItem(str(df.value.iloc[i, j])))

    def OpenDialogBox(self):
        FileName = QtWidgets.QFileDialog.getOpenFileName()
        Path.value = FileName[0]

        ####################################################

    def retranslateUi(self, MainWindow, item, y):
        if y == 'no':
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
            item = self.MyTable.verticalHeaderItem(0)
            item.setText(_translate("MainWindow", "New Row"))
            item = self.MyTable.verticalHeaderItem(1)
            item.setText(_translate("MainWindow", "New Row"))
            item = self.MyTable.verticalHeaderItem(2)
            item.setText(_translate("MainWindow", "New Row"))
            item = self.MyTable.verticalHeaderItem(3)
            item.setText(_translate("MainWindow", "New Row"))
            item = self.MyTable.horizontalHeaderItem(0)
            item.setText(_translate("MainWindow", "New Column"))
            item = self.MyTable.horizontalHeaderItem(1)
            item.setText(_translate("MainWindow", "New Column"))
            item = self.MyTable.horizontalHeaderItem(2)
            item.setText(_translate("MainWindow", "New Column"))

            self.BrowseExcelButton.setText(
                _translate("MainWindow", "browse ..."))
            self.FirtLineButton.setText(_translate(
                "MainWindow", "print few lines"))
            self.label.setText(_translate(
                "MainWindow", "important! browse excel file and than press 'print few lines'"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
