import sys
from PyQt5 import QtWidgets, QtCore
from Ui_SegundaVentana import *

# En este espacio se crea la otra ventana que será llamada
class SegundaVentana(QtWidgets.QMainWindow, Ui_SegundaVentana):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)