# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarPresentacion.ui'
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

class Ui_vtnModificarPresentacion(object):
    def setupUi(self, vtnModificarPresentacion):
        vtnModificarPresentacion.setObjectName(_fromUtf8("vtnModificarPresentacion"))
        vtnModificarPresentacion.resize(638, 348)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarPresentacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(vtnModificarPresentacion)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(vtnModificarPresentacion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarPresentacion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label = QtGui.QLabel(vtnModificarPresentacion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(vtnModificarPresentacion)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 3, 1, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 4, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarPresentacion)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 2)
        self.tableWidget = QtGui.QTableWidget(vtnModificarPresentacion)
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

        self.retranslateUi(vtnModificarPresentacion)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarPresentacion)
        vtnModificarPresentacion.setTabOrder(self.lineEdit, self.pushButton)
        vtnModificarPresentacion.setTabOrder(self.pushButton, self.tableWidget)
        vtnModificarPresentacion.setTabOrder(self.tableWidget, self.lineEdit_2)
        vtnModificarPresentacion.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        vtnModificarPresentacion.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        vtnModificarPresentacion.setTabOrder(self.lineEdit_4, self.buttonBox)

    def retranslateUi(self, vtnModificarPresentacion):
        vtnModificarPresentacion.setWindowTitle(_translate("vtnModificarPresentacion", "Modificar Presentación", None))
        self.pushButton.setText(_translate("vtnModificarPresentacion", "Buscar", None))
        self.label_3.setText(_translate("vtnModificarPresentacion", "Tipo", None))
        self.label_2.setText(_translate("vtnModificarPresentacion", "Unidad de Medida", None))
        self.label.setText(_translate("vtnModificarPresentacion", "Tipo", None))
        self.label_4.setText(_translate("vtnModificarPresentacion", "Cantidad de Fraciones", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("vtnModificarPresentacion", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("vtnModificarPresentacion", "Unidad de Medida", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("vtnModificarPresentacion", "Cantidad de Fracciones", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarPresentacion = QtGui.QWidget()
    ui = Ui_vtnModificarPresentacion()
    ui.setupUi(vtnModificarPresentacion)
    vtnModificarPresentacion.show()
    sys.exit(app.exec_())

