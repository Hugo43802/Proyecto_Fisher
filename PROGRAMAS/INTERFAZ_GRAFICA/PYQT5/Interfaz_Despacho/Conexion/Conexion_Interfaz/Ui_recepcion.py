# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Recepcion.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Recepcion(object):
    def setupUi(self, Recepcion):
        Recepcion.setObjectName("Recepcion")
        Recepcion.resize(800, 161)
        self.centralwidget = QtWidgets.QWidget(Recepcion)
        self.centralwidget.setObjectName("centralwidget")
        self.Recibe = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Recibe.setGeometry(QtCore.QRect(40, 40, 711, 31))
        self.Recibe.setPlaceholderText("")
        self.Recibe.setObjectName("Recibe")
        Recepcion.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Recepcion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        Recepcion.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Recepcion)
        self.statusbar.setObjectName("statusbar")
        Recepcion.setStatusBar(self.statusbar)

        self.retranslateUi(Recepcion)
        QtCore.QMetaObject.connectSlotsByName(Recepcion)

    def retranslateUi(self, Recepcion):
        _translate = QtCore.QCoreApplication.translate
        Recepcion.setWindowTitle(_translate("Recepcion", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Recepcion = QtWidgets.QMainWindow()
    ui = Ui_Recepcion()
    ui.setupUi(Recepcion)
    Recepcion.show()
    sys.exit(app.exec_())