# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarMedicamento.ui'
#
# Created: Fri Sep 26 11:13:14 2014
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

class Ui_vtnModificarMedicamento(object):
    def setupUi(self, vtnModificarMedicamento):
        vtnModificarMedicamento.setObjectName(_fromUtf8("vtnModificarMedicamento"))
        vtnModificarMedicamento.resize(646, 342)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnModificarMedicamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(vtnModificarMedicamento)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 4, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnModificarMedicamento)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 2)
        self.pushButton = QtGui.QPushButton(vtnModificarMedicamento)
        self.pushButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(vtnModificarMedicamento)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 6, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 6, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnModificarMedicamento)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 4, 2, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 7, 3, 1, 2)
        self.tableWidget = QtGui.QTableWidget(vtnModificarMedicamento)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 2, 1, 1, 4)
        self.label_3 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.tableWidget_2 = QtGui.QTableWidget(vtnModificarMedicamento)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget_2, 5, 1, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarMedicamento)
        vtnModificarMedicamento.setTabOrder(self.lineEdit, self.pushButton)
        vtnModificarMedicamento.setTabOrder(self.pushButton, self.tableWidget)
        vtnModificarMedicamento.setTabOrder(self.tableWidget, self.lineEdit_2)
        vtnModificarMedicamento.setTabOrder(self.lineEdit_2, self.pushButton_2)
        vtnModificarMedicamento.setTabOrder(self.pushButton_2, self.tableWidget_2)
        vtnModificarMedicamento.setTabOrder(self.tableWidget_2, self.lineEdit_3)
        vtnModificarMedicamento.setTabOrder(self.lineEdit_3, self.buttonBox)

    def retranslateUi(self, vtnModificarMedicamento):
        vtnModificarMedicamento.setWindowTitle(_translate("vtnModificarMedicamento", "Modificar Medicamento", None))
        self.label.setText(_translate("vtnModificarMedicamento", "Nombre", None))
        self.label_4.setText(_translate("vtnModificarMedicamento", "Medicamento", None))
        self.pushButton_2.setText(_translate("vtnModificarMedicamento", "Buscar", None))
        self.pushButton.setText(_translate("vtnModificarMedicamento", "Buscar", None))
        self.label_2.setText(_translate("vtnModificarMedicamento", "* Cantidad de Monodroga", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnModificarMedicamento", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnModificarMedicamento", "Monodroga", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnModificarMedicamento", "Cantidad de Monodroga", None))
        self.label_3.setText(_translate("vtnModificarMedicamento", "Monodroga", None))
        self.label_5.setText(_translate("vtnModificarMedicamento", "* Nombre", None))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("vtnModificarMedicamento", "Nombre", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("vtnModificarMedicamento", "Receta", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("vtnModificarMedicamento", "Receta Archivada", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("vtnModificarMedicamento", "Descripción", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarMedicamento = QtGui.QWidget()
    ui = Ui_vtnModificarMedicamento()
    ui.setupUi(vtnModificarMedicamento)
    vtnModificarMedicamento.show()
    sys.exit(app.exec_())

