# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaRemito.ui'
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

class Ui_vtnBajaRemito(object):
    def setupUi(self, vtnBajaRemito):
        vtnBajaRemito.setObjectName(_fromUtf8("vtnBajaRemito"))
        vtnBajaRemito.resize(559, 353)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaRemito)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(vtnBajaRemito)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnBajaRemito)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.lineEdit = QtGui.QLineEdit(vtnBajaRemito)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaRemito)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaRemito)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaRemito)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaRemito)
        vtnBajaRemito.setTabOrder(self.lineEdit, self.pushButton)
        vtnBajaRemito.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaRemito.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaRemito):
        vtnBajaRemito.setWindowTitle(_translate("vtnBajaRemito", "Baja Remito", None))
        self.label_2.setText(_translate("vtnBajaRemito", "Número", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaRemito", "Código Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaRemito", "Cantidad", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnBajaRemito", "Importe", None))
        self.pushButton.setText(_translate("vtnBajaRemito", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaRemito = QtGui.QWidget()
    ui = Ui_vtnBajaRemito()
    ui.setupUi(vtnBajaRemito)
    vtnBajaRemito.show()
    sys.exit(app.exec_())

