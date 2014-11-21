# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnBajaMedicamento.ui'
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

class Ui_vtnBajaMedicamento(object):
    def setupUi(self, vtnBajaMedicamento):
        vtnBajaMedicamento.setObjectName(_fromUtf8("vtnBajaMedicamento"))
        vtnBajaMedicamento.resize(579, 307)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaMedicamento)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaMedicamento)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnBajaMedicamento)
        self.btnBuscar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 3, 1, 1)
        self.tablaMedicamento = QtGui.QTableWidget(vtnBajaMedicamento)
        self.tablaMedicamento.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMedicamento.setObjectName(_fromUtf8("tablaMedicamento"))
        self.tablaMedicamento.setColumnCount(0)
        self.tablaMedicamento.setRowCount(0)
        self.tablaMedicamento.horizontalHeader().setDefaultSectionSize(160)
        self.tablaMedicamento.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMedicamento, 1, 0, 1, 4)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaMedicamento)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 2, 1, 2)
        self.lineNomb = QtGui.QLineEdit(vtnBajaMedicamento)
        self.lineNomb.setObjectName(_fromUtf8("lineNomb"))
        self.gridLayout.addWidget(self.lineNomb, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaMedicamento)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaMedicamento)
        vtnBajaMedicamento.setTabOrder(self.lineNomb, self.btnBuscar)
        vtnBajaMedicamento.setTabOrder(self.btnBuscar, self.tablaMedicamento)
        vtnBajaMedicamento.setTabOrder(self.tablaMedicamento, self.buttonBox)

    def retranslateUi(self, vtnBajaMedicamento):
        vtnBajaMedicamento.setWindowTitle(_translate("vtnBajaMedicamento", "Baja Medicamento", None))
        self.label.setText(_translate("vtnBajaMedicamento", "Nombre", None))
        self.btnBuscar.setText(_translate("vtnBajaMedicamento", "Buscar", None))
        self.lineNomb.setStatusTip(_translate("vtnBajaMedicamento", "Ingrese nombre del Medicamento (solo letras y números)", None))
        self.lineNomb.setAccessibleDescription(_translate("vtnBajaMedicamento", "textoNumeros", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaMedicamento = QtGui.QWidget()
    ui = Ui_vtnBajaMedicamento()
    ui.setupUi(vtnBajaMedicamento)
    vtnBajaMedicamento.show()
    sys.exit(app.exec_())

