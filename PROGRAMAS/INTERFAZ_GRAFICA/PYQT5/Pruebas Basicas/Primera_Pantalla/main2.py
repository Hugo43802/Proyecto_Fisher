import sys
from PyQt5 import QtWidgets, Qt, QtCore
from Ui_prueba import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        ## Elementos de la interfaz

        # Se llama el botón de la interfaz compilada y se conecta a la función clicked
        self.pushButton_2.clicked.connect(self.btn2_clic)
    
    def btn2_clic(self):
        texto = self.textEdit.toPlainText()
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setText(texto)
        # El mejor para utilizar y mostrar es plaintextEdit
        self.plainTextEdit.setPlainText(texto)


def run():
    app = QtWidgets.QApplication([])
    app.setStyle("Oxygen")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run()
