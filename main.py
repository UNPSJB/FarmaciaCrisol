__author__ = 'waldo'
# coding: latin-1
import re
import sys
from ventanas import Ui_vtnPrincipal
from baseDatos import Conexion, CreacionTabla
from gestionClientes import *
from gestionProductos import *
from gestionVentas import *
from gui import MyMdi
from lgIngresar import Ingresar
from lgListados import Listar
from PyQt4 import QtGui
from PyQt4 import QtCore
from controladorMonodroga import ControladorMonodroga

class MainWindow(QtGui.QMainWindow, Ui_vtnPrincipal):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # ----- Mappea las tablas con la base y crea una sesion
        CreacionTabla()
        bdConexion = Conexion()
        self.sesion = bdConexion.crearSesion()
        # Cerrar ventana con la opcion del menu
        self.actionSalir_2.triggered.connect(self.close)

        #contenedor de ventanas internas
        self.setCentralWidget(QtGui.QMdiArea(self))
        self.centralWidget().setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.centralWidget().setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        #(self.actionAltaMonodroga, AltaMonodroga),
        # ------ Instanciar ventanas MDI
        action_subwin = [
            (self.actionAltaCliente, Cliente.create),
            (self.actionBajaCliente, Cliente.delete),
            (self.actionModificarCliente, Cliente.update),
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
            (self.actionAltaLote, AltaLote),
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
            (self.actionAltaLote),
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

        #controladorMonodroga=ControladorMonodroga(self.actionAltaMonodroga,AltaMonodroga,self)

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

class Controlador (object):

    def __init__(self):
        self.vtnPrincipal=MainWindow()

    def getVtnPrincipal(self):
        return self.vtnPrincipal


    def iniciar(self):
        self.vtnPrincipal.show()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    controlador=Controlador()
    controlador.iniciar()
    #myapp = MainWindow()
    #myapp.show()
    sys.exit(app.exec_())