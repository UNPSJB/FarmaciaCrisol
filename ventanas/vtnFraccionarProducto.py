# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnFraccionarProducto.ui'
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

class Ui_vtnFraccionarProducto(object):
    def setupUi(self, vtnFraccionarProducto):
        vtnFraccionarProducto.setObjectName(_fromUtf8("vtnFraccionarProducto"))
        vtnFraccionarProducto.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnFraccionarProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnFraccionarProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(vtnFraccionarProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(vtnFraccionarProducto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineCodBarra = QtGui.QLineEdit(vtnFraccionarProducto)
        self.lineCodBarra.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout.addWidget(self.lineCodBarra, 1, 2, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnFraccionarProducto)
        self.btnBuscar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 1, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnFraccionarProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 2, 1, 2)
        self.tableFraccionable = QtGui.QTableWidget(vtnFraccionarProducto)
        self.tableFraccionable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableFraccionable.setObjectName(_fromUtf8("tableFraccionable"))
        self.tableFraccionable.setColumnCount(0)
        self.tableFraccionable.setRowCount(0)
        self.tableFraccionable.horizontalHeader().setDefaultSectionSize(160)
        self.tableFraccionable.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableFraccionable, 4, 1, 1, 3)
        self.tableProducto = QtGui.QTableWidget(vtnFraccionarProducto)
        self.tableProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableProducto.setObjectName(_fromUtf8("tableProducto"))
        self.tableProducto.setColumnCount(0)
        self.tableProducto.setRowCount(0)
        self.tableProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tableProducto.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableProducto, 2, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnFraccionarProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnFraccionarProducto)
        vtnFraccionarProducto.setTabOrder(self.lineCodBarra, self.btnBuscar)
        vtnFraccionarProducto.setTabOrder(self.btnBuscar, self.tableProducto)
        vtnFraccionarProducto.setTabOrder(self.tableProducto, self.tableFraccionable)
        vtnFraccionarProducto.setTabOrder(self.tableFraccionable, self.buttonBox)

    def retranslateUi(self, vtnFraccionarProducto):
        vtnFraccionarProducto.setWindowTitle(_translate("vtnFraccionarProducto", "Fraccionar Producto", None))
        self.label.setText(_translate("vtnFraccionarProducto", "Producto", None))
        self.label_2.setText(_translate("vtnFraccionarProducto", "Código de Barra", None))
        self.label_3.setText(_translate("vtnFraccionarProducto", "Fraccionable", None))
        self.lineCodBarra.setStatusTip(_translate("vtnFraccionarProducto", "Ingrese código de barra del Producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnFraccionarProducto", "codigo", None))
        self.btnBuscar.setText(_translate("vtnFraccionarProducto", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnFraccionarProducto = QtGui.QWidget()
    ui = Ui_vtnFraccionarProducto()
    ui.setupUi(vtnFraccionarProducto)
    vtnFraccionarProducto.show()
    sys.exit(app.exec_())

