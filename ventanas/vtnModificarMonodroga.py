# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnModificarMonodroga.ui'
#
# Created: Tue Oct 28 16:56:00 2014
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
        self.label_3 = QtGui.QLabel(vtnModificarMonodroga)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label = QtGui.QLabel(vtnModificarMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.txtDescripcion = QtGui.QTextEdit(vtnModificarMonodroga)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.gridLayout.addWidget(self.txtDescripcion, 3, 1, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnModificarMonodroga)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.lineNomb = QtGui.QLineEdit(vtnModificarMonodroga)
        self.lineNomb.setObjectName(_fromUtf8("lineNomb"))
        self.gridLayout.addWidget(self.lineNomb, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarMonodroga)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.cmbTipoVenta = QtGui.QComboBox(vtnModificarMonodroga)
        self.cmbTipoVenta.setObjectName(_fromUtf8("cmbTipoVenta"))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbTipoVenta, 2, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarMonodroga)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 2)
        self.tablaMonodroga = QtGui.QTableWidget(vtnModificarMonodroga)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(0)
        self.tablaMonodroga.setRowCount(0)
        self.tablaMonodroga.horizontalHeader().setDefaultSectionSize(130)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.tablaMonodroga.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tablaMonodroga, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarMonodroga)
        vtnModificarMonodroga.setTabOrder(self.lineNomb, self.btnBuscar)
        vtnModificarMonodroga.setTabOrder(self.btnBuscar, self.tablaMonodroga)
        vtnModificarMonodroga.setTabOrder(self.tablaMonodroga, self.cmbTipoVenta)
        vtnModificarMonodroga.setTabOrder(self.cmbTipoVenta, self.txtDescripcion)
        vtnModificarMonodroga.setTabOrder(self.txtDescripcion, self.buttonBox)

    def retranslateUi(self, vtnModificarMonodroga):
        vtnModificarMonodroga.setWindowTitle(_translate("vtnModificarMonodroga", "Modificar Monodroga", None))
        self.label_3.setText(_translate("vtnModificarMonodroga", "* Descripción", None))
        self.label.setText(_translate("vtnModificarMonodroga", "Nombre", None))
        self.txtDescripcion.setStatusTip(_translate("vtnModificarMonodroga", "Ingrese la descripción de la monodroga", None))
        self.btnBuscar.setText(_translate("vtnModificarMonodroga", "Buscar", None))
        self.lineNomb.setStatusTip(_translate("vtnModificarMonodroga", "Ingrese nombre de la monodroga (solo letras)", None))
        self.lineNomb.setAccessibleDescription(_translate("vtnModificarMonodroga", "palabra", None))
        self.label_2.setText(_translate("vtnModificarMonodroga", "* Tipo de Venta", None))
        self.cmbTipoVenta.setStatusTip(_translate("vtnModificarMonodroga", "Seleccione el tipo de venta que exige la monodroga", None))
        self.cmbTipoVenta.setItemText(0, _translate("vtnModificarMonodroga", "Libre", None))
        self.cmbTipoVenta.setItemText(1, _translate("vtnModificarMonodroga", "Receta", None))
        self.cmbTipoVenta.setItemText(2, _translate("vtnModificarMonodroga", "Receta Archivada", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarMonodroga = QtGui.QWidget()
    ui = Ui_vtnModificarMonodroga()
    ui.setupUi(vtnModificarMonodroga)
    vtnModificarMonodroga.show()
    sys.exit(app.exec_())

