# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\Mi unidad\UNIVERSIDAD MILITAR\2021-2022\PROYECTO_FISCHER_PYTHON\PROGRAMAS\INTERFAZ_GRAFICA\PYQT5\Segunda_Prueba\SegundaVentana.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SegundaVentana(object):
    def setupUi(self, SegundaVentana):
        SegundaVentana.setObjectName("SegundaVentana")
        SegundaVentana.resize(332, 243)
        self.centralwidget = QtWidgets.QWidget(SegundaVentana)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(90, 50, 158, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setAcceptDrops(True)
        self.plainTextEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(100, 90, 131, 71))
        self.pushButton2.setObjectName("pushButton2")
        SegundaVentana.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SegundaVentana)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 332, 21))
        self.menubar.setObjectName("menubar")
        SegundaVentana.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SegundaVentana)
        self.statusbar.setObjectName("statusbar")
        SegundaVentana.setStatusBar(self.statusbar)

        self.retranslateUi(SegundaVentana)
        QtCore.QMetaObject.connectSlotsByName(SegundaVentana)

    def retranslateUi(self, SegundaVentana):
        _translate = QtCore.QCoreApplication.translate
        SegundaVentana.setWindowTitle(_translate("SegundaVentana", "MainWindow"))
        self.pushButton2.setText(_translate("SegundaVentana", "PushButton"))
