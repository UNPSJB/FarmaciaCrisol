# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnModificarProducto.ui'
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

class Ui_vtnModificarProducto(object):
    def setupUi(self, vtnModificarProducto):
        vtnModificarProducto.setObjectName(_fromUtf8("vtnModificarProducto"))
        vtnModificarProducto.resize(715, 653)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gpProducto = QtGui.QGroupBox(vtnModificarProducto)
        self.gpProducto.setObjectName(_fromUtf8("gpProducto"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gpProducto)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tablaProducto = QtGui.QTableWidget(self.gpProducto)
        self.tablaProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaProducto.setObjectName(_fromUtf8("tablaProducto"))
        self.tablaProducto.setColumnCount(0)
        self.tablaProducto.setRowCount(0)
        self.tablaProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tablaProducto.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tablaProducto, 1, 0, 1, 3)
        self.label = QtGui.QLabel(self.gpProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineCodBarra = QtGui.QLineEdit(self.gpProducto)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout_2.addWidget(self.lineCodBarra, 0, 1, 1, 1)
        self.btnBuscarProd = QtGui.QPushButton(self.gpProducto)
        self.btnBuscarProd.setObjectName(_fromUtf8("btnBuscarProd"))
        self.gridLayout_2.addWidget(self.btnBuscarProd, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gpProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineImp = QtGui.QLineEdit(self.gpProducto)
        self.lineImp.setObjectName(_fromUtf8("lineImp"))
        self.gridLayout_2.addWidget(self.lineImp, 2, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gpProducto)
        self.gbMedicamento = QtGui.QGroupBox(vtnModificarProducto)
        self.gbMedicamento.setObjectName(_fromUtf8("gbMedicamento"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbMedicamento)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btnBuscarMed = QtGui.QPushButton(self.gbMedicamento)
        self.btnBuscarMed.setObjectName(_fromUtf8("btnBuscarMed"))
        self.gridLayout_3.addWidget(self.btnBuscarMed, 0, 2, 1, 1)
        self.lineNombMed = QtGui.QLineEdit(self.gbMedicamento)
        self.lineNombMed.setObjectName(_fromUtf8("lineNombMed"))
        self.gridLayout_3.addWidget(self.lineNombMed, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.gbMedicamento)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.tablaMedicamento = QtGui.QTableWidget(self.gbMedicamento)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tablaMedicamento, 1, 0, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbMedicamento)
        self.gbPresentacion = QtGui.QGroupBox(vtnModificarProducto)
        self.gbPresentacion.setObjectName(_fromUtf8("gbPresentacion"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gbPresentacion)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.lineTipoPres = QtGui.QLineEdit(self.gbPresentacion)
        self.lineTipoPres.setObjectName(_fromUtf8("lineTipoPres"))
        self.gridLayout_4.addWidget(self.lineTipoPres, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.gbPresentacion)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)
        self.btnBuscarPres = QtGui.QPushButton(self.gbPresentacion)
        self.btnBuscarPres.setObjectName(_fromUtf8("btnBuscarPres"))
        self.gridLayout_4.addWidget(self.btnBuscarPres, 0, 2, 1, 1)
        self.tablaPresentacion = QtGui.QTableWidget(self.gbPresentacion)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.tablaPresentacion, 1, 0, 1, 3)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.gbPresentacion)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnModificarProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarProducto)

    def retranslateUi(self, vtnModificarProducto):
        vtnModificarProducto.setWindowTitle(_translate("vtnModificarProducto", "Modificar Producto", None))
        self.gpProducto.setTitle(_translate("vtnModificarProducto", "Producto", None))
        self.label.setText(_translate("vtnModificarProducto", "Código de Barra", None))
        self.lineCodBarra.setStatusTip(_translate("vtnModificarProducto", "Ingrese código de barra del Producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnModificarProducto", "codigo", None))
        self.btnBuscarProd.setText(_translate("vtnModificarProducto", "Buscar", None))
        self.label_2.setText(_translate("vtnModificarProducto", "* Importe $", None))
        self.lineImp.setStatusTip(_translate("vtnModificarProducto", "Ingrese importe del producto (solo números separando los centavos por un punto (.) ejemplo 125.75)", None))
        self.lineImp.setAccessibleDescription(_translate("vtnModificarProducto", "importe", None))
        self.gbMedicamento.setTitle(_translate("vtnModificarProducto", "Medicamento", None))
        self.btnBuscarMed.setText(_translate("vtnModificarProducto", "Buscar", None))
        self.lineNombMed.setStatusTip(_translate("vtnModificarProducto", "Ingrese nombre del Medicamento (solo letras y números)", None))
        self.lineNombMed.setAccessibleDescription(_translate("vtnModificarProducto", "textoNumeros", None))
        self.label_6.setText(_translate("vtnModificarProducto", "* Nombre", None))
        self.gbPresentacion.setTitle(_translate("vtnModificarProducto", "Presentación", None))
        self.lineTipoPres.setStatusTip(_translate("vtnModificarProducto", "Ingrese tipo de la Presentación (solo letras)", None))
        self.lineTipoPres.setAccessibleDescription(_translate("vtnModificarProducto", "texto", None))
        self.label_7.setText(_translate("vtnModificarProducto", "* Tipo", None))
        self.btnBuscarPres.setText(_translate("vtnModificarProducto", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarProducto = QtGui.QWidget()
    ui = Ui_vtnModificarProducto()
    ui.setupUi(vtnModificarProducto)
    vtnModificarProducto.show()
    sys.exit(app.exec_())

