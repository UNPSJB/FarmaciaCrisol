# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnAltaMedicamento.ui'
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

class Ui_vtnAltaMedicamento(object):
    def setupUi(self, vtnAltaMedicamento):
        vtnAltaMedicamento.setObjectName(_fromUtf8("vtnAltaMedicamento"))
        vtnAltaMedicamento.resize(552, 304)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbMedicamento = QtGui.QGroupBox(vtnAltaMedicamento)
        self.gbMedicamento.setObjectName(_fromUtf8("gbMedicamento"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbMedicamento)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.gbMedicamento)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineNomb = QtGui.QLineEdit(self.gbMedicamento)
        self.lineNomb.setText(_fromUtf8(""))
        self.lineNomb.setObjectName(_fromUtf8("lineNomb"))
        self.gridLayout_2.addWidget(self.lineNomb, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbMedicamento)
        self.gbMonodroga = QtGui.QGroupBox(vtnAltaMedicamento)
        self.gbMonodroga.setObjectName(_fromUtf8("gbMonodroga"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbMonodroga)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tablaMonodroga = QtGui.QTableWidget(self.gbMonodroga)
        self.tablaMonodroga.setEnabled(True)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setRowCount(0)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(0)
        self.tablaMonodroga.horizontalHeader().setDefaultSectionSize(140)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tablaMonodroga, 0, 0, 1, 2)
        self.lineCantidad = QtGui.QLineEdit(self.gbMonodroga)
        self.lineCantidad.setObjectName(_fromUtf8("lineCantidad"))
        self.gridLayout_3.addWidget(self.lineCantidad, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gbMonodroga)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)
        self.btnActMon = QtGui.QPushButton(self.gbMonodroga)
        self.btnActMon.setObjectName(_fromUtf8("btnActMon"))
        self.gridLayout_3.addWidget(self.btnActMon, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbMonodroga)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnAltaMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaMedicamento)
        vtnAltaMedicamento.setTabOrder(self.lineNomb, self.tablaMonodroga)
        vtnAltaMedicamento.setTabOrder(self.tablaMonodroga, self.btnActMon)
        vtnAltaMedicamento.setTabOrder(self.btnActMon, self.lineCantidad)
        vtnAltaMedicamento.setTabOrder(self.lineCantidad, self.buttonBox)

    def retranslateUi(self, vtnAltaMedicamento):
        vtnAltaMedicamento.setWindowTitle(_translate("vtnAltaMedicamento", "Alta Medicamento", None))
        self.gbMedicamento.setTitle(_translate("vtnAltaMedicamento", "Medicamento", None))
        self.label_4.setText(_translate("vtnAltaMedicamento", "Nombre", None))
        self.lineNomb.setStatusTip(_translate("vtnAltaMedicamento", "Ingrese nombre del medicamento (solo letrasy númros)", None))
        self.lineNomb.setAccessibleDescription(_translate("vtnAltaMedicamento", "textoNumeros", None))
        self.gbMonodroga.setTitle(_translate("vtnAltaMedicamento", "Monodroga", None))
        self.tablaMonodroga.setSortingEnabled(False)
        self.lineCantidad.setStatusTip(_translate("vtnAltaMedicamento", "Ingrese cantidad de la monodroga (solo números)", None))
        self.lineCantidad.setAccessibleDescription(_translate("vtnAltaMedicamento", "cantidad", None))
        self.label_3.setText(_translate("vtnAltaMedicamento", "Cantidad", None))
        self.btnActMon.setText(_translate("vtnAltaMedicamento", "Actualizar Monodrogas", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaMedicamento = QtGui.QWidget()
    ui = Ui_vtnAltaMedicamento()
    ui.setupUi(vtnAltaMedicamento)
    vtnAltaMedicamento.show()
    sys.exit(app.exec_())

