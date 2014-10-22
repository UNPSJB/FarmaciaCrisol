# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarLote.ui'
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

class Ui_vtnModificarLote(object):
    def setupUi(self, vtnModificarLote):
        vtnModificarLote.setObjectName(_fromUtf8("vtnModificarLote"))
        vtnModificarLote.resize(638, 303)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarLote)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarLote)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 1, 1, 2)
        self.pushButton = QtGui.QPushButton(vtnModificarLote)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.dateEdit = QtGui.QDateEdit(vtnModificarLote)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label_2 = QtGui.QLabel(vtnModificarLote)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label = QtGui.QLabel(vtnModificarLote)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tableWidget = QtGui.QTableWidget(vtnModificarLote)
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
        self.lineEdit = QtGui.QLineEdit(vtnModificarLote)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarLote)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarLote)
        vtnModificarLote.setTabOrder(self.lineEdit, self.pushButton)
        vtnModificarLote.setTabOrder(self.pushButton, self.tableWidget)
        vtnModificarLote.setTabOrder(self.tableWidget, self.dateEdit)
        vtnModificarLote.setTabOrder(self.dateEdit, self.buttonBox)

    def retranslateUi(self, vtnModificarLote):
        vtnModificarLote.setWindowTitle(_translate("vtnModificarLote", "Modificar Lote", None))
        self.pushButton.setText(_translate("vtnModificarLote", "Buscar", None))
        self.label_2.setText(_translate("vtnModificarLote", "* Fecha de Vencimiento", None))
        self.label.setText(_translate("vtnModificarLote", "Número", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnModificarLote", "Número", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnModificarLote", "Fecha de Vencimiento", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarLote = QtGui.QWidget()
    ui = Ui_vtnModificarLote()
    ui.setupUi(vtnModificarLote)
    vtnModificarLote.show()
    sys.exit(app.exec_())

