# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaPresentacion.ui'
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

class Ui_vtnAltaPresentacion(object):
    def setupUi(self, vtnAltaPresentacion):
        vtnAltaPresentacion.setObjectName(_fromUtf8("vtnAltaPresentacion"))
        vtnAltaPresentacion.resize(535, 263)
        self.verticalLayout = QtGui.QVBoxLayout(vtnAltaPresentacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineCantFracc = QtGui.QLineEdit(vtnAltaPresentacion)
        self.lineCantFracc.setObjectName(_fromUtf8("lineCantFracc"))
        self.gridLayout.addWidget(self.lineCantFracc, 2, 1, 1, 1)
        self.label = QtGui.QLabel(vtnAltaPresentacion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineUnidadMedida = QtGui.QLineEdit(vtnAltaPresentacion)
        self.lineUnidadMedida.setObjectName(_fromUtf8("lineUnidadMedida"))
        self.gridLayout.addWidget(self.lineUnidadMedida, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(vtnAltaPresentacion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QtGui.QLabel(vtnAltaPresentacion)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1, QtCore.Qt.AlignTop)
        self.label_2 = QtGui.QLabel(vtnAltaPresentacion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineTipo = QtGui.QLineEdit(vtnAltaPresentacion)
        self.lineTipo.setObjectName(_fromUtf8("lineTipo"))
        self.gridLayout.addWidget(self.lineTipo, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaPresentacion)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.tablaPresentacion = QtGui.QTableWidget(vtnAltaPresentacion)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setCascadingSectionResizes(False)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaPresentacion, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaPresentacion)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaPresentacion)
        vtnAltaPresentacion.setTabOrder(self.lineTipo, self.lineUnidadMedida)
        vtnAltaPresentacion.setTabOrder(self.lineUnidadMedida, self.lineCantFracc)
        vtnAltaPresentacion.setTabOrder(self.lineCantFracc, self.buttonBox)

    def retranslateUi(self, vtnAltaPresentacion):
        vtnAltaPresentacion.setWindowTitle(_translate("vtnAltaPresentacion", "Alta Presentación", None))
        self.lineCantFracc.setStatusTip(_translate("vtnAltaPresentacion", "Ingrese cantidad de fracciones (solo números)", None))
        self.lineCantFracc.setAccessibleDescription(_translate("vtnAltaPresentacion", "numeros", None))
        self.label.setText(_translate("vtnAltaPresentacion", "Tipo", None))
        self.lineUnidadMedida.setStatusTip(_translate("vtnAltaPresentacion", "Ingrese unidad de medida (solo letras)", None))
        self.lineUnidadMedida.setAccessibleDescription(_translate("vtnAltaPresentacion", "texto", None))
        self.label_3.setText(_translate("vtnAltaPresentacion", "Cantidad de Fracciones", None))
        self.label_4.setText(_translate("vtnAltaPresentacion", "Fraccionable", None))
        self.label_2.setText(_translate("vtnAltaPresentacion", "Unidad de Medida", None))
        self.lineTipo.setStatusTip(_translate("vtnAltaPresentacion", "Ingrese el tipo de Presentación (solo letras)", None))
        self.lineTipo.setAccessibleDescription(_translate("vtnAltaPresentacion", "texto", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaPresentacion = QtGui.QWidget()
    ui = Ui_vtnAltaPresentacion()
    ui.setupUi(vtnAltaPresentacion)
    vtnAltaPresentacion.show()
    sys.exit(app.exec_())

