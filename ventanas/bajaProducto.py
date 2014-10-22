# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaProducto.ui'
#
# Created: Thu Oct 16 15:32:18 2014
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

class Ui_vtnBajaProducto(object):
    def setupUi(self, vtnBajaProducto):
        vtnBajaProducto.setObjectName(_fromUtf8("vtnBajaProducto"))
        vtnBajaProducto.resize(582, 257)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineCodBarra = QtGui.QLineEdit(vtnBajaProducto)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout.addWidget(self.lineCodBarra, 0, 1, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnBajaProducto)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 2, 1, 1)
        self.label = QtGui.QLabel(vtnBajaProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.tablaProducto = QtGui.QTableWidget(vtnBajaProducto)
        self.tablaProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaProducto.setObjectName(_fromUtf8("tablaProducto"))
        self.tablaProducto.setColumnCount(0)
        self.tablaProducto.setRowCount(0)
        self.tablaProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tablaProducto.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaProducto, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaProducto)
        vtnBajaProducto.setTabOrder(self.lineCodBarra, self.btnBuscar)
        vtnBajaProducto.setTabOrder(self.btnBuscar, self.tablaProducto)
        vtnBajaProducto.setTabOrder(self.tablaProducto, self.buttonBox)

    def retranslateUi(self, vtnBajaProducto):
        vtnBajaProducto.setWindowTitle(_translate("vtnBajaProducto", "Baja Producto", None))
        self.lineCodBarra.setStatusTip(_translate("vtnBajaProducto", "Ingrese código de barra del Producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnBajaProducto", "codigo", None))
        self.btnBuscar.setText(_translate("vtnBajaProducto", "Buscar", None))
        self.label.setText(_translate("vtnBajaProducto", "Código de Barra", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaProducto = QtGui.QWidget()
    ui = Ui_vtnBajaProducto()
    ui.setupUi(vtnBajaProducto)
    vtnBajaProducto.show()
    sys.exit(app.exec_())

