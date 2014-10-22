# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bajaPresentacion.ui'
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

class Ui_vtnBajaPresentacion(object):
    def setupUi(self, vtnBajaPresentacion):
        vtnBajaPresentacion.setObjectName(_fromUtf8("vtnBajaPresentacion"))
        vtnBajaPresentacion.resize(526, 229)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaPresentacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaPresentacion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineTipo = QtGui.QLineEdit(vtnBajaPresentacion)
        self.lineTipo.setObjectName(_fromUtf8("lineTipo"))
        self.gridLayout.addWidget(self.lineTipo, 0, 1, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnBajaPresentacion)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaPresentacion)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.tablaPresentacion = QtGui.QTableWidget(vtnBajaPresentacion)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.tablaPresentacion.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tablaPresentacion, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaPresentacion)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaPresentacion)
        vtnBajaPresentacion.setTabOrder(self.lineTipo, self.btnBuscar)
        vtnBajaPresentacion.setTabOrder(self.btnBuscar, self.tablaPresentacion)
        vtnBajaPresentacion.setTabOrder(self.tablaPresentacion, self.buttonBox)

    def retranslateUi(self, vtnBajaPresentacion):
        vtnBajaPresentacion.setWindowTitle(_translate("vtnBajaPresentacion", "Baja Presentación", None))
        self.label.setText(_translate("vtnBajaPresentacion", "Tipo", None))
        self.lineTipo.setStatusTip(_translate("vtnBajaPresentacion", "Ingrese tipo de la presentación (solo letras)", None))
        self.lineTipo.setAccessibleDescription(_translate("vtnBajaPresentacion", "texto", None))
        self.btnBuscar.setText(_translate("vtnBajaPresentacion", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaPresentacion = QtGui.QWidget()
    ui = Ui_vtnBajaPresentacion()
    ui.setupUi(vtnBajaPresentacion)
    vtnBajaPresentacion.show()
    sys.exit(app.exec_())

