from PyQt5 import QtCore, QtWidgets, QtGui
from Ui_recepcion import *
import sys

class Recepcion(QtWidgets.QMainWindow, Ui_Recepcion):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)