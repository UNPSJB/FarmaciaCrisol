# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificarPresentacion.ui'
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

class Ui_vtnModificarPresentacion(object):
    def setupUi(self, vtnModificarPresentacion):
        vtnModificarPresentacion.setObjectName(_fromUtf8("vtnModificarPresentacion"))
        vtnModificarPresentacion.resize(638, 374)
        self.verticalLayout = QtGui.QVBoxLayout(vtnModificarPresentacion)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(vtnModificarPresentacion)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.btnBuscar = QtGui.QPushButton(vtnModificarPresentacion)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.gridLayout.addWidget(self.btnBuscar, 0, 2, 1, 1)
        self.lineUnidadMedida = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineUnidadMedida.setObjectName(_fromUtf8("lineUnidadMedida"))
        self.gridLayout.addWidget(self.lineUnidadMedida, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(vtnModificarPresentacion)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.tablaPresentacion = QtGui.QTableWidget(vtnModificarPresentacion)
        self.tablaPresentacion.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresentacion.setObjectName(_fromUtf8("tablaPresentacion"))
        self.tablaPresentacion.setColumnCount(0)
        self.tablaPresentacion.setRowCount(0)
        self.tablaPresentacion.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresentacion.horizontalHeader().setStretchLastSection(True)
        self.tablaPresentacion.verticalHeader().setVisible(True)
        self.gridLayout.addWidget(self.tablaPresentacion, 1, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(vtnModificarPresentacion)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 2)
        self.lineTipo = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineTipo.setObjectName(_fromUtf8("lineTipo"))
        self.gridLayout.addWidget(self.lineTipo, 0, 1, 1, 1)
        self.lineCantFracc = QtGui.QLineEdit(vtnModificarPresentacion)
        self.lineCantFracc.setObjectName(_fromUtf8("lineCantFracc"))
        self.gridLayout.addWidget(self.lineCantFracc, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(vtnModificarPresentacion)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(vtnModificarPresentacion)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1, QtCore.Qt.AlignTop)
        self.tablaPresFracc = QtGui.QTableWidget(vtnModificarPresentacion)
        self.tablaPresFracc.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tablaPresFracc.setObjectName(_fromUtf8("tablaPresFracc"))
        self.tablaPresFracc.setColumnCount(0)
        self.tablaPresFracc.setRowCount(0)
        self.tablaPresFracc.horizontalHeader().setDefaultSectionSize(160)
        self.tablaPresFracc.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tablaPresFracc, 4, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnModificarPresentacion)
        QtCore.QMetaObject.connectSlotsByName(vtnModificarPresentacion)
        vtnModificarPresentacion.setTabOrder(self.lineTipo, self.btnBuscar)
        vtnModificarPresentacion.setTabOrder(self.btnBuscar, self.tablaPresentacion)
        vtnModificarPresentacion.setTabOrder(self.tablaPresentacion, self.lineUnidadMedida)
        vtnModificarPresentacion.setTabOrder(self.lineUnidadMedida, self.lineCantFracc)
        vtnModificarPresentacion.setTabOrder(self.lineCantFracc, self.buttonBox)

    def retranslateUi(self, vtnModificarPresentacion):
        vtnModificarPresentacion.setWindowTitle(_translate("vtnModificarPresentacion", "Modificar Presentación", None))
        self.label.setText(_translate("vtnModificarPresentacion", "Tipo", None))
        self.btnBuscar.setText(_translate("vtnModificarPresentacion", "Buscar", None))
        self.lineUnidadMedida.setStatusTip(_translate("vtnModificarPresentacion", "Ingrese unidad de medida (solo letras)", None))
        self.lineUnidadMedida.setAccessibleDescription(_translate("vtnModificarPresentacion", "texto", None))
        self.label_4.setText(_translate("vtnModificarPresentacion", "* Cantidad de Fraciones", None))
        self.lineTipo.setStatusTip(_translate("vtnModificarPresentacion", "Ingrese tipo de la Presentación (solo letras)", None))
        self.lineTipo.setAccessibleDescription(_translate("vtnModificarPresentacion", "texto", None))
        self.lineCantFracc.setStatusTip(_translate("vtnModificarPresentacion", "Ingrese cantidad de fracciones (solo números)", None))
        self.lineCantFracc.setAccessibleDescription(_translate("vtnModificarPresentacion", "numeros", None))
        self.label_2.setText(_translate("vtnModificarPresentacion", "* Unidad de Medida", None))
        self.label_3.setText(_translate("vtnModificarPresentacion", "* Fraccionable", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnModificarPresentacion = QtGui.QWidget()
    ui = Ui_vtnModificarPresentacion()
    ui.setupUi(vtnModificarPresentacion)
    vtnModificarPresentacion.show()
    sys.exit(app.exec_())

