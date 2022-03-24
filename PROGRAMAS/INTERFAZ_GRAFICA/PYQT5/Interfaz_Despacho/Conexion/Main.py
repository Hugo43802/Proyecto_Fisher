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
        
        plc = ftrobopy.ftrobopy("192.168.0.100")
        nom_Dispositivo = plc.getDevicename() #guarda en variable el nombre del dispositivo o no sirve
        firmware = plc.getFirmwareVersion()
        
        #PlainTextEdit
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(f"Conectado a {nom_Dispositivo} - {firmware}")
        

def run():
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    window = DespachoUi()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()