# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarMedicamento.ui'
#
# Created: Thu Oct 16 15:32:19 2014
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
        vtnModificarMedicamento.resize(646, 360)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnModificarMedicamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.btnBuscarMon = QtGui.QPushButton(vtnModificarMedicamento)
        self.btnBuscarMon.setObjectName(_fromUtf8("btnBuscarMon"))
        self.gridLayout.addWidget(self.btnBuscarMon, 4, 4, 1, 1)
        self.lineNombMed = QtGui.QLineEdit(vtnModificarMedicamento)
        self.lineNombMed.setObjectName(_fromUtf8("lineNombMed"))
        self.gridLayout.addWidget(self.lineNombMed, 1, 2, 1, 2)
        self.btnBuscarMed = QtGui.QPushButton(vtnModificarMedicamento)
        self.btnBuscarMed.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscarMed.setObjectName(_fromUtf8("btnBuscarMed"))
        self.gridLayout.addWidget(self.btnBuscarMed, 1, 4, 1, 1)
        self.lineCantidad = QtGui.QLineEdit(vtnModificarMedicamento)
        self.lineCantidad.setObjectName(_fromUtf8("lineCantidad"))
        self.gridLayout.addWidget(self.lineCantidad, 6, 2, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 6, 1, 1, 1)
        self.lineNombMon = QtGui.QLineEdit(vtnModificarMedicamento)
        self.lineNombMon.setObjectName(_fromUtf8("lineNombMon"))
        self.gridLayout.addWidget(self.lineNombMon, 4, 2, 1, 2)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 7, 3, 1, 2)
        self.tablaMedicamento = QtGui.QTableWidget(vtnModificarMedicamento)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMedicamento, 2, 1, 1, 4)
        self.label_3 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(vtnModificarMedicamento)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        self.tablaMonodroga = QtGui.QTableWidget(vtnModificarMedicamento)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(0)
        self.tablaMonodroga.setRowCount(0)
        self.tablaMonodroga.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMonodroga, 5, 1, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarMedicamento)
        vtnModificarMedicamento.setTabOrder(self.lineNombMed, self.btnBuscarMed)
        vtnModificarMedicamento.setTabOrder(self.btnBuscarMed, self.tablaMedicamento)
        vtnModificarMedicamento.setTabOrder(self.tablaMedicamento, self.lineNombMon)
        vtnModificarMedicamento.setTabOrder(self.lineNombMon, self.btnBuscarMon)
        vtnModificarMedicamento.setTabOrder(self.btnBuscarMon, self.tablaMonodroga)
        vtnModificarMedicamento.setTabOrder(self.tablaMonodroga, self.lineCantidad)
        vtnModificarMedicamento.setTabOrder(self.lineCantidad, self.buttonBox)

    def retranslateUi(self, vtnModificarMedicamento):
        vtnModificarMedicamento.setWindowTitle(_translate("vtnModificarMedicamento", "Modificar Medicamento", None))
        self.label.setText(_translate("vtnModificarMedicamento", "Nombre", None))
        self.label_4.setText(_translate("vtnModificarMedicamento", "Medicamento", None))
        self.btnBuscarMon.setText(_translate("vtnModificarMedicamento", "Buscar", None))
        self.lineNombMed.setStatusTip(_translate("vtnModificarMedicamento", "Ingrese el nombre del Medicamento (solo letras y números)", None))
        self.lineNombMed.setAccessibleDescription(_translate("vtnModificarMedicamento", "textoNumeros", None))
        self.btnBuscarMed.setText(_translate("vtnModificarMedicamento", "Buscar", None))
        self.lineCantidad.setStatusTip(_translate("vtnModificarMedicamento", "Ingrese cantidad de la Monodroga (solo números)", None))
        self.lineCantidad.setAccessibleDescription(_translate("vtnModificarMedicamento", "numeros", None))
        self.label_2.setText(_translate("vtnModificarMedicamento", "* Cantidad de Monodroga", None))
        self.lineNombMon.setStatusTip(_translate("vtnModificarMedicamento", "Ingrese nombre de la Monodroga (solo letras)", None))
        self.lineNombMon.setAccessibleDescription(_translate("vtnModificarMedicamento", "texto", None))
        self.label_3.setText(_translate("vtnModificarMedicamento", "Monodroga", None))
        self.label_5.setText(_translate("vtnModificarMedicamento", "* Nombre", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarMedicamento = QtGui.QWidget()
    ui = Ui_vtnModificarMedicamento()
    ui.setupUi(vtnModificarMedicamento)
    vtnModificarMedicamento.show()
    sys.exit(app.exec_())

