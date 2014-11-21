# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAltaMonodroga.ui'
#
# Created: Tue Oct 28 16:55:59 2014
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

class Ui_vtnAltaMonodroga(object):
    def setupUi(self, vtnAltaMonodroga):
        vtnAltaMonodroga.setObjectName(_fromUtf8("vtnAltaMonodroga"))
        vtnAltaMonodroga.resize(492, 284)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaMonodroga)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaMonodroga)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 2, 1, 1)
        self.label = QtGui.QLabel(vtnAltaMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAltaMonodroga)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_4 = QtGui.QLabel(vtnAltaMonodroga)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.cmbTipoVenta = QtGui.QComboBox(vtnAltaMonodroga)
        self.cmbTipoVenta.setObjectName(_fromUtf8("cmbTipoVenta"))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.cmbTipoVenta.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbTipoVenta, 1, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.lineNomb = QtGui.QLineEdit(vtnAltaMonodroga)
        self.lineNomb.setObjectName(_fromUtf8("lineNomb"))
        self.gridLayout.addWidget(self.lineNomb, 0, 1, 1, 2)
        self.txtDescripcion = QtGui.QTextEdit(vtnAltaMonodroga)
        self.txtDescripcion.setObjectName(_fromUtf8("txtDescripcion"))
        self.gridLayout.addWidget(self.txtDescripcion, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaMonodroga)
        vtnAltaMonodroga.setTabOrder(self.lineNomb, self.cmbTipoVenta)
        vtnAltaMonodroga.setTabOrder(self.cmbTipoVenta, self.txtDescripcion)
        vtnAltaMonodroga.setTabOrder(self.txtDescripcion, self.buttonBox)

    def retranslateUi(self, vtnAltaMonodroga):
        vtnAltaMonodroga.setWindowTitle(_translate("vtnAltaMonodroga", "Alta Monodroga", None))
        self.label.setText(_translate("vtnAltaMonodroga", "Nombre", None))
        self.label_2.setText(_translate("vtnAltaMonodroga", "* Descripción", None))
        self.label_4.setText(_translate("vtnAltaMonodroga", "Tipo de Venta", None))
        self.cmbTipoVenta.setStatusTip(_translate("vtnAltaMonodroga", "Seleccione el tipo de venta que la monodroga exige", None))
        self.cmbTipoVenta.setItemText(0, _translate("vtnAltaMonodroga", "Libre", None))
        self.cmbTipoVenta.setItemText(1, _translate("vtnAltaMonodroga", "Receta", None))
        self.cmbTipoVenta.setItemText(2, _translate("vtnAltaMonodroga", "Receta Archivada", None))
        self.lineNomb.setStatusTip(_translate("vtnAltaMonodroga", "Ingrese el nombre de la monodroga (solo letras)", None))
        self.lineNomb.setAccessibleDescription(_translate("vtnAltaMonodroga", "palabra", None))
        self.txtDescripcion.setStatusTip(_translate("vtnAltaMonodroga", "Ingrese la descripción de la monodroga (opcional)", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaMonodroga = QtGui.QWidget()
    ui = Ui_vtnAltaMonodroga()
    ui.setupUi(vtnAltaMonodroga)
    vtnAltaMonodroga.show()
    sys.exit(app.exec_())

