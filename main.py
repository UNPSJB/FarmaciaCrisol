__author__ = 'waldo'
# coding: latin-1
import re
import sys
from ventanas import *
from baseDatos import *
from gestionClientes import *
from gestionProductos import *
from gestionVentas import *
from gui import MyMdi
from longin import Login
from PyQt4 import QtGui

class Listar(MdiWidget, Ui_vtnListar):
    pass

class Ingresar(MdiWidget, Ui_vtnIngresar):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.buttonBox.accepted.connect(self.validarUsuario)
        self.txtUsuario.returnPressed.connect(self.validarUsuario)
        self.txtContrasenia.returnPressed.connect(self.validarUsuario)

    def validarUsuario(self):

        log=Login(self.txtUsuario.text(),self.txtContrasenia.text(),myapp.getSesionBD())
        rol=log.loginValido()

        if (rol):
            self.mdi().hide()
            self.habilitarPermisos(rol)
        else:
            QtGui.QMessageBox.warning(self, 'Error', 'Usuario o Contraseņa incorrecta.')

    def habilitarPermisos(self, rol):
        self.mdi().window().deshabilitarMenu()
        permisos={'far':self.mdi().window().farmaceutico, 'tec':self.mdi().window().tecnico_farmaceutico,'adm': self.mdi().window().administrador}
        hab_vtn=permisos[rol]
        for hab in hab_vtn:
            if isinstance(hab, QtGui.QMenu):
                hab.menuAction().setVisible(True)
            else:
                hab.setVisible(True)

class MainWindow(QtGui.QMainWindow, Ui_vtnPrincipal):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # ----- Mappea las tablas con la base y crea una sesion
        CreacionTabla()
        bdConexion = Conexion()
        self.sesion = bdConexion.crearSesion()
        # Cerrar ventana con la opcion del menu
        #self.actionSalir_2.activated.connect(self.close)

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
            (self.actionIngresar, Ingresar),
            (self.actionListar, Listar),
            (self.actionRegistrarCobroRemito, RegistrarCobroRemito),
            (self.actionReintegroCliente, ReintegroCliente),
            (self.actionVentaContado, VentaContado),
            (self.actionVentaConRemito, VentaConRemito),
            (self.actionAjusteNegativoStock, AjusteNegativoStock)
        ]

        # ------ Lista de ventanas disponibles para el farmaceutico
        self.farmaceutico = [
            (self.menuCliente),
            (self.actionAltaCliente),
            (self.actionModificarCliente),
            (self.menuVenta),
            (self.actionRegistrarCobroRemito),
            (self.actionReintegroCliente),
            (self.actionVentaContado),
            (self.actionVentaConRemito),
            (self.actionBajaRemito),
            (self.actionModificarRemito),
            (self.actionDevolucionDeCliente),
            (self.menuListar),
            (self.actionListar)
        ]
        # ----- Lista de ventanas disponibles para el administrador
        self.administrador = [
            (self.menuCliente),
            (self.actionAltaCliente),
            (self.actionBajaCliente),
            (self.actionModificarCliente),
            (self.menuListar),
            (self.actionListar)
        ]
        # ----- Lista de ventanas disponibles para el tecnico farmaceutico
        self.tecnico_farmaceutico = [
            (self.menuCliente),
            (self.actionAltaCliente),
            (self.actionBajaCliente),
            (self.actionModificarCliente),
            (self.menuProducto),
            (self.actionAltaMedicamento),
            (self.actionBajaMedicamento),
            (self.actionModificarMedicamento),
            (self.actionAltaMonodroga),
            (self.actionBajaMonodroga),
            (self.actionModificarMonodroga),
            (self.actionAltaPresentacion),
            (self.actionBajaPresentacion),
            (self.actionModificarPresentacion),
            (self.actionAltaProducto),
            (self.actionBajaProducto),
            (self.actionModificarProducto),
            (self.actionBajaLote),
            (self.actionModificarLote),
            (self.actionAjusteNegativoStock),
            (self.actionFraccionarProducto),
            (self.menuListar),
            (self.actionListar),
            (self.menuVenta),
            (self.actionRegistrarCobroRemito),
            (self.actionReintegroCliente),
            (self.actionVentaContado),
            (self.actionVentaConRemito),
            (self.actionBajaRemito),
            (self.actionModificarRemito),
            (self.actionDevolucionDeCliente)
        ]

        for action, subwin in action_subwin:
            mdi = MyMdi(self)
            mdi.setWidget(subwin(mdi))
            self.centralWidget().addSubWindow(mdi)
            if not (action == self.actionIngresar):
                mdi.hide()
            action.triggered.connect(mdi.show)
        self.deshabilitarMenu()

    # ----- muestra un mensaje en la barra de estado de la ventan principal
    def setBarraEstado(self, estado):
        self.statusBar().showMessage(estado)

    # ----- deshabilita los menu y actions cada vez que se llama a la ventana ingresar

    def deshabilitarMenu(self):
        for hab in self.tecnico_farmaceutico:
            if isinstance(hab, QtGui.QMenu):
                hab.menuAction().setVisible(False)
            else:
                hab.setVisible(False)

    # ----- Devuelve la sesion de la BD
    def getSesionBD(self):
        return self.sesion

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())