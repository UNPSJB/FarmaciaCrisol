# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnListar.ui'
#
# Created: Thu Dec  4 14:19:46 2014
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

class Ui_vtnListar(object):
    def setupUi(self, vtnListar):
        vtnListar.setObjectName(_fromUtf8("vtnListar"))
        vtnListar.resize(418, 149)
        self.formLayout = QtGui.QFormLayout(vtnListar)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.comboBox = QtGui.QComboBox(vtnListar)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(vtnListar)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dateEdit = QtGui.QDateEdit(vtnListar)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout.addWidget(self.dateEdit)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(vtnListar)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.dateEdit_2 = QtGui.QDateEdit(vtnListar)
        self.dateEdit_2.setObjectName(_fromUtf8("dateEdit_2"))
        self.horizontalLayout_2.addWidget(self.dateEdit_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(vtnListar)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)

        self.retranslateUi(vtnListar)
        QtCore.QMetaObject.connectSlotsByName(vtnListar)

    def retranslateUi(self, vtnListar):
        vtnListar.setWindowTitle(_translate("vtnListar", "Listar", None))
        self.comboBox.setItemText(0, _translate("vtnListar", "Facturas Liquidadas Pendientes de Cobro", None))
        self.comboBox.setItemText(1, _translate("vtnListar", "Productos en Stock", None))
        self.comboBox.setItemText(2, _translate("vtnListar", "Ventas Realizadas", None))
        self.comboBox.setItemText(3, _translate("vtnListar", "Clientes", None))
        self.label.setText(_translate("vtnListar", "Fecha Desde", None))
        self.label_2.setText(_translate("vtnListar", "Fecha Hasta", None))
        self.pushButton.setText(_translate("vtnListar", "Listar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnListar = QtGui.QWidget()
    ui = Ui_vtnListar()
    ui.setupUi(vtnListar)
    vtnListar.show()
    sys.exit(app.exec_())

