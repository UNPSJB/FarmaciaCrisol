# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnListar.ui'
#
# Created: Tue Oct 28 16:56:00 2014
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

class Ui_vtnListar(object):
    def setupUi(self, vtnListar):
        vtnListar.setObjectName(_fromUtf8("vtnListar"))
        vtnListar.resize(418, 149)
        self.verticalLayout = QtGui.QVBoxLayout(vtnListar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnListar)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.dateEdit = QtGui.QDateEdit(vtnListar)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_2 = QtGui.QLabel(vtnListar)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.dateEdit_2 = QtGui.QDateEdit(vtnListar)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.gridLayout.addWidget(self.dateEdit_2, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.comboBox = QtGui.QComboBox(vtnListar)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2, QtCore.Qt.AlignLeft)
        self.pushButton = QtGui.QPushButton(vtnListar)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 3, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnListar)
        QtCore.QMetaObject.connectSlotsByName(vtnListar)
        vtnListar.setTabOrder(self.comboBox, self.dateEdit)
        vtnListar.setTabOrder(self.dateEdit, self.dateEdit_2)

    def retranslateUi(self, vtnListar):
        vtnListar.setWindowTitle(_translate("vtnListar", "Listar", None))
        self.label.setText(_translate("vtnListar", "Fecha Desde", None))
        self.label_2.setText(_translate("vtnListar", "Fecha Hasta", None))
        self.comboBox.setItemText(0, _translate("vtnListar", "Facturas Liquidadas Pendientes de Cobro", None))
        self.comboBox.setItemText(1, _translate("vtnListar", "Productos en Stock", None))
        self.comboBox.setItemText(2, _translate("vtnListar", "Ventas Realizadas", None))
        self.comboBox.setItemText(3, _translate("vtnListar", "Clientes", None))
        self.pushButton.setText(_translate("vtnListar", "Listar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnListar = QtGui.QWidget()
    ui = Ui_vtnListar()
    ui.setupUi(vtnListar)
    vtnListar.show()
    sys.exit(app.exec_())

