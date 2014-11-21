# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnBajaMonodroga.ui'
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

class Ui_vtnBajaMonodroga(object):
    def setupUi(self, vtnBajaMonodroga):
        vtnBajaMonodroga.setObjectName(_fromUtf8("vtnBajaMonodroga"))
        vtnBajaMonodroga.resize(553, 291)
        self.verticalLayout = QtGui.QVBoxLayout(vtnBajaMonodroga)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnBajaMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineNomb = QtGui.QLineEdit(vtnBajaMonodroga)
        self.lineNomb.setObjectName(_fromUtf8("lineNomb"))
        self.gridLayout.addWidget(self.lineNomb, 0, 1, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnBajaMonodroga)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 2, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnBajaMonodroga)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 2)
        self.tablaMonodroga = QtGui.QTableWidget(vtnBajaMonodroga)
        self.tablaMonodroga.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaMonodroga.setTabKeyNavigation(True)
        self.tablaMonodroga.setObjectName(_fromUtf8("tablaMonodroga"))
        self.tablaMonodroga.setColumnCount(0)
        self.tablaMonodroga.setRowCount(0)
        self.tablaMonodroga.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaMonodroga, 1, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnBajaMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnBajaMonodroga)
        vtnBajaMonodroga.setTabOrder(self.lineNomb, self.btnBuscar)
        vtnBajaMonodroga.setTabOrder(self.btnBuscar, self.tablaMonodroga)
        vtnBajaMonodroga.setTabOrder(self.tablaMonodroga, self.buttonBox)

    def retranslateUi(self, vtnBajaMonodroga):
        vtnBajaMonodroga.setWindowTitle(_translate("vtnBajaMonodroga", "Baja Monodroga", None))
        self.label.setText(_translate("vtnBajaMonodroga", "Nombre", None))
        self.lineNomb.setStatusTip(_translate("vtnBajaMonodroga", "Ingrese el nombre de la Monodroga (solo letras)", None))
        self.lineNomb.setAccessibleDescription(_translate("vtnBajaMonodroga", "palabra", None))
        self.btnBuscar.setText(_translate("vtnBajaMonodroga", "Buscar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnBajaMonodroga = QtGui.QWidget()
    ui = Ui_vtnBajaMonodroga()
    ui.setupUi(vtnBajaMonodroga)
    vtnBajaMonodroga.show()
    sys.exit(app.exec_())

