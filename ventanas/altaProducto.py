# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaProducto.ui'
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

class Ui_vtnAltaProducto(object):
    def setupUi(self, vtnAltaProducto):
        vtnAltaProducto.setObjectName(_fromUtf8("vtnAltaProducto"))
        vtnAltaProducto.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btnBuscarMed = QtGui.QPushButton(vtnAltaProducto)
        self.btnBuscarMed.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarMed.setObjectName(_fromUtf8("btnBuscarMed"))
        self.gridLayout.addWidget(self.btnBuscarMed, 1, 3, 1, 1)
        self.label_5 = QtGui.QLabel(vtnAltaProducto)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.btnBuscarPres = QtGui.QPushButton(vtnAltaProducto)
        self.btnBuscarPres.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarPres.setObjectName(_fromUtf8("btnBuscarPres"))
        self.gridLayout.addWidget(self.btnBuscarPres, 4, 3, 1, 1)
        self.label_7 = QtGui.QLabel(vtnAltaProducto)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.tablaPresentacion = QtGui.QTableWidget(vtnAltaProducto)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaPresentacion, 5, 1, 1, 3)
        self.lineImp = QtGui.QLineEdit(vtnAltaProducto)
        self.lineImp.setInputMask(_fromUtf8(""))
        self.lineImp.setObjectName(_fromUtf8("lineImp"))
        self.gridLayout.addWidget(self.lineImp, 8, 2, 1, 1)
        self.label_4 = QtGui.QLabel(vtnAltaProducto)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 9, 2, 1, 2)
        self.label_3 = QtGui.QLabel(vtnAltaProducto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        self.label = QtGui.QLabel(vtnAltaProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineNombMed = QtGui.QLineEdit(vtnAltaProducto)
        self.lineNombMed.setInputMask(_fromUtf8(""))
        self.lineNombMed.setObjectName(_fromUtf8("lineNombMed"))
        self.gridLayout.addWidget(self.lineNombMed, 1, 2, 1, 1)
        self.lineCodBarra = QtGui.QLineEdit(vtnAltaProducto)
        self.lineCodBarra.setObjectName(_fromUtf8("lineCodBarra"))
        self.gridLayout.addWidget(self.lineCodBarra, 7, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAltaProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.tablaMedicamento = QtGui.QTableWidget(vtnAltaProducto)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMedicamento, 2, 1, 1, 3)
        self.label_6 = QtGui.QLabel(vtnAltaProducto)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.lineTipoPres = QtGui.QLineEdit(vtnAltaProducto)
        self.lineTipoPres.setObjectName(_fromUtf8("lineTipoPres"))
        self.gridLayout.addWidget(self.lineTipoPres, 4, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaProducto)
        vtnAltaProducto.setTabOrder(self.lineNombMed, self.btnBuscarMed)
        vtnAltaProducto.setTabOrder(self.btnBuscarMed, self.tablaMedicamento)
        vtnAltaProducto.setTabOrder(self.tablaMedicamento, self.lineTipoPres)
        vtnAltaProducto.setTabOrder(self.lineTipoPres, self.btnBuscarPres)
        vtnAltaProducto.setTabOrder(self.btnBuscarPres, self.tablaPresentacion)
        vtnAltaProducto.setTabOrder(self.tablaPresentacion, self.lineCodBarra)
        vtnAltaProducto.setTabOrder(self.lineCodBarra, self.lineImp)
        vtnAltaProducto.setTabOrder(self.lineImp, self.buttonBox)

    def retranslateUi(self, vtnAltaProducto):
        vtnAltaProducto.setWindowTitle(_translate("vtnAltaProducto", "Alta Producto", None))
        self.btnBuscarMed.setText(_translate("vtnAltaProducto", "Buscar", None))
        self.label_5.setText(_translate("vtnAltaProducto", "Nombre", None))
        self.btnBuscarPres.setText(_translate("vtnAltaProducto", "Buscar", None))
        self.label_7.setText(_translate("vtnAltaProducto", "Producto", None))
        self.lineImp.setStatusTip(_translate("vtnAltaProducto", "Ingrese importe del producto (solo números separando los centavos por un punto (.) ejemplo 125.75)", None))
        self.lineImp.setAccessibleDescription(_translate("vtnAltaProducto", "importe", None))
        self.label_4.setText(_translate("vtnAltaProducto", "Importe $", None))
        self.label_3.setText(_translate("vtnAltaProducto", "Código de Barra", None))
        self.label.setText(_translate("vtnAltaProducto", "Medicamento", None))
        self.lineNombMed.setStatusTip(_translate("vtnAltaProducto", "Ingrese nombre del Medicamento (solo números y letras)", None))
        self.lineNombMed.setAccessibleDescription(_translate("vtnAltaProducto", "textoNumeros", None))
        self.lineCodBarra.setStatusTip(_translate("vtnAltaProducto", "Ingrese código de barra del producto (exactamente 9 números)", None))
        self.lineCodBarra.setAccessibleDescription(_translate("vtnAltaProducto", "codigo", None))
        self.label_2.setText(_translate("vtnAltaProducto", "Presentación", None))
        self.label_6.setText(_translate("vtnAltaProducto", "Tipo", None))
        self.lineTipoPres.setStatusTip(_translate("vtnAltaProducto", "Ingrese tipo de presentación(solo letras)", None))
        self.lineTipoPres.setAccessibleDescription(_translate("vtnAltaProducto", "texto", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaProducto = QtGui.QWidget()
    ui = Ui_vtnAltaProducto()
    ui.setupUi(vtnAltaProducto)
    vtnAltaProducto.show()
    sys.exit(app.exec_())

