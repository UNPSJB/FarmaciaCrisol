# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnBajaLote.ui'
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

class Ui_vtnBajaLote(object):
    def setupUi(self, vtnBajaLote):
        vtnBajaLote.setObjectName(_fromUtf8("vtnBajaLote"))
        vtnBajaLote.resize(461, 236)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaLote)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineNumero = QtGui.QLineEdit(vtnBajaLote)
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.gridLayout.addWidget(self.lineNumero, 0, 1, 1, 1)
        self.label = QtGui.QLabel(vtnBajaLote)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnBajaLote)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 2, 1, 1)
        self.tablaLote = QtGui.QTableWidget(vtnBajaLote)
        self.tablaLote.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaLote.setObjectName(_fromUtf8("tablaLote"))
        self.tablaLote.setColumnCount(0)
        self.tablaLote.setRowCount(0)
        self.tablaLote.horizontalHeader().setDefaultSectionSize(160)
        self.tablaLote.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaLote, 1, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaLote)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaLote)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaLote)
        vtnBajaLote.setTabOrder(self.lineNumero, self.btnBuscar)
        vtnBajaLote.setTabOrder(self.btnBuscar, self.tablaLote)
        vtnBajaLote.setTabOrder(self.tablaLote, self.buttonBox)

    def retranslateUi(self, vtnBajaLote):
        vtnBajaLote.setWindowTitle(_translate("vtnBajaLote", "Baja Lote", None))
        self.lineNumero.setStatusTip(_translate("vtnBajaLote", "Ingrese número de lote (solo letras y números sin espacios)", None))
        self.lineNumero.setAccessibleDescription(_translate("vtnBajaLote", "lote", None))
        self.label.setText(_translate("vtnBajaLote", "Número", None))
        self.btnBuscar.setText(_translate("vtnBajaLote", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaLote = QtGui.QWidget()
    ui = Ui_vtnBajaLote()
    ui.setupUi(vtnBajaLote)
    vtnBajaLote.show()
    sys.exit(app.exec_())

