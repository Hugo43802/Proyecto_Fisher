from PyQt5 import QtCore, QtWidgets, QtGui, Qt
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
             
        #Acción del boton
        self.Abrir.clicked.connect(self.btn1_clic)
        
    def btn1_clic(self): 
        #Conseguir el texto de la casilla 
        texto = self.plainTextEdit.toPlainText()
        
        
        #Activar la segunda ventana al accionar el clic        
        self.segunda = Recepcion.Recepcion()
        self.segunda.show()
        
        #Se asignaa la segunda ventana lo escrito en el editText
        self.segunda.Recibe.setPlainText(texto)
        
def run():
    app = QtWidgets.QApplication([])
    window = CargaUi()
    window.show()
    sys.exit(app.exec_())

if __name__== "__main__":
    run()