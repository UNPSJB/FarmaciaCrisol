# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnMonodroga.ui'
#
# Created: Wed Apr  1 14:28:26 2015
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

class Ui_vtnMonodroga(object):
    def setupUi(self, vtnMonodroga):
        vtnMonodroga.setObjectName(_fromUtf8("vtnMonodroga"))
        vtnMonodroga.resize(568, 483)
        self.formLayout = QtGui.QFormLayout(vtnMonodroga)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(vtnMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineNombre = QtGui.QLineEdit(vtnMonodroga)
        self.lineNombre.setObjectName(_fromUtf8("lineNombre"))
        self.horizontalLayout.addWidget(self.lineNombre)
        self.btnBuscar = QtGui.QPushButton(vtnMonodroga)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_4 = QtGui.QLabel(vtnMonodroga)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cmbTipoVenta = QtGui.QComboBox(vtnMonodroga)
        self.cmbTipoVenta.setObjectName(_fromUtf8("cmbTipoVenta"))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbTipoVenta)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(vtnMonodroga)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txtDescripcion = QtGui.QTextEdit(vtnMonodroga)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtDescripcion)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnAceptar = QtGui.QPushButton(vtnMonodroga)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_3.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnMonodroga)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_3.addWidget(self.btnCancelar)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.groupMonodroga = QtGui.QGroupBox(vtnMonodroga)
        self.groupMonodroga.setObjectName(_fromUtf8("groupMonodroga"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupMonodroga)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.tablaMonodroga = QtGui.QTableWidget(self.groupMonodroga)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setTabKeyNavigation(True)
        self.tablaMonodroga.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaMonodroga.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(3)
        self.tablaMonodroga.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaMonodroga.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMonodroga.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaMonodroga.setHorizontalHeaderItem(2, item)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.tablaMonodroga)
        self.formLayout.setWidget(3, QtGui.QFormLayout.SpanningRole, self.groupMonodroga)

        self.retranslateUi(vtnMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnMonodroga)
        vtnMonodroga.setTabOrder(self.lineNombre, self.btnBuscar)
        vtnMonodroga.setTabOrder(self.btnBuscar, self.cmbTipoVenta)
        vtnMonodroga.setTabOrder(self.cmbTipoVenta, self.txtDescripcion)
        vtnMonodroga.setTabOrder(self.txtDescripcion, self.tablaMonodroga)
        vtnMonodroga.setTabOrder(self.tablaMonodroga, self.btnAceptar)
        vtnMonodroga.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnMonodroga):
        vtnMonodroga.setWindowTitle(_translate("vtnMonodroga", "Alta Monodroga", None))
        self.label.setText(_translate("vtnMonodroga", "Nombre", None))
        self.lineNombre.setStatusTip(_translate("vtnMonodroga", "Ingrese el nombre de la monodroga (solo letras)", None))
        self.lineNombre.setAccessibleDescription(_translate("vtnMonodroga", "palabra", None))
        self.btnBuscar.setText(_translate("vtnMonodroga", "Buscar", None))
        self.label_4.setText(_translate("vtnMonodroga", "Tipo de Venta", None))
        self.cmbTipoVenta.setStatusTip(_translate("vtnMonodroga", "Seleccione el tipo de venta que la monodroga exige", None))
        self.cmbTipoVenta.setItemText(0, _translate("vtnMonodroga", "Libre", None))
        self.cmbTipoVenta.setItemText(1, _translate("vtnMonodroga", "Receta", None))
        self.cmbTipoVenta.setItemText(2, _translate("vtnMonodroga", "Receta Archivada", None))
        self.label_2.setText(_translate("vtnMonodroga", "* Descripción", None))
        self.txtDescripcion.setStatusTip(_translate("vtnMonodroga", "Ingrese la descripción de la monodroga (opcional)", None))
        self.btnAceptar.setText(_translate("vtnMonodroga", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnMonodroga", "Cancelar", None))
        self.groupMonodroga.setTitle(_translate("vtnMonodroga", "Monodroga", None))
        item = self.tablaMonodroga.horizontalHeaderItem(0)
        item.setText(_translate("vtnMonodroga", "Nombre", None))
        item = self.tablaMonodroga.horizontalHeaderItem(1)
        item.setText(_translate("vtnMonodroga", "Tipo de Venta", None))
        item = self.tablaMonodroga.horizontalHeaderItem(2)
        item.setText(_translate("vtnMonodroga", "Descripción", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnMonodroga = QtGui.QWidget()
    ui = Ui_vtnMonodroga()
    ui.setupUi(vtnMonodroga)
    vtnMonodroga.show()
    sys.exit(app.exec_())

