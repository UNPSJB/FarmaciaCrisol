# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaLote.ui'
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

class Ui_vtnBajaLote(object):
    def setupUi(self, vtnBajaLote):
        vtnBajaLote.setObjectName(_fromUtf8("vtnBajaLote"))
        vtnBajaLote.resize(461, 236)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaLote)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdit = QtGui.QLineEdit(vtnBajaLote)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(vtnBajaLote)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaLote)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnBajaLote)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaLote)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaLote)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaLote)
        vtnBajaLote.setTabOrder(self.lineEdit, self.pushButton)
        vtnBajaLote.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaLote.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaLote):
        vtnBajaLote.setWindowTitle(_translate("vtnBajaLote", "Baja Lote", None))
        self.label.setText(_translate("vtnBajaLote", "Número", None))
        self.pushButton.setText(_translate("vtnBajaLote", "Buscar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaLote", "Número", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaLote", "Fecha de Vencimiento", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaLote = QtGui.QWidget()
    ui = Ui_vtnBajaLote()
    ui.setupUi(vtnBajaLote)
    vtnBajaLote.show()
    sys.exit(app.exec_())

