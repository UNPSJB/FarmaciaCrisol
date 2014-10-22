# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresar.ui'
#
# Created: Thu Oct 16 15:32:19 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_vtnIngresar(object):
    def setupUi(self, vtnIngresar):
        vtnIngresar.setObjectName(_fromUtf8("vtnIngresar"))
        vtnIngresar.resize(484, 113)
        self.verticalLayout = QtGui.QVBoxLayout(vtnIngresar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnIngresar)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(vtnIngresar)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.txtUsuario = QtGui.QLineEdit(vtnIngresar)
        self.txtUsuario.setObjectName(_fromUtf8("txtUsuario"))
        self.gridLayout.addWidget(self.txtUsuario, 0, 1, 1, 1)
        self.txtContrasenia = QtGui.QLineEdit(vtnIngresar)
        self.txtContrasenia.setEchoMode(QtGui.QLineEdit.Password)
        self.txtContrasenia.setObjectName(_fromUtf8("txtContrasenia"))
        self.gridLayout.addWidget(self.txtContrasenia, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnIngresar)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnIngresar)
        QtCore.QMetaObject.connectSlotsByName(vtnIngresar)

    def retranslateUi(self, vtnIngresar):
        vtnIngresar.setWindowTitle(_translate("vtnIngresar", "Ingresar", None))
        self.label.setText(_translate("vtnIngresar", "Usuario", None))
        self.label_2.setText(_translate("vtnIngresar", "Contraseña", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnIngresar = QtGui.QWidget()
    ui = Ui_vtnIngresar()
    ui.setupUi(vtnIngresar)
    vtnIngresar.show()
    sys.exit(app.exec_())

