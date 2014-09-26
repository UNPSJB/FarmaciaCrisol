# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reintegroCliente.ui'
#
# Created: Fri Sep 26 11:13:15 2014
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
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(vtnReintegroCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnReintegroCliente)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(vtnReintegroCliente)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 5, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnReintegroCliente)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)
        self.label_6 = QtGui.QLabel(vtnReintegroCliente)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label = QtGui.QLabel(vtnReintegroCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(vtnReintegroCliente)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnReintegroCliente)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 2)
        self.label_5 = QtGui.QLabel(vtnReintegroCliente)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(vtnReintegroCliente)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 5, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnReintegroCliente)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 2, 4, 1, 1)
        self.tableWidget_3 = QtGui.QTableWidget(vtnReintegroCliente)
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
        self.gridLayout.addWidget(self.tableWidget_3, 8, 1, 1, 4)
        self.tableWidget = QtGui.QTableWidget(vtnReintegroCliente)
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
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 1, 4)
        self.tableWidget_2 = QtGui.QTableWidget(vtnReintegroCliente)
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
        self.gridLayout.addWidget(self.tableWidget_2, 6, 1, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(vtnReintegroCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 9, 3, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnReintegroCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnReintegroCliente)
        vtnReintegroCliente.setTabOrder(self.lineEdit, self.lineEdit_2)
        vtnReintegroCliente.setTabOrder(self.lineEdit_2, self.pushButton)
        vtnReintegroCliente.setTabOrder(self.pushButton, self.tableWidget)
        vtnReintegroCliente.setTabOrder(self.tableWidget, self.lineEdit_3)
        vtnReintegroCliente.setTabOrder(self.lineEdit_3, self.pushButton_2)
        vtnReintegroCliente.setTabOrder(self.pushButton_2, self.tableWidget_2)
        vtnReintegroCliente.setTabOrder(self.tableWidget_2, self.tableWidget_3)
        vtnReintegroCliente.setTabOrder(self.tableWidget_3, self.buttonBox)

    def retranslateUi(self, vtnReintegroCliente):
        vtnReintegroCliente.setWindowTitle(_translate("vtnReintegroCliente", "Reintegro Cliente", None))
        self.label_2.setText(_translate("vtnReintegroCliente", "CUIT", None))
        self.label_4.setText(_translate("vtnReintegroCliente", "Número", None))
        self.label_6.setText(_translate("vtnReintegroCliente", "Nota de Crédito", None))
        self.label.setText(_translate("vtnReintegroCliente", "Obra Social", None))
        self.label_3.setText(_translate("vtnReintegroCliente", "Razón Social", None))
        self.label_5.setText(_translate("vtnReintegroCliente", "Factura", None))
        self.pushButton_2.setText(_translate("vtnReintegroCliente", "Buscar", None))
        self.pushButton.setText(_translate("vtnReintegroCliente", "Buscar", None))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Código Barra", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "Cantidad", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Importe", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Razón Social", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "CUIT", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Dirección", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnReintegroCliente", "Código Barra", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnReintegroCliente", "Cantidad", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnReintegroCliente", "Importe", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnReintegroCliente = QtGui.QWidget()
    ui = Ui_vtnReintegroCliente()
    ui.setupUi(vtnReintegroCliente)
    vtnReintegroCliente.show()
    sys.exit(app.exec_())

