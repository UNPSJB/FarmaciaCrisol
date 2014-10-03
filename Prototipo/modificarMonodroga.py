# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarMonodroga.ui'
#
# Created: Wed Oct  1 13:55:07 2014
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

class Ui_vtnModificarMonodroga(object):
    def setupUi(self, vtnModificarMonodroga):
        vtnModificarMonodroga.setObjectName(_fromUtf8("vtnModificarMonodroga"))
        vtnModificarMonodroga.resize(659, 396)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarMonodroga)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableWidget = QtGui.QTableWidget(vtnModificarMonodroga)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 4)
        self.textEdit = QtGui.QTextEdit(vtnModificarMonodroga)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 4, 1, 1, 1)
        self.checkBox = QtGui.QCheckBox(vtnModificarMonodroga)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 2, 1, 1, 1)
        self.label = QtGui.QLabel(vtnModificarMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(vtnModificarMonodroga)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, QtCore.Qt.AlignTop)
        self.pushButton = QtGui.QPushButton(vtnModificarMonodroga)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)
        self.checkBox_2 = QtGui.QCheckBox(vtnModificarMonodroga)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 3, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarMonodroga)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 2, 1, 2)
        self.lineEdit = QtGui.QLineEdit(vtnModificarMonodroga)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarMonodroga)
        vtnModificarMonodroga.setTabOrder(self.lineEdit, self.pushButton)
        vtnModificarMonodroga.setTabOrder(self.pushButton, self.tableWidget)
        vtnModificarMonodroga.setTabOrder(self.tableWidget, self.checkBox)
        vtnModificarMonodroga.setTabOrder(self.checkBox, self.checkBox_2)
        vtnModificarMonodroga.setTabOrder(self.checkBox_2, self.textEdit)
        vtnModificarMonodroga.setTabOrder(self.textEdit, self.buttonBox)

    def retranslateUi(self, vtnModificarMonodroga):
        vtnModificarMonodroga.setWindowTitle(_translate("vtnModificarMonodroga", "Modificar Monodroga", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnModificarMonodroga", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnModificarMonodroga", "Receta Archivada", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnModificarMonodroga", "Receta", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("vtnModificarMonodroga", "Descripción", None))
        self.checkBox.setText(_translate("vtnModificarMonodroga", "* Receta Archivada?", None))
        self.label.setText(_translate("vtnModificarMonodroga", "Nombre", None))
        self.label_3.setText(_translate("vtnModificarMonodroga", "* Descripción", None))
        self.pushButton.setText(_translate("vtnModificarMonodroga", "Buscar", None))
        self.checkBox_2.setText(_translate("vtnModificarMonodroga", "* Receta?", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarMonodroga = QtGui.QWidget()
    ui = Ui_vtnModificarMonodroga()
    ui.setupUi(vtnModificarMonodroga)
    vtnModificarMonodroga.show()
    sys.exit(app.exec_())

