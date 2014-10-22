# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devolucionDeCliente.ui'
#
# Created: Thu Oct 16 15:32:19 2014
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
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(vtnDevolucionDeCliente)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 3, 1, 1)
        self.label = QtGui.QLabel(vtnDevolucionDeCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(vtnDevolucionDeCliente)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(vtnDevolucionDeCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnDevolucionDeCliente)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnDevolucionDeCliente)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnDevolucionDeCliente)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 3, 2, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnDevolucionDeCliente)
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
        self.gridLayout.addWidget(self.tableWidget, 2, 1, 1, 4)
        self.tableWidget_2 = QtGui.QTableWidget(vtnDevolucionDeCliente)
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
        self.gridLayout.addWidget(self.tableWidget_2, 5, 1, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(vtnDevolucionDeCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 6, 3, 1, 2)
        self.pushButton_2 = QtGui.QPushButton(vtnDevolucionDeCliente)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 3, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnDevolucionDeCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnDevolucionDeCliente)
        vtnDevolucionDeCliente.setTabOrder(self.lineEdit, self.tableWidget)
        vtnDevolucionDeCliente.setTabOrder(self.tableWidget, self.lineEdit_2)
        vtnDevolucionDeCliente.setTabOrder(self.lineEdit_2, self.pushButton_2)
        vtnDevolucionDeCliente.setTabOrder(self.pushButton_2, self.tableWidget_2)
        vtnDevolucionDeCliente.setTabOrder(self.tableWidget_2, self.buttonBox)

    def retranslateUi(self, vtnDevolucionDeCliente):
        vtnDevolucionDeCliente.setWindowTitle(_translate("vtnDevolucionDeCliente", "Devolución de Cliente", None))
        self.pushButton.setText(_translate("vtnDevolucionDeCliente", "Buscar", None))
        self.label.setText(_translate("vtnDevolucionDeCliente", "Factura", None))
        self.label_3.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        self.label_2.setText(_translate("vtnDevolucionDeCliente", "Número", None))
        self.label_4.setText(_translate("vtnDevolucionDeCliente", "Nota de Crédito", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnDevolucionDeCliente", "Código Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnDevolucionDeCliente", "Importe", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnDevolucionDeCliente", "Código Barra", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnDevolucionDeCliente", "Cantidad", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnDevolucionDeCliente", "Importe", None))
        self.pushButton_2.setText(_translate("vtnDevolucionDeCliente", "Agergar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnDevolucionDeCliente = QtGui.QWidget()
    ui = Ui_vtnDevolucionDeCliente()
    ui.setupUi(vtnDevolucionDeCliente)
    vtnDevolucionDeCliente.show()
    sys.exit(app.exec_())

