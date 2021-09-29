from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from qt_material import apply_stylesheet
from Helpers.misc import *
from main import *
import time


import sys


class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(980, 555)
        MainWindow.setWindowTitle("Dominosa")   
        self.centralwidget = QtWidgets.QWidget(MainWindow)



        #self.centralwidget.setObjectName("centralwidget")
        self.framePuzzle = QtWidgets.QFrame(self.centralwidget)
        self.frameSolution = QtWidgets.QFrame(self.centralwidget)

        self.font = QtGui.QFont()
        self.font.setFamily("Arial Rounded MT Bold")
        self.font.setPointSize(20)   

        #LABEL_1 DOMINO
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(185, 20, 131, 31))
        self.label.setFont(self.font)
        self.label.setObjectName("label")

        #LABEL_2 SOLUTION
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(660, 20, 151, 31))
        self.label_2.setFont(self.font)
        self.label_2.setObjectName("label_2")

        #LABEL_3 ARRAY
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 485, 101, 41))
        self.label_3.setFont(self.font)
        self.label_3.setObjectName("label_3")

        #LABEL_4 SIZE
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 490, 71, 31))
        self.label_4.setFont(self.font)
        self.label_4.setObjectName("label_4")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #CAJA DE OPCIONES
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 495, 131, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        #BOTON DE EJECUTAR
        self.buttonSolvePuzzle = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSolvePuzzle.setGeometry(QtCore.QRect(830, 495, 93, 25))
        self.buttonSolvePuzzle.setObjectName("buttonSolvePuzzle")
        self.buttonSolvePuzzle.setDisabled(True) 

        #BOTON DE COLOCAR EL GRID
        self.buttonCreatePuzzle = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCreatePuzzle.setGeometry(QtCore.QRect(710, 495, 93, 25))
        self.buttonCreatePuzzle.setObjectName("buttonCreatePuzzle")
        self.buttonCreatePuzzle.setText("Create Puzzle")
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        #CAJA PARA EL ARRAY
        #lineEditCreatePuzzle
        self.lineEditCreatePuzzle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditCreatePuzzle.setGeometry(QtCore.QRect(120, 495, 200, 30))
        self.lineEditCreatePuzzle.setObjectName("lineEditCreatePuzzle")

        #CAJA PARA EL SIZE
        #lineEditSetSize
        self.lineEditSetSize = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditSetSize.setGeometry(QtCore.QRect(450, 495, 40, 30))
        self.lineEditSetSize.setObjectName("lineEditSetSize")
       
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.buttonCreatePuzzle.clicked.connect(self.fill)
        #self.buttonSolvePuzzle.clicked.connect(self.solve1)
        self.buttonSolvePuzzle.clicked.connect(self.pressed)


        MainWindow.setCentralWidget(self.centralwidget)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Brute Force"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Backtracking"))
        self.buttonSolvePuzzle.setText(_translate("MainWindow", "Execute"))
        self.buttonCreatePuzzle.setText(_translate("MainWindow", "Put Grid"))
        self.label.setText(_translate("MainWindow", "Domino"))
        self.label_2.setText(_translate("MainWindow", "Solution"))
        self.label_3.setText(_translate("MainWindow", "Array"))
        self.label_4.setText(_translate("MainWindow", "Size"))


    def fill(self):
        self.size = self.lineEditSetSize.text()
        self.char = self.lineEditCreatePuzzle.text()

        if self.size == '' or self.char == '': 
            self.popupWrongInput("No input", "Missing size or puzzle")
            return

        try:
            self.size = int(self.size)        
            int(self.char)                  
        except ValueError:
            self.popupWrongInput("Wrong input type", "Puzzle and size input must contain only digits")
            return


        if len(self.char) != (self.size + 1)*(self.size + 2):      
            self.popupWrongInput("Wrong input", "Wrong input size or puzzle length")
            return

        self.buttonSolvePuzzle.setDisabled(False)

        self.framePuzzle.setGeometry(QtCore.QRect((550 - 50*(self.size+2))//2, (600 - 50*(self.size+1))//2, 50*(self.size+2), 50*(self.size+1)))
        while(self.framePuzzle.children()):
            self.framePuzzle.children()[0].setParent(None)

        self.framePuzzle.hide()
        for i in range(self.size + 1): 
            for j in range(self.size + 2):
                self.label = QtWidgets.QLabel(self.framePuzzle)
                self.label.setText(self.char[i * (self.size + 2) + j])
                self.label.setGeometry(QtCore.QRect(j * 40, i * 40, 40, 40))
                self.label.setFont(self.font)
                self.label.setStyleSheet(
                        ".QLabel {border: 2px solid #FF3264;border-radius: 20px;background-color: #FF3264;}")#E70D4F
                self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.framePuzzle.show()

    def solve1(self):

        solution = mainBack(int(self.size), dominosaArr(self.size, charToIntList(self.char)))

        self.frameSolution.setGeometry(
            QtCore.QRect(550 + (550 - 50 * (self.size + 2)) // 2, (600 - 50 * (self.size + 1)) // 2, 50 * (self.size + 2),
                         50 * (self.size + 1)))
        while (self.frameSolution.children()):
            self.frameSolution.children()[0].setParent(None)

        self.frameSolution.hide()

        indexTable = genIndexList(int(self.size))

        if (solution==False):
            self.popupNoSolution()
        
        elif (len(solution)!=0):
            BOARD = solutionBoard(solution,indexTable,int(self.size))
            for i in range(self.size + 1):  
                for j in range(self.size + 2):
                    self.label = QtWidgets.QLabel(self.frameSolution)
                    self.label.setText(self.char[i * (self.size + 2) + j])
                    self.label.setAlignment(QtCore.Qt.AlignCenter)
                    self.label.setFont(self.font)
                    self.label.setGeometry(QtCore.QRect(j * 40, i * 40, 40, 40))
                    if BOARD[i][j] == 'L':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-right-radius: 15px;border-bottom-right-radius: 15px;background-color: #E70D4F;}")
                        #self.label.setText('L')
                    if BOARD[i][j] == 'R':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-left-radius: 15px;border-bottom-left-radius: 15px;background-color: #E70D4F;}")
                        #self.label.setText('R')
                    if BOARD[i][j] == 'D':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-left-radius: 15px;border-top-right-radius: 15px;background-color: #E70D4F;}")
                        #self.label.setText('D')
                    if BOARD[i][j] == 'U':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-bottom-left-radius: 15px;border-bottom-right-radius: 15px;background-color: #E70D4F;}")

        elif (solution==False):
            self.popupNoSolution()
        self.frameSolution.show()
        self.buttonSolvePuzzle.setDisabled(True)

    def solve2(self):
        solution = mainBrute(int(self.size), dominosaArr(self.size, charToIntList(self.char)))

        self.frameSolution.setGeometry(
            QtCore.QRect(500 + (500 - 50 * (self.size + 2)) // 2, (600 - 50 * (self.size + 1)) // 2, 50 * (self.size + 2),
                         50 * (self.size + 1)))
        while (self.frameSolution.children()):
            self.frameSolution.children()[0].setParent(None)

        self.frameSolution.hide()

        indexTable = genIndexList(int(self.size))
        if (solution==False):
            self.popupNoSolution()
        elif (len(solution)!=0):
            BOARD = solutionBoard(solution,indexTable,int(self.size))
            for i in range(self.size + 1):  
                for j in range(self.size + 2):
                    self.label = QtWidgets.QLabel(self.frameSolution)
                    self.label.setText(self.char[i * (self.size + 2) + j])
                    self.label.setAlignment(QtCore.Qt.AlignCenter)
                    self.label.setFont(self.font)
                    self.label.setGeometry(QtCore.QRect(j * 40, i * 40, 40, 40))
                    if BOARD[i][j] == 'L':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-right-radius: 15px;border-bottom-right-radius: 15px;background-color: #FF5733;}")
                        #self.label.setText('L')
                    if BOARD[i][j] == 'R':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-left-radius: 15px;border-bottom-left-radius: 15px;background-color: #FF5733;}")
                        #self.label.setText('R')
                    if BOARD[i][j] == 'D':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-top-left-radius: 15px;border-top-right-radius: 15px;background-color: #FF5733;}")
                        #self.label.setText('D')
                    if BOARD[i][j] == 'U':  
                        self.label.setStyleSheet(
                            ".QLabel {border: 2px solid;border-bottom-left-radius: 15px;border-bottom-right-radius: 15px;background-color: #FF5733;}")#E70D4F

        elif (solution==False):
            self.popupNoSolution()
        self.frameSolution.show()
        self.buttonSolvePuzzle.setDisabled(True)        


    def popupWrongInput(self, title, text):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(title)
        msgbox.setText(text)
        msgbox.setIcon(QMessageBox.Critical)
        msgbox.setInformativeText("See help in the lower right corner")
        msgbox.setStandardButtons(QMessageBox.Close)
        msgbox.exec_()

    def popupNoSolution(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("No solution")
        msgbox.setText("No solution found for the given puzzle")
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setStandardButtons(QMessageBox.Close)
        msgbox.exec_()


    #INDICADOR DE OPCION A LA COMBO BOX
    #HACER LLAMADA AL ALGORITMO ACA
    def pressed(self):
        if (self.comboBox.currentText()=="Backtracking"):
            inicio = time.time()
            print("Backtracking selected")
            self.solve1()
            fin = time.time()
            duracion = (fin - inicio)
            print("Backtracking lasted: ",duracion," seconds")
        else:
            inicio = time.time()
            print("Brute force selected")
            self.solve2()
            fin = time.time()
            duracion = (fin - inicio)
            print("Brute Force lasted: ",duracion, " seconds")




def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(MainWindow)
    MainWindow.show()
    apply_stylesheet(app,theme = 'dark_red.xml')
    sys.exit(app.exec_())

if __name__ == "__main__":
   main()