# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnDevolucionDeCliente.ui'
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

class Ui_vtnDevolucionDeCliente(object):
    def setupUi(self, vtnDevolucionDeCliente):
        vtnDevolucionDeCliente.setObjectName(_fromUtf8("vtnDevolucionDeCliente"))
        vtnDevolucionDeCliente.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnDevolucionDeCliente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbFactura = QtGui.QGroupBox(vtnDevolucionDeCliente)
        self.gbFactura.setObjectName(_fromUtf8("gbFactura"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbFactura)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.gbFactura)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gbFactura)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 2, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.gbFactura)
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
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.gbFactura)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gbFactura)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gbFactura)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gbFactura)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbFactura)
        self.gbNotaCredito = QtGui.QGroupBox(vtnDevolucionDeCliente)
        self.gbNotaCredito.setObjectName(_fromUtf8("gbNotaCredito"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbNotaCredito)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tableWidget_2 = QtGui.QTableWidget(self.gbNotaCredito)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tableWidget_2, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbNotaCredito)
        self.buttonBox = QtGui.QDialogButtonBox(vtnDevolucionDeCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnDevolucionDeCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnDevolucionDeCliente)

    def retranslateUi(self, vtnDevolucionDeCliente):
        vtnDevolucionDeCliente.setWindowTitle(_translate("vtnDevolucionDeCliente", "Devolución de Cliente", None))
        self.gbFactura.setTitle(_translate("vtnDevolucionDeCliente", "Factura", None))
        self.pushButton.setText(_translate("vtnDevolucionDeCliente", "Buscar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnDevolucionDeCliente", "Código Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnDevolucionDeCliente", "Importe", None))
        self.label_2.setText(_translate("vtnDevolucionDeCliente", "Número", None))
        self.label_3.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        self.pushButton_2.setText(_translate("vtnDevolucionDeCliente", "Agergar", None))
        self.gbNotaCredito.setTitle(_translate("vtnDevolucionDeCliente", "Nota de Crédito", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnDevolucionDeCliente", "Código Barra", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnDevolucionDeCliente", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnDevolucionDeCliente = QtGui.QWidget()
    ui = Ui_vtnDevolucionDeCliente()
    ui.setupUi(vtnDevolucionDeCliente)
    vtnDevolucionDeCliente.show()
    sys.exit(app.exec_())

