# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'altaMonodroga.ui'
#
# Created: Wed Sep 24 13:59:38 2014
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
        self.label = QtGui.QLabel(vtnAltaMonodroga)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.checkBox = QtGui.QCheckBox(vtnAltaMonodroga)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.gridLayout.addWidget(self.checkBox, 1, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(vtnAltaMonodroga)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.textEdit = QtGui.QTextEdit(vtnAltaMonodroga)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout.addWidget(self.textEdit, 3, 1, 1, 1)
        self.label_2 = QtGui.QLabel(vtnAltaMonodroga)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1, QtCore.Qt.AlignTop)
        self.checkBox_2 = QtGui.QCheckBox(vtnAltaMonodroga)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.gridLayout.addWidget(self.checkBox_2, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(vtnAltaMonodroga)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(vtnAltaMonodroga)
        QtCore.QMetaObject.connectSlotsByName(vtnAltaMonodroga)
        vtnAltaMonodroga.setTabOrder(self.lineEdit, self.checkBox)
        vtnAltaMonodroga.setTabOrder(self.checkBox, self.checkBox_2)
        vtnAltaMonodroga.setTabOrder(self.checkBox_2, self.textEdit)
        vtnAltaMonodroga.setTabOrder(self.textEdit, self.buttonBox)

    def retranslateUi(self, vtnAltaMonodroga):
        vtnAltaMonodroga.setWindowTitle(_translate("vtnAltaMonodroga", "Alta Monodroga", None))
        self.label.setText(_translate("vtnAltaMonodroga", "Nombre", None))
        self.checkBox.setText(_translate("vtnAltaMonodroga", "Receta Archivada?", None))
        self.label_2.setText(_translate("vtnAltaMonodroga", "Descripción", None))
        self.checkBox_2.setText(_translate("vtnAltaMonodroga", "Receta?", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnAltaMonodroga = QtGui.QWidget()
    ui = Ui_vtnAltaMonodroga()
    ui.setupUi(vtnAltaMonodroga)
    vtnAltaMonodroga.show()
    sys.exit(app.exec_())

