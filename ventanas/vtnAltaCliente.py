# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAltaCliente.ui'
#
# Created: Tue Oct 28 16:55:59 2014
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

class Ui_vtnAltaCliente(object):
    def setupUi(self, vtnAltaCliente):
        vtnAltaCliente.setObjectName(_fromUtf8("vtnAltaCliente"))
        vtnAltaCliente.resize(568, 183)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaCliente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnAltaCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtTel = QtGui.QLineEdit(vtnAltaCliente)
        self.txtTel.setObjectName(_fromUtf8("txtTel"))
        self.gridLayout.addWidget(self.txtTel, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnAltaCliente)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.txtDNI = QtGui.QLineEdit(vtnAltaCliente)
        self.txtDNI.setObjectName(_fromUtf8("txtDNI"))
        self.gridLayout.addWidget(self.txtDNI, 1, 1, 1, 1)
        self.txtNomyApell = QtGui.QLineEdit(vtnAltaCliente)
        self.txtNomyApell.setObjectName(_fromUtf8("txtNomyApell"))
        self.gridLayout.addWidget(self.txtNomyApell, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(vtnAltaCliente)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.txtDir = QtGui.QLineEdit(vtnAltaCliente)
        self.txtDir.setObjectName(_fromUtf8("txtDir"))
        self.gridLayout.addWidget(self.txtDir, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAltaCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaCliente)
        vtnAltaCliente.setTabOrder(self.txtNomyApell, self.txtDNI)
        vtnAltaCliente.setTabOrder(self.txtDNI, self.txtDir)
        vtnAltaCliente.setTabOrder(self.txtDir, self.txtTel)
        vtnAltaCliente.setTabOrder(self.txtTel, self.buttonBox)

    def retranslateUi(self, vtnAltaCliente):
        vtnAltaCliente.setWindowTitle(_translate("vtnAltaCliente", "Alta Cliente", None))
        self.label.setText(_translate("vtnAltaCliente", "Nombre y Apellido", None))
        self.label_4.setText(_translate("vtnAltaCliente", "* Teléfono", None))
        self.label_3.setText(_translate("vtnAltaCliente", "Dirección", None))
        self.label_2.setText(_translate("vtnAltaCliente", "DNI", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaCliente = QtGui.QWidget()
    ui = Ui_vtnAltaCliente()
    ui.setupUi(vtnAltaCliente)
    vtnAltaCliente.show()
    sys.exit(app.exec_())

