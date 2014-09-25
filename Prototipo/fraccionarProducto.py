# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fraccionarProducto.ui'
#
# Created: Wed Sep 24 13:59:39 2014
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

class Ui_vtnFraccionarProducto(object):
    def setupUi(self, vtnFraccionarProducto):
        vtnFraccionarProducto.setObjectName(_fromUtf8("vtnFraccionarProducto"))
        vtnFraccionarProducto.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnFraccionarProducto)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnFraccionarProducto)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(vtnFraccionarProducto)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(vtnFraccionarProducto)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnFraccionarProducto)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnFraccionarProducto)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnFraccionarProducto)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 2, 1, 2)
        self.tableWidget_2 = QtGui.QTableWidget(vtnFraccionarProducto)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_2, 4, 1, 1, 3)
        self.tableWidget = QtGui.QTableWidget(vtnFraccionarProducto)
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
        self.gridLayout.addWidget(self.tableWidget, 2, 1, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnFraccionarProducto)
        QtCore.QMetaObject.connectSlotsByName(vtnFraccionarProducto)
        vtnFraccionarProducto.setTabOrder(self.lineEdit, self.pushButton)
        vtnFraccionarProducto.setTabOrder(self.pushButton, self.tableWidget)
        vtnFraccionarProducto.setTabOrder(self.tableWidget, self.tableWidget_2)
        vtnFraccionarProducto.setTabOrder(self.tableWidget_2, self.buttonBox)

    def retranslateUi(self, vtnFraccionarProducto):
        vtnFraccionarProducto.setWindowTitle(_translate("vtnFraccionarProducto", "Fraccionar Producto", None))
        self.label.setText(_translate("vtnFraccionarProducto", "Producto", None))
        self.label_2.setText(_translate("vtnFraccionarProducto", "Código de Barra", None))
        self.label_3.setText(_translate("vtnFraccionarProducto", "Fraccionable", None))
        self.pushButton.setText(_translate("vtnFraccionarProducto", "Buscar", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnFraccionarProducto", "Código de Barra", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnFraccionarProducto", "Medicamento", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnFraccionarProducto", "Presentación", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("vtnFraccionarProducto", "Importe", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnFraccionarProducto", "Código de Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnFraccionarProducto", "Medicamento", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnFraccionarProducto", "Presentación", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("vtnFraccionarProducto", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnFraccionarProducto = QtGui.QWidget()
    ui = Ui_vtnFraccionarProducto()
    ui.setupUi(vtnFraccionarProducto)
    vtnFraccionarProducto.show()
    sys.exit(app.exec_())

