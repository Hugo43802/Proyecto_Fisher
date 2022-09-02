from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from Ui_Inicial import *
import Despacho
import sys

class VentanaUi(QtWidgets.QMainWindow, Ui_Inicio):
    
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.Aceptar.clicked.connect(self.Aceptar_clic)
        #self.Automatico.clicked.connect(self.Automatico_Select)
        
    def Aceptar_clic(self):
            if self.Automatico.isChecked():
                    self.label.setText("Lo logré")
  
def run():
        app = QtWidgets.QApplication([])
        window = VentanaUi()
        window.show()
        sys.exit(app.exec_())

if __name__== "__main__":
        run()

