# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnLote.ui'
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

class Ui_vtnLote(object):
    def setupUi(self, vtnLote):
        vtnLote.setObjectName(_fromUtf8("vtnLote"))
        vtnLote.resize(622, 503)
        self.verticalLayout = QtGui.QVBoxLayout(vtnLote)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbLote = QtGui.QGroupBox(vtnLote)
        self.gbLote.setObjectName(_fromUtf8("gbLote"))
        self.formLayout = QtGui.QFormLayout(self.gbLote)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.gbLote)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lineCodigo = QtGui.QLineEdit(self.gbLote)
        self.lineCodigo.setObjectName(_fromUtf8("lineCodigo"))
        self.horizontalLayout_2.addWidget(self.lineCodigo)
        self.btnBuscarLote = QtGui.QPushButton(self.gbLote)
        self.btnBuscarLote.setObjectName(_fromUtf8("btnBuscarLote"))
        self.horizontalLayout_2.addWidget(self.btnBuscarLote)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(self.gbLote)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.dateFechVenc = QtGui.QDateEdit(self.gbLote)
        self.dateFechVenc.setObjectName(_fromUtf8("dateFechVenc"))
        self.horizontalLayout_3.addWidget(self.dateFechVenc)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.labelCantidad = QtGui.QLabel(self.gbLote)
        self.labelCantidad.setObjectName(_fromUtf8("labelCantidad"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.labelCantidad)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.spinCantidad = QtGui.QSpinBox(self.gbLote)
        self.spinCantidad.setMinimum(1)
        self.spinCantidad.setMaximum(500)
        self.spinCantidad.setSingleStep(10)
        self.spinCantidad.setObjectName(_fromUtf8("spinCantidad"))
        self.horizontalLayout_8.addWidget(self.spinCantidad)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.tablaLote = QtGui.QTableWidget(self.gbLote)
        self.tablaLote.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaLote.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaLote.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaLote.setObjectName(_fromUtf8("tablaLote"))
        self.tablaLote.setColumnCount(2)
        self.tablaLote.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaLote.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaLote.setHorizontalHeaderItem(1, item)
        self.tablaLote.horizontalHeader().setDefaultSectionSize(160)
        self.tablaLote.horizontalHeader().setStretchLastSection(True)
        self.formLayout.setWidget(4, QtGui.QFormLayout.SpanningRole, self.tablaLote)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.btnActualizarLote = QtGui.QPushButton(self.gbLote)
        self.btnActualizarLote.setObjectName(_fromUtf8("btnActualizarLote"))
        self.horizontalLayout_9.addWidget(self.btnActualizarLote)
        self.formLayout.setLayout(5, QtGui.QFormLayout.FieldRole, self.horizontalLayout_9)
        self.verticalLayout.addWidget(self.gbLote)
        self.gbProducto = QtGui.QGroupBox(vtnLote)
        self.gbProducto.setObjectName(_fromUtf8("gbProducto"))
        self.formLayout_2 = QtGui.QFormLayout(self.gbProducto)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.gbProducto)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lineCod_Barra = QtGui.QLineEdit(self.gbProducto)
        self.lineCod_Barra.setObjectName(_fromUtf8("lineCod_Barra"))
        self.horizontalLayout.addWidget(self.lineCod_Barra)
        self.btnBuscarProd = QtGui.QPushButton(self.gbProducto)
        self.btnBuscarProd.setObjectName(_fromUtf8("btnBuscarProd"))
        self.horizontalLayout.addWidget(self.btnBuscarProd)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.tablaProducto = QtGui.QTableWidget(self.gbProducto)
        self.tablaProducto.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaProducto.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tablaProducto.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tablaProducto.setObjectName(_fromUtf8("tablaProducto"))
        self.tablaProducto.setColumnCount(4)
        self.tablaProducto.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tablaProducto.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tablaProducto.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tablaProducto.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tablaProducto.setHorizontalHeaderItem(3, item)
        self.tablaProducto.horizontalHeader().setDefaultSectionSize(160)
        self.tablaProducto.horizontalHeader().setStretchLastSection(True)
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.SpanningRole, self.tablaProducto)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.btnActualizarProd = QtGui.QPushButton(self.gbProducto)
        self.btnActualizarProd.setObjectName(_fromUtf8("btnActualizarProd"))
        self.horizontalLayout_7.addWidget(self.btnActualizarProd)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout.addWidget(self.gbProducto)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.btnAceptar = QtGui.QPushButton(vtnLote)
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.horizontalLayout_5.addWidget(self.btnAceptar)
        self.btnCancelar = QtGui.QPushButton(vtnLote)
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.horizontalLayout_5.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(vtnLote)
        QtCore.QMetaObject.connectSlotsByName(vtnLote)
        vtnLote.setTabOrder(self.lineCodigo, self.btnBuscarLote)
        vtnLote.setTabOrder(self.btnBuscarLote, self.dateFechVenc)
        vtnLote.setTabOrder(self.dateFechVenc, self.spinCantidad)
        vtnLote.setTabOrder(self.spinCantidad, self.tablaLote)
        vtnLote.setTabOrder(self.tablaLote, self.lineCod_Barra)
        vtnLote.setTabOrder(self.lineCod_Barra, self.btnBuscarProd)
        vtnLote.setTabOrder(self.btnBuscarProd, self.tablaProducto)
        vtnLote.setTabOrder(self.tablaProducto, self.btnActualizarProd)
        vtnLote.setTabOrder(self.btnActualizarProd, self.btnAceptar)
        vtnLote.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, vtnLote):
        vtnLote.setWindowTitle(_translate("vtnLote", "Alta Lote", None))
        self.gbLote.setTitle(_translate("vtnLote", "Lote", None))
        self.label.setText(_translate("vtnLote", "Código", None))
        self.lineCodigo.setStatusTip(_translate("vtnLote", "Ingrese el número de Lote del Producto (solo letras y números sin espacios)", None))
        self.lineCodigo.setAccessibleDescription(_translate("vtnLote", "codLote", None))
        self.btnBuscarLote.setText(_translate("vtnLote", "Buscar", None))
        self.label_2.setText(_translate("vtnLote", "Fecha de Vencimiento", None))
        self.dateFechVenc.setStatusTip(_translate("vtnLote", "Ingrese la fecha de vencimiento del lote", None))
        self.labelCantidad.setText(_translate("vtnLote", "Cantidad", None))
        self.spinCantidad.setStatusTip(_translate("vtnLote", "Ingrese la cantidad del Producto para dicho lote", None))
        item = self.tablaLote.horizontalHeaderItem(0)
        item.setText(_translate("vtnLote", "Código", None))
        item = self.tablaLote.horizontalHeaderItem(1)
        item.setText(_translate("vtnLote", "Fecha de Vencimiento", None))
        self.btnActualizarLote.setText(_translate("vtnLote", "Actualizar", None))
        self.gbProducto.setTitle(_translate("vtnLote", "Producto", None))
        self.label_4.setText(_translate("vtnLote", "* Código de Barra", None))
        self.lineCod_Barra.setStatusTip(_translate("vtnLote", "Ingrese código de barra del producto (exactamente 9 números)", None))
        self.lineCod_Barra.setAccessibleDescription(_translate("vtnLote", "codigo", None))
        self.btnBuscarProd.setText(_translate("vtnLote", "Buscar", None))
        item = self.tablaProducto.horizontalHeaderItem(0)
        item.setText(_translate("vtnLote", "Código de Barra", None))
        item = self.tablaProducto.horizontalHeaderItem(1)
        item.setText(_translate("vtnLote", "Medicamento", None))
        item = self.tablaProducto.horizontalHeaderItem(2)
        item.setText(_translate("vtnLote", "Presentación", None))
        item = self.tablaProducto.horizontalHeaderItem(3)
        item.setText(_translate("vtnLote", "Importe", None))
        self.btnActualizarProd.setText(_translate("vtnLote", "Actualizar", None))
        self.btnAceptar.setText(_translate("vtnLote", "Aceptar", None))
        self.btnCancelar.setText(_translate("vtnLote", "Cancelar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnLote = QtGui.QWidget()
    ui = Ui_vtnLote()
    ui.setupUi(vtnLote)
    vtnLote.show()
    sys.exit(app.exec_())

