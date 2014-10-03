# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaProducto.ui'
#
# Created: Fri Oct  3 15:23:12 2014
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
        self.btnBuscarTipo = QtGui.QPushButton(vtnAltaProducto)
        self.btnBuscarTipo.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarTipo.setObjectName(_fromUtf8("btnBuscarTipo"))
        self.gridLayout.addWidget(self.btnBuscarTipo, 4, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 9, 2, 1, 2)
        self.label = QtGui.QLabel(vtnAltaProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(vtnAltaProducto)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_2, 5, 1, 1, 3)
        self.btnBuscarNomb = QtGui.QPushButton(vtnAltaProducto)
        self.btnBuscarNomb.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarNomb.setObjectName(_fromUtf8("btnBuscarNomb"))
        self.gridLayout.addWidget(self.btnBuscarNomb, 1, 3, 1, 1)
        self.txtNomb = QtGui.QLineEdit(vtnAltaProducto)
        self.txtNomb.setInputMask(_fromUtf8(""))
        self.txtNomb.setObjectName(_fromUtf8("txtNomb"))
        self.gridLayout.addWidget(self.txtNomb, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAltaProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnAltaProducto)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 2, 1, 1, 3)
        self.label_5 = QtGui.QLabel(vtnAltaProducto)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_7 = QtGui.QLabel(vtnAltaProducto)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.txtTipo = QtGui.QLineEdit(vtnAltaProducto)
        self.txtTipo.setObjectName(_fromUtf8("txtTipo"))
        self.gridLayout.addWidget(self.txtTipo, 4, 2, 1, 1)
        self.label_6 = QtGui.QLabel(vtnAltaProducto)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.txtCodBarra = QtGui.QLineEdit(vtnAltaProducto)
        self.txtCodBarra.setObjectName(_fromUtf8("txtCodBarra"))
        self.gridLayout.addWidget(self.txtCodBarra, 7, 2, 1, 1)
        self.txtImp = QtGui.QLineEdit(vtnAltaProducto)
        self.txtImp.setInputMask(_fromUtf8(""))
        self.txtImp.setObjectName(_fromUtf8("txtImp"))
        self.gridLayout.addWidget(self.txtImp, 8, 2, 1, 1)
        self.label_3 = QtGui.QLabel(vtnAltaProducto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnAltaProducto)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 8, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaProducto)
        vtnAltaProducto.setTabOrder(self.txtNomb, self.btnBuscarNomb)
        vtnAltaProducto.setTabOrder(self.btnBuscarNomb, self.tableWidget)
        vtnAltaProducto.setTabOrder(self.tableWidget, self.txtTipo)
        vtnAltaProducto.setTabOrder(self.txtTipo, self.btnBuscarTipo)
        vtnAltaProducto.setTabOrder(self.btnBuscarTipo, self.tableWidget_2)
        vtnAltaProducto.setTabOrder(self.tableWidget_2, self.txtCodBarra)
        vtnAltaProducto.setTabOrder(self.txtCodBarra, self.txtImp)
        vtnAltaProducto.setTabOrder(self.txtImp, self.buttonBox)

    def retranslateUi(self, vtnAltaProducto):
        vtnAltaProducto.setWindowTitle(_translate("vtnAltaProducto", "Alta Producto", None))
        self.btnBuscarTipo.setText(_translate("vtnAltaProducto", "Buscar", None))
        self.label.setText(_translate("vtnAltaProducto", "Medicamento", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnAltaProducto", "Tipo", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnAltaProducto", "Unidad Medida", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnAltaProducto", "Cantidad Fracciones", None))
        self.btnBuscarNomb.setText(_translate("vtnAltaProducto", "Buscar", None))
        self.txtNomb.setAccessibleDescription(_translate("vtnAltaProducto", "texto", None))
        self.label_2.setText(_translate("vtnAltaProducto", "Presentación", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnAltaProducto", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnAltaProducto", "Monodroga", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnAltaProducto", "Cantidad de Monodroga", None))
        self.label_5.setText(_translate("vtnAltaProducto", "Nombre", None))
        self.label_7.setText(_translate("vtnAltaProducto", "Producto", None))
        self.txtTipo.setAccessibleDescription(_translate("vtnAltaProducto", "texto", None))
        self.label_6.setText(_translate("vtnAltaProducto", "Tipo", None))
        self.txtCodBarra.setAccessibleDescription(_translate("vtnAltaProducto", "codigo", None))
        self.txtImp.setAccessibleDescription(_translate("vtnAltaProducto", "importe", None))
        self.label_3.setText(_translate("vtnAltaProducto", "Código de Barra", None))
        self.label_4.setText(_translate("vtnAltaProducto", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaProducto = QtGui.QWidget()
    ui = Ui_vtnAltaProducto()
    ui.setupUi(vtnAltaProducto)
    vtnAltaProducto.show()
    sys.exit(app.exec_())

