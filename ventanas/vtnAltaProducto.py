# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAltaProducto.ui'
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

class Ui_vtnAltaProducto(object):
    def setupUi(self, vtnAltaProducto):
        vtnAltaProducto.setObjectName(_fromUtf8("vtnAltaProducto"))
        vtnAltaProducto.resize(757, 546)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbMedicamento = QtGui.QGroupBox(vtnAltaProducto)
        self.gbMedicamento.setObjectName(_fromUtf8("gbMedicamento"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbMedicamento)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.btnBuscarMed = QtGui.QPushButton(self.gbMedicamento)
        self.btnBuscarMed.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarMed.setObjectName(_fromUtf8("btnBuscarMed"))
        self.gridLayout_2.addWidget(self.btnBuscarMed, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(self.gbMedicamento)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineNombMed = QtGui.QLineEdit(self.gbMedicamento)
        self.lineNombMed.setInputMask(_fromUtf8(""))
        self.lineNombMed.setObjectName(_fromUtf8("lineNombMed"))
        self.gridLayout_2.addWidget(self.lineNombMed, 0, 1, 1, 1)
        self.tablaMedicamento = QtGui.QTableWidget(self.gbMedicamento)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tablaMedicamento, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbMedicamento)
        self.gbPresentacion = QtGui.QGroupBox(vtnAltaProducto)
        self.gbPresentacion.setObjectName(_fromUtf8("gbPresentacion"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbPresentacion)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_6 = QtGui.QLabel(self.gbPresentacion)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.btnBuscarPres = QtGui.QPushButton(self.gbPresentacion)
        self.btnBuscarPres.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarPres.setObjectName(_fromUtf8("btnBuscarPres"))
        self.gridLayout_4.addWidget(self.btnBuscarPres, 0, 2, 1, 1)
        self.lineTipoPres = QtGui.QLineEdit(self.gbPresentacion)
        self.lineTipoPres.setObjectName(_fromUtf8("lineTipoPres"))
        self.gridLayout_4.addWidget(self.lineTipoPres, 0, 1, 1, 1)
        self.tablaPresentacion = QtGui.QTableWidget(self.gbPresentacion)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.tablaPresentacion, 1, 0, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.gbPresentacion)
        self.gpProducto = QtGui.QGroupBox(vtnAltaProducto)
        self.gpProducto.setObjectName(_fromUtf8("gpProducto"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gpProducto)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.lineCodBarra = QtGui.QLineEdit(self.gpProducto)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout_5.addWidget(self.lineCodBarra, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gpProducto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gpProducto)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineImp = QtGui.QLineEdit(self.gpProducto)
        self.lineImp.setInputMask(_fromUtf8(""))
        self.lineImp.setObjectName(_fromUtf8("lineImp"))
        self.gridLayout_5.addWidget(self.lineImp, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_5)
        self.verticalLayout.addWidget(self.gpProducto)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnAltaProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaProducto)

    def retranslateUi(self, vtnAltaProducto):
        vtnAltaProducto.setWindowTitle(_translate("vtnAltaProducto", "Alta Producto", None))
        self.gbMedicamento.setTitle(_translate("vtnAltaProducto", "Medicamento", None))
        self.btnBuscarMed.setText(_translate("vtnAltaProducto", "Buscar", None))
        self.label_5.setText(_translate("vtnAltaProducto", "Nombre", None))
        self.lineNombMed.setStatusTip(_translate("vtnAltaProducto", "Ingrese nombre del Medicamento (solo números y letras)", None))
        self.lineNombMed.setAccessibleDescription(_translate("vtnAltaProducto", "textoNumeros", None))
        self.gbPresentacion.setTitle(_translate("vtnAltaProducto", "Presentación", None))
        self.label_6.setText(_translate("vtnAltaProducto", "Tipo", None))
        self.btnBuscarPres.setText(_translate("vtnAltaProducto", "Buscar", None))
        self.lineTipoPres.setStatusTip(_translate("vtnAltaProducto", "Ingrese tipo de presentación(solo letras)", None))
        self.lineTipoPres.setAccessibleDescription(_translate("vtnAltaProducto", "texto", None))
        self.gpProducto.setTitle(_translate("vtnAltaProducto", "Producto", None))
        self.lineCodBarra.setStatusTip(_translate("vtnAltaProducto", "Ingrese código de barra del producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnAltaProducto", "codigo", None))
        self.label_3.setText(_translate("vtnAltaProducto", "Código de Barra", None))
        self.label_4.setText(_translate("vtnAltaProducto", "Importe $", None))
        self.lineImp.setStatusTip(_translate("vtnAltaProducto", "Ingrese importe del producto (solo números separando los centavos por un punto (.) ejemplo 125.75)", None))
        self.lineImp.setAccessibleDescription(_translate("vtnAltaProducto", "importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaProducto = QtGui.QWidget()
    ui = Ui_vtnAltaProducto()
    ui.setupUi(vtnAltaProducto)
    vtnAltaProducto.show()
    sys.exit(app.exec_())

