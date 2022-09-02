from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from Ui_despacho import * 
import ftrobopy
import sys

class DespachoUi(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        plc = ftrobopy.ftrobopy("192.168.0.117")
        
        nom_Dispositivo = plc.getDevicename() #guarda en variable el nombre del dispositivo o no sirve
        firmware = plc.getFirmwareVersion()
        
        #label
        self.label_2.setText(f"Conectado a {nom_Dispositivo} - {firmware}")

def run():
        app = QtWidgets.QApplication([])
        window = DespachoUi()
        window.show()
        sys.exit(app.exec_())

if __name__== "__main__":
        run()

