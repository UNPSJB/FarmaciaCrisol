# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnReintegroCliente.ui'
#
# Created: Tue Oct 28 16:56:01 2014
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

class Ui_vtnReintegroCliente(object):
    def setupUi(self, vtnReintegroCliente):
        vtnReintegroCliente.setObjectName(_fromUtf8("vtnReintegroCliente"))
        vtnReintegroCliente.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(vtnReintegroCliente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbObraSocial = QtGui.QGroupBox(vtnReintegroCliente)
        self.gbObraSocial.setObjectName(_fromUtf8("gbObraSocial"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbObraSocial)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.lineEdit = QtGui.QLineEdit(self.gbObraSocial)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gbObraSocial)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gbObraSocial)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gbObraSocial)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gbObraSocial)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.gbObraSocial)
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
        self.gridLayout_2.addWidget(self.tableWidget, 2, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbObraSocial)
        self.gbFactura = QtGui.QGroupBox(vtnReintegroCliente)
        self.gbFactura.setObjectName(_fromUtf8("gbFactura"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbFactura)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.gbFactura)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gbFactura)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.gbFactura)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(self.gbFactura)
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
        self.gridLayout_3.addWidget(self.tableWidget_2, 1, 0, 1, 3)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbFactura)
        self.gbNotaCredito = QtGui.QGroupBox(vtnReintegroCliente)
        self.gbNotaCredito.setObjectName(_fromUtf8("gbNotaCredito"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.gbNotaCredito)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tableWidget_3 = QtGui.QTableWidget(self.gbNotaCredito)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.tableWidget_3, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_4)
        self.verticalLayout.addWidget(self.gbNotaCredito)
        self.buttonBox = QtGui.QDialogButtonBox(vtnReintegroCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnReintegroCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnReintegroCliente)

    def retranslateUi(self, vtnReintegroCliente):
        vtnReintegroCliente.setWindowTitle(_translate("vtnReintegroCliente", "Reintegro Cliente", None))
        self.gbObraSocial.setTitle(_translate("vtnReintegroCliente", "Obra Social", None))
        self.pushButton.setText(_translate("vtnReintegroCliente", "Buscar", None))
        self.label_2.setText(_translate("vtnReintegroCliente", "CUIT", None))
        self.label_3.setText(_translate("vtnReintegroCliente", "Razón Social", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Razón Social", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "CUIT", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Dirección", None))
        self.gbFactura.setTitle(_translate("vtnReintegroCliente", "Factura", None))
        self.pushButton_2.setText(_translate("vtnReintegroCliente", "Buscar", None))
        self.label_4.setText(_translate("vtnReintegroCliente", "Número", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Código Barra", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "Cantidad", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Importe", None))
        self.gbNotaCredito.setTitle(_translate("vtnReintegroCliente", "Nota de Crédito", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Código Barra", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "Cantidad", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnReintegroCliente = QtGui.QWidget()
    ui = Ui_vtnReintegroCliente()
    ui.setupUi(vtnReintegroCliente)
    vtnReintegroCliente.show()
    sys.exit(app.exec_())

