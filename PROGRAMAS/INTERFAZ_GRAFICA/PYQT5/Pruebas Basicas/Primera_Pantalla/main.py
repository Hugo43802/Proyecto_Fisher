import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from Ui_prueba import *
import Ui_prueba
 
def run():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_prueba.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()
 