__author__ = 'waldo'
 # coding: latin-1
import sys
import re
from PyQt4 import QtCore, QtGui
from ventanaPrincipal import Ui_vtnPrincipal
from altaCliente import Ui_vtnAltaCliente
from bajaCliente import Ui_vtnBajaCliente
from modificarCliente import Ui_vtnModificarCliente
from altaMedicamento import Ui_vtnAltaMedicamento
from bajaMedicamento import Ui_vtnBajaMedicamento
from modificarMedicamento import Ui_vtnModificarMedicamento
from altaMonodroga import Ui_vtnAltaMonodroga
from bajaMonodroga import Ui_vtnBajaMonodroga
from modificarMonodroga import Ui_vtnModificarMonodroga
from altaProducto import Ui_vtnAltaProducto
from bajaProducto import Ui_vtnBajaProducto
from modificarProducto import Ui_vtnModificarProducto
from altaPresentacion import Ui_vtnAltaPresentacion
from bajaPresentacion import Ui_vtnBajaPresentacion
from modificarPresentacion import Ui_vtnModificarPresentacion
from bajaLote import Ui_vtnBajaLote
from modificarLote import Ui_vtnModificarLote
from bajaRemito import Ui_vtnBajaRemito
from modificarRemito import Ui_vtnModificarRemito
from devolucionDeCliente import Ui_vtnDevolucionDeCliente
from fraccionarProducto import Ui_vtnFraccionarProducto
from ingresar import Ui_vtnIngresar
from listar import Ui_vtnListar
from registrarCobroRemito import Ui_vtnRegistrarCobroRemito
from reintegroCliente import Ui_vtnReintegroCliente
from ventaContado import Ui_vtnVentaContado
from ventaConRemito import Ui_vtnVentaConRemito
from ajusteNegativoStock import Ui_vtnAjusteNegativoStock

class MyMdi(QtGui.QMdiSubWindow):
    def closeEvent(self, event):
        self.hide()
        #self.reset()
        #super(MyMdi, self).closeEvent(event)

    def window(self):
        return self.parent()

class MdiWidget(QtGui.QWidget):
    def __init__(self, mdi):
        QtGui.QWidget.__init__(self, mdi)
        self.setupUi(self)
        if hasattr(self, "buttonBox"):
            self.buttonBox.rejected.connect(self.mdi().hide)
            self.buttonBox.accepted.connect(self.showMsjEstado)

    def showMsjEstado(self):
        self.mdi().window().parent().parent().setBarraEstado("El Producto fue dado de alta.")

    def validarDatos(self):
        txt = self.sender().text()
        if(self.sender().accessibleDescription() == "texto"):
            regexp = '^[a-zA-Zéáúóíñ]{3,10} ?[a-zA-Zéáúóíñ]{0,10} ?[a-zA-Zéáúóíñ]{0,10}$'
        elif (self.sender().accessibleDescription() == "codigo"):
            regexp = '^[0-9]{9}$'
        elif (self.sender().accessibleDescription() == "importe"):
            regexp = '^[0-9]+\.[0-9]{2}$'
        if (re.match(regexp, txt)):
            self.sender().setStyleSheet("QLineEdit { background-color : white; }")
        else:
            self.sender().setStyleSheet("QLineEdit { background-color : red; }")
        #validar que los campos obligatorios contengan algo cuando pulsa aceptar
        pass

    def mdi(self):
        return self.parent()

class AltaMedicamento(MdiWidget, Ui_vtnAltaMedicamento):
    pass

class BajaMedicamento(MdiWidget, Ui_vtnBajaMedicamento):
    pass

class ModificarMedicamento(MdiWidget, Ui_vtnModificarMedicamento):
    pass

class AltaMonodroga(MdiWidget, Ui_vtnAltaMonodroga):
    pass

class BajaMonodroga(MdiWidget, Ui_vtnBajaMonodroga):
    pass

class ModificarMonodroga(MdiWidget, Ui_vtnModificarMonodroga):
    pass

class AltaPresentacion(MdiWidget, Ui_vtnAltaPresentacion):
    pass

class BajaPresentacion(MdiWidget, Ui_vtnBajaPresentacion):
    pass

class ModificarPresentacion(MdiWidget, Ui_vtnModificarPresentacion):
    pass

