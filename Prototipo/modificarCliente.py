# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarCliente.ui'
#
# Created: Wed Sep 24 13:59:39 2014
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

class Ui_vtnModificarCliente(object):
    def setupUi(self, vtnModificarCliente):
        vtnModificarCliente.setObjectName(_fromUtf8("vtnModificarCliente"))
        vtnModificarCliente.resize(607, 204)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarCliente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnModificarCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(vtnModificarCliente)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtGui.QLabel(vtnModificarCliente)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnModificarCliente)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnModificarCliente)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(vtnModificarCliente)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnModificarCliente)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.lineEdit_3 = QtGui.QLineEdit(vtnModificarCliente)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarCliente)
        vtnModificarCliente.setTabOrder(self.lineEdit, self.lineEdit_2)
        vtnModificarCliente.setTabOrder(self.lineEdit_2, self.pushButton)
        vtnModificarCliente.setTabOrder(self.pushButton, self.lineEdit_3)
        vtnModificarCliente.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        vtnModificarCliente.setTabOrder(self.lineEdit_4, self.buttonBox)

    def retranslateUi(self, vtnModificarCliente):
        vtnModificarCliente.setWindowTitle(_translate("vtnModificarCliente", "Modificar Cliente", None))
        self.label.setText(_translate("vtnModificarCliente", "Nombre y Apellido", None))
        self.label_2.setText(_translate("vtnModificarCliente", "DNI", None))
        self.label_4.setText(_translate("vtnModificarCliente", "Teléfono", None))
        self.label_3.setText(_translate("vtnModificarCliente", "Dirección", None))
        self.pushButton.setText(_translate("vtnModificarCliente", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarCliente = QtGui.QWidget()
    ui = Ui_vtnModificarCliente()
    ui.setupUi(vtnModificarCliente)
    vtnModificarCliente.show()
    sys.exit(app.exec_())
