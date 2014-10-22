# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarRemito.ui'
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

class Ui_vtnModificarRemito(object):
    def setupUi(self, vtnModificarRemito):
        vtnModificarRemito.setObjectName(_fromUtf8("vtnModificarRemito"))
        vtnModificarRemito.resize(544, 246)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarRemito)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(vtnModificarRemito)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnModificarRemito)
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
        self.pushButton = QtGui.QPushButton(vtnModificarRemito)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarRemito)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 2)
        self.lineEdit = QtGui.QLineEdit(vtnModificarRemito)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarRemito)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarRemito)
        vtnModificarRemito.setTabOrder(self.lineEdit, self.pushButton)
        vtnModificarRemito.setTabOrder(self.pushButton, self.tableWidget)
        vtnModificarRemito.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnModificarRemito):
        vtnModificarRemito.setWindowTitle(_translate("vtnModificarRemito", "Modificar Remito", None))
        self.label_2.setText(_translate("vtnModificarRemito", "Número", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnModificarRemito", "Código Barra", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnModificarRemito", "Cantidad", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnModificarRemito", "Importe", None))
        self.pushButton.setText(_translate("vtnModificarRemito", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarRemito = QtGui.QWidget()
    ui = Ui_vtnModificarRemito()
    ui.setupUi(vtnModificarRemito)
    vtnModificarRemito.show()
    sys.exit(app.exec_())

