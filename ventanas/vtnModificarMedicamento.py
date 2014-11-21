# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnModificarMedicamento.ui'
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

class Ui_vtnModificarMedicamento(object):
    def setupUi(self, vtnModificarMedicamento):
        vtnModificarMedicamento.setObjectName(_fromUtf8("vtnModificarMedicamento"))
        vtnModificarMedicamento.resize(646, 388)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gbMedicamento = QtGui.QGroupBox(vtnModificarMedicamento)
        self.gbMedicamento.setObjectName(_fromUtf8("gbMedicamento"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.gbMedicamento)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.gbMedicamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.btnBuscarMed = QtGui.QPushButton(self.gbMedicamento)
        self.btnBuscarMed.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarMed.setObjectName(_fromUtf8("btnBuscarMed"))
        self.gridLayout_2.addWidget(self.btnBuscarMed, 0, 2, 1, 1)
        self.lineNombMed = QtGui.QLineEdit(self.gbMedicamento)
        self.lineNombMed.setObjectName(_fromUtf8("lineNombMed"))
        self.gridLayout_2.addWidget(self.lineNombMed, 0, 1, 1, 1)
        self.tablaMedicamento = QtGui.QTableWidget(self.gbMedicamento)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tablaMedicamento, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.gbMedicamento)
        self.gbMonodroga = QtGui.QGroupBox(vtnModificarMedicamento)
        self.gbMonodroga.setObjectName(_fromUtf8("gbMonodroga"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.gbMonodroga)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.gbMonodroga)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineNombMon = QtGui.QLineEdit(self.gbMonodroga)
        self.lineNombMon.setObjectName(_fromUtf8("lineNombMon"))
        self.gridLayout_3.addWidget(self.lineNombMon, 0, 1, 1, 1)
        self.btnBuscarMon = QtGui.QPushButton(self.gbMonodroga)
        self.btnBuscarMon.setObjectName(_fromUtf8("btnBuscarMon"))
        self.gridLayout_3.addWidget(self.btnBuscarMon, 0, 2, 1, 1)
        self.tablaMonodroga = QtGui.QTableWidget(self.gbMonodroga)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(0)
        self.tablaMonodroga.setRowCount(0)
        self.tablaMonodroga.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.tablaMonodroga, 1, 0, 1, 3)
        self.label_2 = QtGui.QLabel(self.gbMonodroga)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineCantidad = QtGui.QLineEdit(self.gbMonodroga)
        self.lineCantidad.setObjectName(_fromUtf8("lineCantidad"))
        self.gridLayout_3.addWidget(self.lineCantidad, 2, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.verticalLayout.addWidget(self.gbMonodroga)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(vtnModificarMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarMedicamento)

    def retranslateUi(self, vtnModificarMedicamento):
        vtnModificarMedicamento.setWindowTitle(_translate("vtnModificarMedicamento", "Modificar Medicamento", None))
        self.gbMedicamento.setTitle(_translate("vtnModificarMedicamento", "Medicamento", None))
        self.label.setText(_translate("vtnModificarMedicamento", "Nombre", None))
        self.btnBuscarMed.setText(_translate("vtnModificarMedicamento", "Buscar", None))
        self.lineNombMed.setStatusTip(_translate("vtnModificarMedicamento", "Ingrese el nombre del Medicamento (solo letras y números)", None))
        self.lineNombMed.setAccessibleDescription(_translate("vtnModificarMedicamento", "textoNumeros", None))
        self.gbMonodroga.setTitle(_translate("vtnModificarMedicamento", "Monodroga", None))
        self.label_5.setText(_translate("vtnModificarMedicamento", "* Nombre", None))
        self.lineNombMon.setStatusTip(_translate("vtnModificarMedicamento", "Ingrese nombre de la Monodroga (solo letras)", None))
        self.lineNombMon.setAccessibleDescription(_translate("vtnModificarMedicamento", "texto", None))
        self.btnBuscarMon.setText(_translate("vtnModificarMedicamento", "Buscar", None))
        self.label_2.setText(_translate("vtnModificarMedicamento", "* Cantidad", None))
        self.lineCantidad.setStatusTip(_translate("vtnModificarMedicamento", "Ingrese cantidad de la Monodroga (solo números)", None))
        self.lineCantidad.setAccessibleDescription(_translate("vtnModificarMedicamento", "cantidad", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarMedicamento = QtGui.QWidget()
    ui = Ui_vtnModificarMedicamento()
    ui.setupUi(vtnModificarMedicamento)
    vtnModificarMedicamento.show()
    sys.exit(app.exec_())

