# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnPresentacion.ui'
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

class Ui_vtnPresentacion(object):
    def setupUi(self, vtnPresentacion):
        vtnPresentacion.setObjectName(_fromUtf8("vtnPresentacion"))
        vtnPresentacion.resize(701, 433)
        self.formLayout = QtGui.QFormLayout(vtnPresentacion)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(vtnPresentacion)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineTipo = QtGui.QLineEdit(vtnPresentacion)
        self.lineTipo.setObjectName(_fromUtf8("lineTipo"))
        self.horizontalLayout.addWidget(self.lineTipo)
        self.btnBuscar = QtGui.QPushButton(vtnPresentacion)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.horizontalLayout.addWidget(self.btnBuscar)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_2 = QtGui.QLabel(vtnPresentacion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lineUnidad_Medida = QtGui.QLineEdit(vtnPresentacion)
        self.lineUnidad_Medida.setObjectName(_fromUtf8("lineUnidad_Medida"))
        self.horizontalLayout_4.addWidget(self.lineUnidad_Medida)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_3 = QtGui.QLabel(vtnPresentacion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.groupPresentacion = QtGui.QGroupBox(vtnPresentacion)
        self.groupPresentacion.setObjectName(_fromUtf8("groupPresentacion"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupPresentacion)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.tablaPresentacion = QtGui.QTableWidget(self.groupPresentacion)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaPresentacion.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(5)
        self.tablaPresentacion.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaPresentacion.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPresentacion.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPresentacion.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPresentacion.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tablaPresentacion.setHorizontalHeaderItem(4, item)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.tablaPresentacion.verticalHeader().setVisible(True)
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.SpanningRole, self.tablaPresentacion)
        self.formLayout.setWidget(6, QtGui.QFormLayout.SpanningRole, self.groupPresentacion)
        self.groupFraccionable = QtGui.QGroupBox(vtnPresentacion)
        self.groupFraccionable.setObjectName(_fromUtf8("groupFraccionable"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupFraccionable)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.tablaFraccionable = QtGui.QTableWidget(self.groupFraccionable)
        self.tablaFraccionable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaFraccionable.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaFraccionable.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaFraccionable.setObjectName(_fromUtf8("tablaFraccionable"))
        self.tablaFraccionable.setColumnCount(3)
        self.tablaFraccionable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaFraccionable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaFraccionable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaFraccionable.setHorizontalHeaderItem(2, item)
        self.tablaFraccionable.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaFraccionable.horizontalHeader().setDefaultSectionSize(160)
        self.tablaFraccionable.horizontalHeader().setStretchLastSection(True)
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.SpanningRole, self.tablaFraccionable)
        self.formLayout.setWidget(7, QtGui.QFormLayout.SpanningRole, self.groupFraccionable)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.btnAceptar = QtGui.QPushButton(vtnPresentacion)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_5.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnPresentacion)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_5.addWidget(self.btnCancelar)
        self.formLayout.setLayout(8, QtGui.QFormLayout.SpanningRole, self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.spinCantidad = QtGui.QSpinBox(vtnPresentacion)
        self.spinCantidad.setMinimum(1)
        self.spinCantidad.setMaximum(500)
        self.spinCantidad.setSingleStep(10)
        self.spinCantidad.setObjectName(_fromUtf8("spinCantidad"))
        self.horizontalLayout_6.addWidget(self.spinCantidad)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_6)

        self.retranslateUi(vtnPresentacion)
        QtCore.QMetaObject.connectSlotsByName(vtnPresentacion)
        vtnPresentacion.setTabOrder(self.lineTipo, self.btnBuscar)
        vtnPresentacion.setTabOrder(self.btnBuscar, self.lineUnidad_Medida)
        vtnPresentacion.setTabOrder(self.lineUnidad_Medida, self.spinCantidad)
        vtnPresentacion.setTabOrder(self.spinCantidad, self.tablaPresentacion)
        vtnPresentacion.setTabOrder(self.tablaPresentacion, self.tablaFraccionable)
        vtnPresentacion.setTabOrder(self.tablaFraccionable, self.btnAceptar)
        vtnPresentacion.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnPresentacion):
        vtnPresentacion.setWindowTitle(_translate("vtnPresentacion", "Alta Presentación", None))
        self.label.setText(_translate("vtnPresentacion", "Tipo", None))
        self.lineTipo.setStatusTip(_translate("vtnPresentacion", "Ingrese el tipo de Presentación (solo letras)", None))
        self.lineTipo.setAccessibleDescription(_translate("vtnPresentacion", "texto", None))
        self.btnBuscar.setText(_translate("vtnPresentacion", "Buscar", None))
        self.label_2.setText(_translate("vtnPresentacion", "Unidad de Medida", None))
        self.lineUnidad_Medida.setStatusTip(_translate("vtnPresentacion", "Ingrese unidad de medida (solo letras)", None))
        self.lineUnidad_Medida.setAccessibleDescription(_translate("vtnPresentacion", "texto", None))
        self.label_3.setText(_translate("vtnPresentacion", "Cantidad de Fracciones", None))
        self.groupPresentacion.setTitle(_translate("vtnPresentacion", "Presentación", None))
        item = self.tablaPresentacion.horizontalHeaderItem(0)
        item.setText(_translate("vtnPresentacion", "Tipo", None))
        item = self.tablaPresentacion.horizontalHeaderItem(1)
        item.setText(_translate("vtnPresentacion", "Unidad de Medida", None))
        item = self.tablaPresentacion.horizontalHeaderItem(2)
        item.setText(_translate("vtnPresentacion", "Cantidad de Fracciones", None))
        item = self.tablaPresentacion.horizontalHeaderItem(3)
        item.setText(_translate("vtnPresentacion", "Fraccionable", None))
        item = self.tablaPresentacion.horizontalHeaderItem(4)
        item.setText(_translate("vtnPresentacion", "Super Presentación", None))
        self.groupFraccionable.setTitle(_translate("vtnPresentacion", "Fraccionable", None))
        item = self.tablaFraccionable.horizontalHeaderItem(0)
        item.setText(_translate("vtnPresentacion", "Tipo", None))
        item = self.tablaFraccionable.horizontalHeaderItem(1)
        item.setText(_translate("vtnPresentacion", "Unidad de Medida", None))
        item = self.tablaFraccionable.horizontalHeaderItem(2)
        item.setText(_translate("vtnPresentacion", "Cantidad de Fracciones", None))
        self.btnAceptar.setText(_translate("vtnPresentacion", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnPresentacion", "Cancelar", None))
        self.spinCantidad.setStatusTip(_translate("vtnPresentacion", "Ingrese la cantidad del Producto para dicho lote", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnPresentacion = QtGui.QWidget()
    ui = Ui_vtnPresentacion()
    ui.setupUi(vtnPresentacion)
    vtnPresentacion.show()
    sys.exit(app.exec_())
