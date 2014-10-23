__author__ = 'waldo'
# coding: latin-1
from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtCore import QRegExp
class ValidarDatos():
    def setValidator(self, campos):
        for campo in campos:
            if campo.accessibleDescription() == "palabra":
                regexp = QRegExp("[a-zA-Zéáúóíñ]+")
            elif campo.accessibleDescription() == "texto":
                regexp = QRegExp("[a-zA-Zéáúóíñ]+[a-zA-Zéáúóíñ ]*")
            elif campo.accessibleDescription() == "numeros":
                regexp = QRegExp("[1-9]\d{1,4}")
            elif campo.accessibleDescription() == "textoNumeros":
                regexp = QRegExp("[a-zA-Zéáúóíñ0-9]+[a-zA-Zéáúóíñ0-9 ]*")
            elif campo.accessibleDescription() == "codigo":
                regexp = QRegExp("\d{9}")
            elif campo.accessibleDescription() == "importe":
                regexp = QRegExp("[1-9]\d*\.\d{2}")
            validator = QRegExpValidator(regexp)
            campo.setValidator(validator)

    def validarCamposVacios(self, campos):
        for campo in campos:
            if campo.text() == "":
                return False
        return True