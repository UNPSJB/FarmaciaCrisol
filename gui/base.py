__author__ = 'waldo'
# coding: latin-1
from PyQt4 import QtGui
import re
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
        if hasattr(self, "buttonBox"):
            self.buttonBox.rejected.connect(self.mdi().hide)
            self.buttonBox.accepted.connect(self.confirmarOperacion)

    def showMsjEstado(self, msj):
        self.mdi().window().setBarraEstado(msj)

    def mdi(self):
        return self.parent()

    def confirmarOperacion(self):
        pass

    def cargarObjetos(self, tabla, queryset, atributos):
        for n, obj in enumerate(queryset):
            tabla.insertRow(n)
            for m, campo in enumerate(atributos):
                tabla.setItem(n, m, QtGui.QTableWidgetItem("%s" % getattr(obj, campo)))


    def cargarTabla(self, tabla, items, columnHeaders):
        tabla.setColumnCount(len(columnHeaders))
        tabla.setHorizontalHeaderLabels(columnHeaders)
        n = 0
        for key in items:
            m = 0
            tabla.insertRow(n)
            for item in items[key]:
                newitem = QtGui.QTableWidgetItem(str(item))
                tabla.setItem(n, m, newitem)
                m += 1
            n += 1

    def limpiarTabla(self, tabla, columnHeaders):
        tabla.clear()
        tabla.setRowCount(0)
        tabla.setHorizontalHeaderLabels(columnHeaders)

    def itemSeleccionado(self, tabla):
        return str(tabla.item(tabla.currentItem().row(), 0).text())

    def actualizarVentana(self):
        pass