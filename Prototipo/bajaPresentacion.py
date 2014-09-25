# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaPresentacion.ui'
#
# Created: Wed Sep 24 13:59:38 2014
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

class Ui_vtnBajaPresentacion(object):
    def setupUi(self, vtnBajaPresentacion):
        vtnBajaPresentacion.setObjectName(_fromUtf8("vtnBajaPresentacion"))
        vtnBajaPresentacion.resize(526, 229)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaPresentacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaPresentacion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnBajaPresentacion)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaPresentacion)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaPresentacion)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.tableWidget = QtGui.QTableWidget(vtnBajaPresentacion)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaPresentacion)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaPresentacion)
        vtnBajaPresentacion.setTabOrder(self.lineEdit, self.pushButton)
        vtnBajaPresentacion.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaPresentacion.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaPresentacion):
        vtnBajaPresentacion.setWindowTitle(_translate("vtnBajaPresentacion", "Baja Presentación", None))
        self.label.setText(_translate("vtnBajaPresentacion", "Tipo", None))
        self.pushButton.setText(_translate("vtnBajaPresentacion", "Buscar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaPresentacion", "Tipo", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaPresentacion", "Unidad de Medidad", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnBajaPresentacion", "Cantidad de Fracciones", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaPresentacion = QtGui.QWidget()
    ui = Ui_vtnBajaPresentacion()
    ui.setupUi(vtnBajaPresentacion)
    vtnBajaPresentacion.show()
    sys.exit(app.exec_())

