# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajusteNegativoStock.ui'
#
# Created: Wed Sep 24 13:59:38 2014
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
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(vtnAjusteNegativoStock)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.label = QtGui.QLabel(vtnAjusteNegativoStock)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnAjusteNegativoStock)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAjusteNegativoStock)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnAjusteNegativoStock)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAjusteNegativoStock)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 2)
        self.label_3 = QtGui.QLabel(vtnAjusteNegativoStock)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnAjusteNegativoStock)
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
        self.gridLayout.addWidget(self.tableWidget, 2, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAjusteNegativoStock)
        QtCore.QMetaObject.connectSlotsByName(vtnAjusteNegativoStock)
        vtnAjusteNegativoStock.setTabOrder(self.lineEdit, self.pushButton)
        vtnAjusteNegativoStock.setTabOrder(self.pushButton, self.tableWidget)
        vtnAjusteNegativoStock.setTabOrder(self.tableWidget, self.lineEdit_2)
        vtnAjusteNegativoStock.setTabOrder(self.lineEdit_2, self.buttonBox)

    def retranslateUi(self, vtnAjusteNegativoStock):
        vtnAjusteNegativoStock.setWindowTitle(_translate("vtnAjusteNegativoStock", "Ajuste Negativo Stock", None))
        self.label.setText(_translate("vtnAjusteNegativoStock", "Código de Barra", None))
        self.label_2.setText(_translate("vtnAjusteNegativoStock", "Cantidad", None))
        self.pushButton.setText(_translate("vtnAjusteNegativoStock", "Buscar", None))
        self.label_3.setText(_translate("vtnAjusteNegativoStock", "Producto", None))
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

