# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarProducto.ui'
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

class Ui_vtnModificarProducto(object):
    def setupUi(self, vtnModificarProducto):
        vtnModificarProducto.setObjectName(_fromUtf8("vtnModificarProducto"))
        vtnModificarProducto.resize(715, 653)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBuscarPres = QtGui.QPushButton(vtnModificarProducto)
        self.btnBuscarPres.setObjectName(_fromUtf8("btnBuscarPres"))
        self.gridLayout.addWidget(self.btnBuscarPres, 8, 3, 1, 1)
        self.btnBuscarMed = QtGui.QPushButton(vtnModificarProducto)
        self.btnBuscarMed.setObjectName(_fromUtf8("btnBuscarMed"))
        self.gridLayout.addWidget(self.btnBuscarMed, 5, 3, 1, 1)
        self.tablaProducto = QtGui.QTableWidget(vtnModificarProducto)
        self.tablaProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaProducto.setObjectName(_fromUtf8("tablaProducto"))
        self.tablaProducto.setColumnCount(0)
        self.tablaProducto.setRowCount(0)
        self.tablaProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tablaProducto.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaProducto, 2, 0, 1, 4)
        self.lineImp = QtGui.QLineEdit(vtnModificarProducto)
        self.lineImp.setObjectName(_fromUtf8("lineImp"))
        self.gridLayout.addWidget(self.lineImp, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.lineTipoPres = QtGui.QLineEdit(vtnModificarProducto)
        self.lineTipoPres.setObjectName(_fromUtf8("lineTipoPres"))
        self.gridLayout.addWidget(self.lineTipoPres, 8, 2, 1, 1)
        self.lineNombMed = QtGui.QLineEdit(vtnModificarProducto)
        self.lineNombMed.setObjectName(_fromUtf8("lineNombMed"))
        self.gridLayout.addWidget(self.lineNombMed, 5, 2, 1, 1)
        self.lineCodBarra = QtGui.QLineEdit(vtnModificarProducto)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout.addWidget(self.lineCodBarra, 1, 2, 1, 1)
        self.label_8 = QtGui.QLabel(vtnModificarProducto)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(vtnModificarProducto)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        self.label_7 = QtGui.QLabel(vtnModificarProducto)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 8, 1, 1, 1)
        self.label = QtGui.QLabel(vtnModificarProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnModificarProducto)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.btnBuscarProd = QtGui.QPushButton(vtnModificarProducto)
        self.btnBuscarProd.setObjectName(_fromUtf8("btnBuscarProd"))
        self.gridLayout.addWidget(self.btnBuscarProd, 1, 3, 1, 1)
        self.tablaMedicamento = QtGui.QTableWidget(vtnModificarProducto)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMedicamento, 6, 0, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 10, 2, 1, 2)
        self.tablaPresentacion = QtGui.QTableWidget(vtnModificarProducto)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaPresentacion, 9, 0, 1, 4)
        self.label_5 = QtGui.QLabel(vtnModificarProducto)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarProducto)
        vtnModificarProducto.setTabOrder(self.lineCodBarra, self.btnBuscarProd)
        vtnModificarProducto.setTabOrder(self.btnBuscarProd, self.tablaProducto)
        vtnModificarProducto.setTabOrder(self.tablaProducto, self.lineImp)
        vtnModificarProducto.setTabOrder(self.lineImp, self.lineNombMed)
        vtnModificarProducto.setTabOrder(self.lineNombMed, self.btnBuscarMed)
        vtnModificarProducto.setTabOrder(self.btnBuscarMed, self.tablaMedicamento)
        vtnModificarProducto.setTabOrder(self.tablaMedicamento, self.lineTipoPres)
        vtnModificarProducto.setTabOrder(self.lineTipoPres, self.btnBuscarPres)
        vtnModificarProducto.setTabOrder(self.btnBuscarPres, self.tablaPresentacion)
        vtnModificarProducto.setTabOrder(self.tablaPresentacion, self.buttonBox)

    def retranslateUi(self, vtnModificarProducto):
        vtnModificarProducto.setWindowTitle(_translate("vtnModificarProducto", "Modificar Producto", None))
        self.btnBuscarPres.setText(_translate("vtnModificarProducto", "Buscar", None))
        self.btnBuscarMed.setText(_translate("vtnModificarProducto", "Buscar", None))
        self.lineImp.setStatusTip(_translate("vtnModificarProducto", "Ingrese importe del producto (solo números separando los centavos por un punto (.) ejemplo 125.75)", None))
        self.lineImp.setAccessibleDescription(_translate("vtnModificarProducto", "importe", None))
        self.label_2.setText(_translate("vtnModificarProducto", "* Importe $", None))
        self.lineTipoPres.setStatusTip(_translate("vtnModificarProducto", "Ingrese tipo de la Presentación (solo letras)", None))
        self.lineTipoPres.setAccessibleDescription(_translate("vtnModificarProducto", "texto", None))
        self.lineNombMed.setStatusTip(_translate("vtnModificarProducto", "Ingrese nombre del Medicamento (solo letras y números)", None))
        self.lineNombMed.setAccessibleDescription(_translate("vtnModificarProducto", "textoNumeros", None))
        self.lineCodBarra.setStatusTip(_translate("vtnModificarProducto", "Ingrese código de barra del Producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnModificarProducto", "codigo", None))
        self.label_8.setText(_translate("vtnModificarProducto", "Producto", None))
        self.label_6.setText(_translate("vtnModificarProducto", "* Nombre", None))
        self.label_7.setText(_translate("vtnModificarProducto", "* Tipo", None))
        self.label.setText(_translate("vtnModificarProducto", "Código de Barra", None))
        self.label_4.setText(_translate("vtnModificarProducto", "Medicamento", None))
        self.btnBuscarProd.setText(_translate("vtnModificarProducto", "Buscar", None))
        self.label_5.setText(_translate("vtnModificarProducto", "Presentación", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarProducto = QtGui.QWidget()
    ui = Ui_vtnModificarProducto()
    ui.setupUi(vtnModificarProducto)
    vtnModificarProducto.show()
    sys.exit(app.exec_())

