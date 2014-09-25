# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaMonodroga.ui'
#
# Created: Wed Sep 24 13:59:39 2014
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

class Ui_vtnBajaMonodroga(object):
    def setupUi(self, vtnBajaMonodroga):
        vtnBajaMonodroga.setObjectName(_fromUtf8("vtnBajaMonodroga"))
        vtnBajaMonodroga.resize(553, 291)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaMonodroga)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnBajaMonodroga)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(vtnBajaMonodroga)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaMonodroga)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.tableWidget = QtGui.QTableWidget(vtnBajaMonodroga)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaMonodroga)
        vtnBajaMonodroga.setTabOrder(self.lineEdit, self.pushButton)
        vtnBajaMonodroga.setTabOrder(self.pushButton, self.tableWidget)
        vtnBajaMonodroga.setTabOrder(self.tableWidget, self.buttonBox)

    def retranslateUi(self, vtnBajaMonodroga):
        vtnBajaMonodroga.setWindowTitle(_translate("vtnBajaMonodroga", "Baja Monodroga", None))
        self.label.setText(_translate("vtnBajaMonodroga", "Nombre", None))
        self.pushButton.setText(_translate("vtnBajaMonodroga", "Buscar", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnBajaMonodroga", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnBajaMonodroga", "Descripción", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaMonodroga = QtGui.QWidget()
    ui = Ui_vtnBajaMonodroga()
    ui.setupUi(vtnBajaMonodroga)
    vtnBajaMonodroga.show()
    sys.exit(app.exec_())

