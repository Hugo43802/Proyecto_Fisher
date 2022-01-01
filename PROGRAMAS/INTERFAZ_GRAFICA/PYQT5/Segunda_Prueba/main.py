import sys
from PyQt5 import QtWidgets, QtCore
from Ui_PrimeraVentana import *
from Ui_SegundaVentana import *
import SecVentana

class PrimeraVentana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        # Para saber si está seleccionado toggled
        # self.radioButton.toggled.connect(self.seleccionado)

        self.pushButton.clicked.connect(self.btn1_clic)

    def btn1_clic(self):
        # Verifica si el radiobutton está seleccionado
        if self.radioButton.isChecked() == True:
            # Se instancia del archivo SecVentana la clase SegundaVentana
            self.segunda = SecVentana.SegundaVentana()
            self.segunda.show()
            print(self.radioButton.text(), "Está seleccionado")
            self.radioButton.setChecked(False)

def run():
    app = QtWidgets.QApplication([])
    app.setStyle("Fusion")
    window = PrimeraVentana()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()