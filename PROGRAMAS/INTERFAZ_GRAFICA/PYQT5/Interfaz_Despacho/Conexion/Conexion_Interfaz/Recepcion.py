from PyQt5 import QtCore, QtWidgets, QtGui
from Ui_recepcion import *
import sys
import ftrobopy

class Recepcion(QtWidgets.QMainWindow, Ui_Recepcion):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
    
    plc = ftrobopy.ftrobopy("192.168.0.117")