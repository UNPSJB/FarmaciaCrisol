__author__ = 'waldo'
# coding: latin-1
from PyQt4 import QtGui
from validarDatos import ValidarDatos
class MyMdi(QtGui.QMdiSubWindow):
    def __init__(self, mainWindow):
        super(MyMdi, self).__init__(mainWindow)
        self.mainWindow = mainWindow

    def closeEvent(self, event):
        self.hide()
        #super(MyMdi, self).closeEvent(event)

    def window(self):
        return self.mainWindow

    def show(self):
        super(MyMdi, self).show()
        self.setFocus()
        if self.isMinimized():
            self.showNormal()

class MdiWidget(QtGui.QWidget):
    def __init__(self, mdi):
        QtGui.QWidget.__init__(self, mdi)
        self.setupUi(self)


    def validadores(self, model):
        ##Esta parte analiza los campos requeridos para el cliente
        self.camposRequeridos = [getattr(self, "line%s" % campo.title()) for campo in model.requeridos]
        ValidarDatos.setValidador(self.camposRequeridos)
        ##Esta parte analiza los campos que son opcionales
        camposNoRequeridos=[getattr(self, "line%s" % campo.title()) for campo in model.noRequeridos]
        ValidarDatos.setValidador(camposNoRequeridos)

    def showMsjEstado(self, msj):
        self.mdi().window().setBarraEstado(msj)

    def mdi(self):
        return self.parent()

    def cargarObjetos(self, tabla, queryset, atributos):
        for n, obj in enumerate(queryset):
            tabla.insertRow(n)
            for m, campo in enumerate(atributos):
                tabla.setItem(n, m, QtGui.QTableWidgetItem("%s" % getattr(obj, campo)))

    def confirmarOperacion(self):
        pass

    def limpiarTabla(self, tabla):
        tabla.clear()
        tabla.setRowCount(0)

    def itemSeleccionado(self, tabla):
        return str(tabla.item(tabla.currentItem().row(), 0).text())

    def actualizarVentana(self):
        pass