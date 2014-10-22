# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaMedicamento.ui'
#
# Created: Thu Oct 16 15:32:18 2014
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

class Ui_vtnAltaMedicamento(object):
    def setupUi(self, vtnAltaMedicamento):
        vtnAltaMedicamento.setObjectName(_fromUtf8("vtnAltaMedicamento"))
        vtnAltaMedicamento.resize(552, 286)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(vtnAltaMedicamento)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAltaMedicamento)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignTop)
        self.lineNomb = QtGui.QLineEdit(vtnAltaMedicamento)
        self.lineNomb.setText(_fromUtf8(""))
        self.lineNomb.setObjectName(_fromUtf8("lineNomb"))
        self.gridLayout.addWidget(self.lineNomb, 1, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 2, 1, 1)
        self.lineCantidad = QtGui.QLineEdit(vtnAltaMedicamento)
        self.lineCantidad.setObjectName(_fromUtf8("lineCantidad"))
        self.gridLayout.addWidget(self.lineCantidad, 3, 2, 1, 1)
        self.label = QtGui.QLabel(vtnAltaMedicamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(vtnAltaMedicamento)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.tablaMonodroga = QtGui.QTableWidget(vtnAltaMedicamento)
        self.tablaMonodroga.setEnabled(True)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setRowCount(0)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(0)
        self.tablaMonodroga.horizontalHeader().setDefaultSectionSize(140)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMonodroga, 2, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaMedicamento)
        vtnAltaMedicamento.setTabOrder(self.lineNomb, self.tablaMonodroga)
        vtnAltaMedicamento.setTabOrder(self.tablaMonodroga, self.lineCantidad)
        vtnAltaMedicamento.setTabOrder(self.lineCantidad, self.buttonBox)

    def retranslateUi(self, vtnAltaMedicamento):
        vtnAltaMedicamento.setWindowTitle(_translate("vtnAltaMedicamento", "Alta Medicamento", None))
        self.label_4.setText(_translate("vtnAltaMedicamento", "Nombre", None))
        self.label_2.setText(_translate("vtnAltaMedicamento", "Monodroga", None))
        self.lineNomb.setStatusTip(_translate("vtnAltaMedicamento", "Ingrese nombre del medicamento (solo letrasy númros)", None))
        self.lineNomb.setAccessibleDescription(_translate("vtnAltaMedicamento", "textoNumeros", None))
        self.lineCantidad.setStatusTip(_translate("vtnAltaMedicamento", "Ingrese cantidad de la monodroga (solo números)", None))
        self.lineCantidad.setAccessibleDescription(_translate("vtnAltaMedicamento", "numeros", None))
        self.label.setText(_translate("vtnAltaMedicamento", "Medicamento", None))
        self.label_3.setText(_translate("vtnAltaMedicamento", "Cantidad", None))
        self.tablaMonodroga.setSortingEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaMedicamento = QtGui.QWidget()
    ui = Ui_vtnAltaMedicamento()
    ui.setupUi(vtnAltaMedicamento)
    vtnAltaMedicamento.show()
    sys.exit(app.exec_())

