from PyQt5 import QtCore, QtWidgets, QtGui
from Ui_carga import *
from Ui_recepcion import *
import Recepcion
import sys

class CargaUi(QtWidgets.QMainWindow, Ui_Carga):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        ## Elementos de la interfaz
        self.Abrir.clicked.connect(self.btn1_clic)
        
    def btn1_clic(self): 
        texto = self.plainTextEdit.toPlainText()
        self.label.setText(texto)
        
        self.segunda = Recepcion.Recepcion()
        self.segunda.show()
        
        self.segunda.Recibe.setPlainText(texto)
        
        
        

def run():
    app = QtWidgets.QApplication([])
    window = CargaUi()
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    run()