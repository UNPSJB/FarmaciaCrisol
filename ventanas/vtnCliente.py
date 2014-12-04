# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnCliente.ui'
#
# Created: Thu Dec  4 14:19:45 2014
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

class Ui_vtnCliente(object):
    def setupUi(self, vtnCliente):
        vtnCliente.setObjectName(_fromUtf8("vtnCliente"))
        vtnCliente.resize(701, 418)
        self.formLayout = QtGui.QFormLayout(vtnCliente)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_2 = QtGui.QLabel(vtnCliente)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineDni = QtGui.QLineEdit(vtnCliente)
        self.lineDni.setObjectName(_fromUtf8("lineDni"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineDni)
        self.label_5 = QtGui.QLabel(vtnCliente)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.lineNombre = QtGui.QLineEdit(vtnCliente)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineNombre)
        self.label = QtGui.QLabel(vtnCliente)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.lineApellido = QtGui.QLineEdit(vtnCliente)
        self.lineApellido.setObjectName(_fromUtf8("lineApellido"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineApellido)
        self.label_3 = QtGui.QLabel(vtnCliente)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineDireccion = QtGui.QLineEdit(vtnCliente)
        self.lineDireccion.setObjectName(_fromUtf8("lineDireccion"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineDireccion)
        self.groupBuscar = QtGui.QGroupBox(vtnCliente)
        self.groupBuscar.setObjectName(_fromUtf8("groupBuscar"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBuscar)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableClientes = QtGui.QTableWidget(self.groupBuscar)
        self.tableClientes.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableClientes.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableClientes.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableClientes.setObjectName(_fromUtf8("tableClientes"))
        self.tableClientes.setColumnCount(5)
        self.tableClientes.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(4, item)
        self.tableClientes.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableClientes)
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.groupBuscar)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAceptar = QtGui.QPushButton(vtnCliente)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnCliente)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.formLayout.setLayout(8, QtGui.QFormLayout.SpanningRole, self.horizontalLayout)
        self.lineTelefono = QtGui.QLineEdit(vtnCliente)
        self.lineTelefono.setEnabled(True)
        self.lineTelefono.setObjectName(_fromUtf8("lineTelefono"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineTelefono)
        self.label_4 = QtGui.QLabel(vtnCliente)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnBuscar = QtGui.QPushButton(vtnCliente)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout_2.addWidget(self.btnBuscar)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)

        self.retranslateUi(vtnCliente)
        QtCore.QMetaObject.connectSlotsByName(vtnCliente)
        vtnCliente.setTabOrder(self.lineDni, self.lineNombre)
        vtnCliente.setTabOrder(self.lineNombre, self.lineApellido)
        vtnCliente.setTabOrder(self.lineApellido, self.btnBuscar)
        vtnCliente.setTabOrder(self.btnBuscar, self.lineDireccion)
        vtnCliente.setTabOrder(self.lineDireccion, self.lineTelefono)
        vtnCliente.setTabOrder(self.lineTelefono, self.tableClientes)
        vtnCliente.setTabOrder(self.tableClientes, self.btnAceptar)
        vtnCliente.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnCliente):
        vtnCliente.setWindowTitle(_translate("vtnCliente", "Form", None))
        self.label_2.setText(_translate("vtnCliente", "DNI", None))
        self.lineDni.setAccessibleDescription(_translate("vtnCliente", "dni", None))
        self.label_5.setText(_translate("vtnCliente", "Nombre", None))
        self.lineNombre.setAccessibleDescription(_translate("vtnCliente", "nya", None))
        self.label.setText(_translate("vtnCliente", "Apellido", None))
        self.lineApellido.setAccessibleDescription(_translate("vtnCliente", "nya", None))
        self.label_3.setText(_translate("vtnCliente", "Dirección", None))
        self.lineDireccion.setAccessibleDescription(_translate("vtnCliente", "direccion", None))
        self.groupBuscar.setTitle(_translate("vtnCliente", "Clientes", None))
        item = self.tableClientes.horizontalHeaderItem(0)
        item.setText(_translate("vtnCliente", "DNI", None))
        item = self.tableClientes.horizontalHeaderItem(1)
        item.setText(_translate("vtnCliente", "Nombre", None))
        item = self.tableClientes.horizontalHeaderItem(2)
        item.setText(_translate("vtnCliente", "Apellido", None))
        item = self.tableClientes.horizontalHeaderItem(3)
        item.setText(_translate("vtnCliente", "Dirección", None))
        item = self.tableClientes.horizontalHeaderItem(4)
        item.setText(_translate("vtnCliente", "Teléfono", None))
        self.btnAceptar.setText(_translate("vtnCliente", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnCliente", "Cancelar", None))
        self.lineTelefono.setAccessibleDescription(_translate("vtnCliente", "telefono", None))
        self.label_4.setText(_translate("vtnCliente", "Teléfono", None))
        self.btnBuscar.setText(_translate("vtnCliente", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnCliente = QtGui.QWidget()
    ui = Ui_vtnCliente()
    ui.setupUi(vtnCliente)
    vtnCliente.show()
    sys.exit(app.exec_())

