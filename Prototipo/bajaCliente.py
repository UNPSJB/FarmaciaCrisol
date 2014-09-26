# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaCliente.ui'
#
# Created: Fri Sep 26 11:13:13 2014
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

class Ui_vtnBajaCliente(object):
    def setupUi(self, vtnBajaCliente):
        vtnBajaCliente.setObjectName(_fromUtf8("vtnBajaCliente"))
        vtnBajaCliente.resize(514, 250)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaCliente)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnBajaCliente)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaCliente)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnBajaCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaCliente)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 2)
        self.lineEdit = QtGui.QLineEdit(vtnBajaCliente)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.tableWidget = QtGui.QTableWidget(vtnBajaCliente)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaCliente)
        vtnBajaCliente.setTabOrder(self.lineEdit, self.lineEdit_2)
        vtnBajaCliente.setTabOrder(self.lineEdit_2, self.pushButton)
        vtnBajaCliente.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaCliente.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaCliente):
        vtnBajaCliente.setWindowTitle(_translate("vtnBajaCliente", "Baja Cliente", None))
        self.label.setText(_translate("vtnBajaCliente", "Nombre y Apellido", None))
        self.pushButton.setText(_translate("vtnBajaCliente", "Buscar", None))
        self.label_2.setText(_translate("vtnBajaCliente", "DNI", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaCliente", "Nombre y Apellido", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaCliente", "DNI", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnBajaCliente", "Dirección", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("vtnBajaCliente", "Teléfono", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaCliente = QtGui.QWidget()
    ui = Ui_vtnBajaCliente()
    ui.setupUi(vtnBajaCliente)
    vtnBajaCliente.show()
    sys.exit(app.exec_())

