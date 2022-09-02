from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from Ui_carga import *
from Ui_recepcion import *
import Recepcion
import ftrobopy
import sys

class CargaUi(QtWidgets.QMainWindow, Ui_Carga):
    plc = ftrobopy.ftrobopy("192.168.0.117")
    
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        
        
        ## Elementos de la interfaz
             
        #Acción del boton
        self.Abrir.clicked.connect(self.btn1_clic)
        
    def btn1_clic(self, plc): 
        #Conseguir el texto de la casilla 
        texto = self.plainTextEdit.toPlainText()
        
        
        #Activar la segunda ventana al accionar el clic        
        self.segunda = Recepcion.Recepcion()
        self.segunda.show()
        
        self.label.setText("Hugo")
def run():
    app = QtWidgets.QApplication([])
    window = CargaUi()
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    run()