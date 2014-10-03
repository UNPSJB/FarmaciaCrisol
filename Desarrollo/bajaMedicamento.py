# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaMedicamento.ui'
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

class Ui_vtnBajaMedicamento(object):
    def setupUi(self, vtnBajaMedicamento):
        vtnBajaMedicamento.setObjectName(_fromUtf8("vtnBajaMedicamento"))
        vtnBajaMedicamento.resize(579, 307)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaMedicamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnBajaMedicamento)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaMedicamento)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnBajaMedicamento)
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
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaMedicamento)
        vtnBajaMedicamento.setTabOrder(self.lineEdit, self.pushButton)
        vtnBajaMedicamento.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaMedicamento.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaMedicamento):
        vtnBajaMedicamento.setWindowTitle(_translate("vtnBajaMedicamento", "Baja Medicamento", None))
        self.label.setText(_translate("vtnBajaMedicamento", "Nombre", None))
        self.pushButton.setText(_translate("vtnBajaMedicamento", "Buscar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaMedicamento", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaMedicamento", "Monodroga", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnBajaMedicamento", "Cantidad de Monodroga", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaMedicamento = QtGui.QWidget()
    ui = Ui_vtnBajaMedicamento()
    ui.setupUi(vtnBajaMedicamento)
    vtnBajaMedicamento.show()
    sys.exit(app.exec_())

