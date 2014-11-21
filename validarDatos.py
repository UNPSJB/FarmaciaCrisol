__author__ = 'waldo'
# coding: latin-1
from PyQt4.QtGui import QRegExpValidator
from PyQt4.QtCore import QRegExp
class ValidarDatos():

    @classmethod
    def setValidador(cls, campos):
        for campo in campos:
            c = campo.accessibleDescription()
            if c == "palabra":
                regexp = QRegExp("[a-zA-Zéáúóíñ]+")
            elif c == "texto":
                regexp = QRegExp("[a-zA-Zéáúóíñ]+[a-zA-Zéáúóíñ ]*")
            elif c == "numeros":
                regexp = QRegExp("[1-9]\d{1,4}")
            elif c == "textoNumeros":
                regexp = QRegExp("[a-zA-Zéáúóíñ0-9]+[a-zA-Zéáúóíñ0-9 ]*")
            elif c == "codigo":
                regexp = QRegExp("\d{9}")
            elif c == "importe":
                regexp = QRegExp("[1-9]\d*\.\d{2}")
            elif c == "lote":
                regexp = QRegExp("[0-9A-Za-z]{2,10}")
            elif c == "cantidad":
                regexp = QRegExp("[1-9]\d{1,6}")
            #TODO Agregue el codigo de validacion para los campos de clientes
            elif c=="dni":
                regexp=QRegExp("\d{8}")
            elif c=="telefono":
                regexp=QRegExp("\d{0,20}")
            elif c=="direccion":
                regexp=QRegExp(".+\d{0,5}")
            elif c=="nya":
                regexp=QRegExp("[a-zA-Zéáúóíñ]+(\s[a-zA-Zéáúóíñ]+)")

            # TODO : que pasa si no tiene nada?
            validator = QRegExpValidator(regexp)
            campo.setValidator(validator)

    def validarCamposVacios(self, campos):
        for campo in campos:
            if campo.text() == "":
                return False
        return True