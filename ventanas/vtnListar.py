# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnListar.ui'
#
# Created: Wed Apr  1 14:28:27 2015
#      by: PyQt4 UI code generator 4.11.2
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
        vtnListar.resize(418, 168)
        self.formLayout = QtGui.QFormLayout(vtnListar)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.cbTipoListado = QtGui.QComboBox(vtnListar)
        self.cbTipoListado.setObjectName(_fromUtf8("cbTipoListado"))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.cbTipoListado.addItem(_fromUtf8(""))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.cbTipoListado)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(vtnListar)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.deFechaDesde = QtGui.QDateEdit(vtnListar)
        self.deFechaDesde.setObjectName(_fromUtf8("deFechaDesde"))
        self.horizontalLayout.addWidget(self.deFechaDesde)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.deFechaHasta = QtGui.QLabel(vtnListar)
        self.deFechaHasta.setObjectName(_fromUtf8("deFechaHasta"))
        self.horizontalLayout_2.addWidget(self.deFechaHasta)
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
        self.btnListar = QtGui.QPushButton(vtnListar)
        self.btnListar.setObjectName(_fromUtf8("btnListar"))
        self.horizontalLayout_3.addWidget(self.btnListar)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)

        self.retranslateUi(vtnListar)
        QtCore.QMetaObject.connectSlotsByName(vtnListar)

    def retranslateUi(self, vtnListar):
        vtnListar.setWindowTitle(_translate("vtnListar", "Listar", None))
        self.cbTipoListado.setItemText(0, _translate("vtnListar", "Facturas Liquidadas Pendientes de Cobro", None))
        self.cbTipoListado.setItemText(1, _translate("vtnListar", "Productos en Stock", None))
        self.cbTipoListado.setItemText(2, _translate("vtnListar", "Ventas Realizadas", None))
        self.cbTipoListado.setItemText(3, _translate("vtnListar", "Clientes", None))
        self.label.setText(_translate("vtnListar", "Fecha Desde", None))
        self.deFechaHasta.setText(_translate("vtnListar", "Fecha Hasta", None))
        self.btnListar.setText(_translate("vtnListar", "Listar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnListar = QtGui.QWidget()
    ui = Ui_vtnListar()
    ui.setupUi(vtnListar)
    vtnListar.show()
    sys.exit(app.exec_())

