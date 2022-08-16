from PyQt5 import QtWidgets
from Ui_conexion import *
import ftrobopy
import sys

# Ui_MainWindow viene de la clase del archivo Ui_conexion.py
class DespachoUi(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.label.setText("¡No Conectado!")
        
        plc = ftrobopy.ftrobopy("192.168.0.102")
        nom_Dispositivo = plc.getDevicename() #guarda en variable el nombre del dispositivo o no sirve
        firmware = plc.getFirmwareVersion()
        
        #label
        self.label.setText(f"Conectado a {nom_Dispositivo} - {firmware}")
        
        
        

def run():
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    window = DespachoUi()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()