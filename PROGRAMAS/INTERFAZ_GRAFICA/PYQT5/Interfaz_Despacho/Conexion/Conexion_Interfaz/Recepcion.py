from PyQt5 import QtCore, QtWidgets, QtGui
from Ui_recepcion import *
import sys
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.0.117")

class Recepcion(QtWidgets.QMainWindow, Ui_Recepcion):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        # guarda en variable el nombre del dispositivo o no sirve
        nom_Dispositivo = plc.getDevicename()
    
   