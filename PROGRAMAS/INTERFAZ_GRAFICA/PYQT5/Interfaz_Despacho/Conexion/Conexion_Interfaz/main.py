from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from PyQt5.QtWidgets import QMessageBox
from Ui_carga import *
from Ui_recepcion import *
import Recepcion
import ftrobopy
import sys

class CargaUi(QtWidgets.QMainWindow, Ui_Carga):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        ## Elementos de la interfaz
        self.label.setText(f"Conectado al proceso de Despacho")
        
        #Acción del boton
        self.Abrir.clicked.connect(self.btn1_clic)
               
    def btn1_clic(self): 
        if self.radioButton.isChecked():
            #Activar la segunda ventana al accionar el clic        
            self.segunda = Recepcion.Recepcion()
            self.segunda.show()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Por favor seleccione una opción")
            retval = msg.exec_()
        
def run():
    app = QtWidgets.QApplication([])
    window = CargaUi()
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    run()