class AltaProducto(MdiWidget, Ui_vtnAltaProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        #---------Coleccion de Campos de texto,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
        camposTxt = [
            (self.txtNomb),
            (self.txtTipo),
            (self.txtCodBarra),
            (self.txtImp)
        ]
        for campo in camposTxt:
            campo.textChanged.connect(self.validarDatos)

class BajaProducto(MdiWidget, Ui_vtnBajaProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.txtCodBarra.textChanged.connect(self.validarDatos)

class ModificarProducto(MdiWidget, Ui_vtnModificarProducto):
    pass

class BajaLote(MdiWidget, Ui_vtnBajaLote):
    pass

class ModificarLote(MdiWidget, Ui_vtnModificarLote):
    pass

class FraccionarProducto(MdiWidget, Ui_vtnFraccionarProducto):
    pass

class AjusteNegativoStock(MdiWidget, Ui_vtnAjusteNegativoStock):
    pass

class BajaRemito(MdiWidget, Ui_vtnBajaRemito):
    pass

class ModificarRemito(MdiWidget, Ui_vtnModificarRemito):
    pass

class DevolucionDeCliente(MdiWidget, Ui_vtnDevolucionDeCliente):
    pass

class Listar(MdiWidget, Ui_vtnListar):
    pass

class RegistrarCobroRemito(MdiWidget, Ui_vtnRegistrarCobroRemito):
    pass

class ReintegroCliente(MdiWidget, Ui_vtnReintegroCliente):
    pass

class VentaContado(MdiWidget, Ui_vtnVentaContado):
    pass

class VentaConRemito(MdiWidget, Ui_vtnVentaConRemito):
    pass

class AltaCliente(MdiWidget, Ui_vtnAltaCliente):
    pass

class BajaCliente(MdiWidget, Ui_vtnBajaCliente):
    pass

class ModificarCliente(MdiWidget, Ui_vtnModificarCliente):
    pass

class Ingresar(QtGui.QDialog, Ui_vtnIngresar):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.accepted.connect(self.crearVtnPrincipal)

    def crearVtnPrincipal(self):
        if (self.txtUsuario.text() == 'foo' and self.txtContrasenia.text() == 'bar'):
            self.accept()
            self.habilitarPermisos(self.txtUsuario.text())
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Usuario o Contraseña incorrecta.')

    def habilitarPermisos(self, usuario):

        self.menuMonodroga.menuAction().setVisible(False)

class MainWindow(QtGui.QMainWindow, Ui_vtnPrincipal):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # Cerrar ventana con la opcion del menu
        self.actionSalir_2.activated.connect(self.close)

        #contenedor de ventanas internas
        self.setCentralWidget(QtGui.QMdiArea(self))
        #self.centralWidget().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        #self.centralWidget().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        # ------ Instanciar ventanas MDI
        action_subwin = [
            (self.actionAltaCliente, AltaCliente),
            (self.actionBajaCliente, BajaCliente),
            (self.actionModificarCliente, ModificarCliente),
            (self.actionAltaMedicamento, AltaMedicamento),
            (self.actionBajaMedicamento, BajaMedicamento),
            (self.actionModificarMedicamento, ModificarMedicamento),
            (self.actionAltaMonodroga, AltaMonodroga),
            (self.actionBajaMonodroga, BajaMonodroga),
            (self.actionModificarMonodroga, ModificarMonodroga),
            (self.actionAltaPresentacion, AltaPresentacion),
            (self.actionBajaPresentacion, BajaPresentacion),
            (self.actionModificarPresentacion, ModificarPresentacion),
            (self.actionAltaProducto, AltaProducto),
            (self.actionBajaProducto, BajaProducto),
            (self.actionModificarProducto, ModificarProducto),
            (self.actionBajaLote, BajaLote),
            (self.actionModificarLote, ModificarLote),
            (self.actionBajaRemito, BajaRemito),
            (self.actionModificarRemito, ModificarRemito),
            (self.actionDevolucionDeCliente, DevolucionDeCliente),
            (self.actionFraccionarProducto, FraccionarProducto),
            (self.actionListar, Listar),
            (self.actionRegistrarCobroRemito, RegistrarCobroRemito),
            (self.actionReintegroCliente, ReintegroCliente),
            (self.actionVentaContado, VentaContado),
            (self.actionVentaConRemito, VentaConRemito),
            (self.actionAjusteNegativoStock, AjusteNegativoStock)
        ]
        for action, subwin in action_subwin:
            mdi = MyMdi(self)
            mdi.setWidget(subwin(mdi))
            self.centralWidget().addSubWindow(mdi)
            mdi.hide()
            action.activated.connect(mdi.show)

    def setBarraEstado(self, estado):
        self.statusBar().showMessage(estado)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    if Ingresar().exec_() == QtGui.QDialog.Accepted:
        myapp = MainWindow()
        myapp.show()
        sys.exit(app.exec_())