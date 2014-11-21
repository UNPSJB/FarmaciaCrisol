# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnModificarLote.ui'
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

class Ui_vtnModificarLote(object):
    def setupUi(self, vtnModificarLote):
        vtnModificarLote.setObjectName(_fromUtf8("vtnModificarLote"))
        vtnModificarLote.resize(638, 421)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarLote)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(vtnModificarLote)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.dateFechVenc = QtGui.QDateEdit(self.groupBox)
        self.dateFechVenc.setObjectName(_fromUtf8("dateFechVenc"))
        self.gridLayout_2.addWidget(self.dateFechVenc, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.tablaLote = QtGui.QTableWidget(self.groupBox)
        self.tablaLote.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaLote.setObjectName(_fromUtf8("tablaLote"))
        self.tablaLote.setColumnCount(0)
        self.tablaLote.setRowCount(0)
        self.tablaLote.horizontalHeader().setDefaultSectionSize(160)
        self.tablaLote.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tablaLote, 1, 0, 1, 3)
        self.btnBuscarLote = QtGui.QPushButton(self.groupBox)
        self.btnBuscarLote.setObjectName(_fromUtf8("btnBuscarLote"))
        self.gridLayout_2.addWidget(self.btnBuscarLote, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineNumero = QtGui.QLineEdit(self.groupBox)
        self.lineNumero.setObjectName(_fromUtf8("lineNumero"))
        self.gridLayout_2.addWidget(self.lineNumero, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineCant = QtGui.QLineEdit(self.groupBox)
        self.lineCant.setObjectName(_fromUtf8("lineCant"))
        self.gridLayout_2.addWidget(self.lineCant, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(vtnModificarLote)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBuscarProd = QtGui.QPushButton(self.groupBox_2)
        self.btnBuscarProd.setObjectName(_fromUtf8("btnBuscarProd"))
        self.gridLayout.addWidget(self.btnBuscarProd, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineCodBarra = QtGui.QLineEdit(self.groupBox_2)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout.addWidget(self.lineCodBarra, 0, 1, 1, 1)
        self.tablaProducto = QtGui.QTableWidget(self.groupBox_2)
        self.tablaProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaProducto.setObjectName(_fromUtf8("tablaProducto"))
        self.tablaProducto.setColumnCount(0)
        self.tablaProducto.setRowCount(0)
        self.tablaProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tablaProducto.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaProducto, 1, 0, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarLote)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnModificarLote)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarLote)
        vtnModificarLote.setTabOrder(self.lineNumero, self.btnBuscarLote)
        vtnModificarLote.setTabOrder(self.btnBuscarLote, self.tablaLote)
        vtnModificarLote.setTabOrder(self.tablaLote, self.dateFechVenc)
        vtnModificarLote.setTabOrder(self.dateFechVenc, self.lineCant)
        vtnModificarLote.setTabOrder(self.lineCant, self.lineCodBarra)
        vtnModificarLote.setTabOrder(self.lineCodBarra, self.btnBuscarProd)
        vtnModificarLote.setTabOrder(self.btnBuscarProd, self.tablaProducto)
        vtnModificarLote.setTabOrder(self.tablaProducto, self.buttonBox)

    def retranslateUi(self, vtnModificarLote):
        vtnModificarLote.setWindowTitle(_translate("vtnModificarLote", "Modificar Lote", None))
        self.groupBox.setTitle(_translate("vtnModificarLote", "Lote", None))
        self.label.setText(_translate("vtnModificarLote", "Número", None))
        self.btnBuscarLote.setText(_translate("vtnModificarLote", "Buscar", None))
        self.label_2.setText(_translate("vtnModificarLote", "* Fecha de Vencimiento", None))
        self.lineNumero.setStatusTip(_translate("vtnModificarLote", "Ingrese número de lote (solo letras y números sin espacios)", None))
        self.lineNumero.setAccessibleDescription(_translate("vtnModificarLote", "lote", None))
        self.label_3.setText(_translate("vtnModificarLote", "* Cantidad", None))
        self.lineCant.setStatusTip(_translate("vtnModificarLote", "Ingrese cantidad del producto para dicho lote", None))
        self.lineCant.setAccessibleDescription(_translate("vtnModificarLote", "cantidad", None))
        self.groupBox_2.setTitle(_translate("vtnModificarLote", "Producto", None))
        self.btnBuscarProd.setText(_translate("vtnModificarLote", "Buscar", None))
        self.label_4.setText(_translate("vtnModificarLote", "* Código de Barra", None))
        self.lineCodBarra.setStatusTip(_translate("vtnModificarLote", "Ingrese código de barra del producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnModificarLote", "codigo", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarLote = QtGui.QWidget()
    ui = Ui_vtnModificarLote()
    ui.setupUi(vtnModificarLote)
    vtnModificarLote.show()
    sys.exit(app.exec_())

