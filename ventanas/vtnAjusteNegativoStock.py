# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAjusteNegativoStock.ui'
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

class Ui_vtnAjusteNegativoStock(object):
    def setupUi(self, vtnAjusteNegativoStock):
        vtnAjusteNegativoStock.setObjectName(_fromUtf8("vtnAjusteNegativoStock"))
        vtnAjusteNegativoStock.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAjusteNegativoStock)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbProducto = QtGui.QGroupBox(vtnAjusteNegativoStock)
        self.gbProducto.setObjectName(_fromUtf8("gbProducto"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbProducto)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.gbProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gbProducto)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gbProducto)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gbProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.gbProducto)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.gbProducto)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbProducto)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAjusteNegativoStock)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnAjusteNegativoStock)
        QtCore.QMetaObject.connectSlotsByName(vtnAjusteNegativoStock)

    def retranslateUi(self, vtnAjusteNegativoStock):
        vtnAjusteNegativoStock.setWindowTitle(_translate("vtnAjusteNegativoStock", "Ajuste Negativo Stock", None))
        self.gbProducto.setTitle(_translate("vtnAjusteNegativoStock", "Producto", None))
        self.label.setText(_translate("vtnAjusteNegativoStock", "Código de Barra", None))
        self.pushButton.setText(_translate("vtnAjusteNegativoStock", "Buscar", None))
        self.label_2.setText(_translate("vtnAjusteNegativoStock", "Cantidad", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnAjusteNegativoStock", "Código de Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnAjusteNegativoStock", "Medicamento", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnAjusteNegativoStock", "Presentacion", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("vtnAjusteNegativoStock", "Cantidad", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("vtnAjusteNegativoStock", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAjusteNegativoStock = QtGui.QWidget()
    ui = Ui_vtnAjusteNegativoStock()
    ui.setupUi(vtnAjusteNegativoStock)
    vtnAjusteNegativoStock.show()
    sys.exit(app.exec_())

