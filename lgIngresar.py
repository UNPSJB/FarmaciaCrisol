__author__ = 'waldo'
# coding: latin-1
from PyQt4 import QtGui
from ventanas import Ui_vtnIngresar
from gui import MdiWidget

class Ingresar(MdiWidget, Ui_vtnIngresar):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.buttonBox.accepted.connect(self.validarUsuario)
        self.txtUsuario.returnPressed.connect(self.validarUsuario)
        self.txtContrasenia.returnPressed.connect(self.validarUsuario)

    def validarUsuario(self):
        if ((self.txtUsuario.text() == 'far' and self.txtContrasenia.text() == 'far')or
                (self.txtUsuario.text() == 'adm' and self.txtContrasenia.text() == 'adm')or
                (self.txtUsuario.text() == 'tec' and self.txtContrasenia.text() == 'tec')):
            self.mdi().hide()
            self.habilitarPermisos(self.txtUsuario.text())
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Usuario o Contraseña incorrecta.')

    def habilitarPermisos(self, usuario):
        self.mdi().window().deshabilitarMenu()
        if usuario == "far":
            hab_vtn = self.mdi().window().farmaceutico
        elif usuario == "adm":
            hab_vtn = self.mdi().window().administrador
        else:
            hab_vtn = self.mdi().window().tecnico_farmaceutico
        for hab in hab_vtn:
            if isinstance(hab, QtGui.QMenu):
                hab.menuAction().setVisible(True)
            else:
                hab.setVisible(True)
