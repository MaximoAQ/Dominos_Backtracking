from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sys


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(920, 515)
        MainWindow.setWindowTitle("Dominosa")   
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        #self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)

        self.font = QtGui.QFont()
        self.font.setFamily("Arial Rounded MT Bold")
        self.font.setPointSize(20)   


        self.comboBox.setGeometry(QtCore.QRect(550, 450, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(750, 450, 93, 28))
        self.pushButton.setObjectName("pushButton")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 131, 31))



        self.label.setFont(self.font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 20, 151, 31))


        self.label_2.setFont(self.font)
        self.label_2.setObjectName("label_2")


        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 450, 201, 31))
        self.lineEdit.setObjectName("lineEdit")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 450, 41, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 440, 101, 41))


        self.label_3.setFont(self.font)
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 450, 71, 31))


        self.label_4.setFont(self.font)
        self.label_4.setObjectName("label_4")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Brute Force"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Backtracking"))
        self.pushButton.setText(_translate("MainWindow", "Ejecutar"))
        self.label.setText(_translate("MainWindow", "Domino"))
        self.label_2.setText(_translate("MainWindow", "Solucion"))
        self.label_3.setText(_translate("MainWindow", "Array"))
        self.label_4.setText(_translate("MainWindow", "Size"))








def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
   main()