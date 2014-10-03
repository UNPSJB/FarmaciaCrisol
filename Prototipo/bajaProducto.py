# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaProducto.ui'
#
# Created: Wed Oct  1 13:55:06 2014
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

class Ui_vtnBajaProducto(object):
    def setupUi(self, vtnBajaProducto):
        vtnBajaProducto.setObjectName(_fromUtf8("vtnBajaProducto"))
        vtnBajaProducto.resize(582, 257)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(vtnBajaProducto)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaProducto)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label = QtGui.QLabel(vtnBajaProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.tableWidget = QtGui.QTableWidget(vtnBajaProducto)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaProducto)
        vtnBajaProducto.setTabOrder(self.lineEdit, self.pushButton)
        vtnBajaProducto.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaProducto.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaProducto):
        vtnBajaProducto.setWindowTitle(_translate("vtnBajaProducto", "Baja Producto", None))
        self.pushButton.setText(_translate("vtnBajaProducto", "Buscar", None))
        self.label.setText(_translate("vtnBajaProducto", "Código de Barra", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaProducto", "Código de Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaProducto", "Medicamento", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnBajaProducto", "Presentación", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("vtnBajaProducto", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaProducto = QtGui.QWidget()
    ui = Ui_vtnBajaProducto()
    ui.setupUi(vtnBajaProducto)
    vtnBajaProducto.show()
    sys.exit(app.exec_())

