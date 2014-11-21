# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAltaLote.ui'
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

class Ui_vtnAltaLote(object):
    def setupUi(self, vtnAltaLote):
        vtnAltaLote.setObjectName(_fromUtf8("vtnAltaLote"))
        vtnAltaLote.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaLote)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(vtnAltaLote)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineNumero = QtGui.QLineEdit(self.groupBox)
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.gridLayout.addWidget(self.lineNumero, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineCant = QtGui.QLineEdit(self.groupBox)
        self.lineCant.setObjectName(_fromUtf8("lineCant"))
        self.gridLayout.addWidget(self.lineCant, 2, 1, 1, 1)
        self.dateFechVenc = QtGui.QDateEdit(self.groupBox)
        self.dateFechVenc.setObjectName(_fromUtf8("dateFechVenc"))
        self.gridLayout.addWidget(self.dateFechVenc, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(vtnAltaLote)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tablaProducto = QtGui.QTableWidget(self.groupBox_2)
        self.tablaProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaProducto.setObjectName(_fromUtf8("tablaProducto"))
        self.tablaProducto.setColumnCount(0)
        self.tablaProducto.setRowCount(0)
        self.tablaProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tablaProducto.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tablaProducto, 0, 0, 1, 1)
        self.btnActualizarProductos = QtGui.QPushButton(self.groupBox_2)
        self.btnActualizarProductos.setObjectName(_fromUtf8("btnActualizarProductos"))
        self.gridLayout_2.addWidget(self.btnActualizarProductos, 1, 0, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaLote)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnAltaLote)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaLote)
        vtnAltaLote.setTabOrder(self.lineNumero, self.dateFechVenc)
        vtnAltaLote.setTabOrder(self.dateFechVenc, self.lineCant)
        vtnAltaLote.setTabOrder(self.lineCant, self.tablaProducto)

    def retranslateUi(self, vtnAltaLote):
        vtnAltaLote.setWindowTitle(_translate("vtnAltaLote", "Alta Lote", None))
        self.groupBox.setTitle(_translate("vtnAltaLote", "Lote", None))
        self.label.setText(_translate("vtnAltaLote", "Número", None))
        self.lineNumero.setStatusTip(_translate("vtnAltaLote", "Ingrese el número de Lote del Producto (solo letras y números sin espacios)", None))
        self.lineNumero.setAccessibleDescription(_translate("vtnAltaLote", "lote", None))
        self.label_2.setText(_translate("vtnAltaLote", "Fecha de Vencimiento", None))
        self.label_3.setText(_translate("vtnAltaLote", "Cantidad", None))
        self.lineCant.setStatusTip(_translate("vtnAltaLote", "Ingrese la cantidad del producto para dicho lote", None))
        self.lineCant.setAccessibleDescription(_translate("vtnAltaLote", "cantidad", None))
        self.dateFechVenc.setStatusTip(_translate("vtnAltaLote", "Ingrese la fecha de vencimiento del lote", None))
        self.groupBox_2.setTitle(_translate("vtnAltaLote", "Producto", None))
        self.btnActualizarProductos.setText(_translate("vtnAltaLote", "Actualizar Productos", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaLote = QtGui.QWidget()
    ui = Ui_vtnAltaLote()
    ui.setupUi(vtnAltaLote)
    vtnAltaLote.show()
    sys.exit(app.exec_())

