# coding: latin-1
__author__ = 'waldo'
from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnCliente
from validarDatos import ValidarDatos
from baseDatos import Cliente as ClienteModel
from baseDatos import Remito as RemitoModel
from PyQt4 import QtGui
class Cliente(CRUDWidget, Ui_vtnCliente):
    """
    Lógica del ABM de clientes.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase Cliente.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(ClienteModel)

    def cargarClientes(self):
        """
        Carga los datos de los clientes en las tablas de las ventanas (Baja y Modificación).
        :return:
        """
        self.cargarObjetos(self.tableClientes,
            ClienteModel.buscarTodos("dni", self.sesion).all(),
            ("dni", "nombre", "apellido", "direccion", "telefono")
        )

    def crear(self):
        """
        Da de alta un cliente nuevo y lo almacena en la base de datos.
        :return:
        """
        if ValidarDatos.validarCamposVacios(self.camposRequeridos):
            cliente = ClienteModel(str(self.lineDni.text()), str(self.lineNombre.text()),
                                  str(self.lineApellido.text()), str(self.lineDireccion.text()),
                                  str(self.lineTelefono.text()))
            if cliente.guardar(self.sesion):
                self.showMsjEstado("El Cliente fue dado de alta.")
                self.limpiarCampos()
                self.objectCreated.emit()
            else:
                cliente = ClienteModel.buscar(ClienteModel.dni, self.sesion,
                                                      str(self.lineDni.text())).first()
                if cliente.getBaja():
                    cliente.setBaja(False)
                    cliente.modificar(self.sesion)
                    self.showMsjEstado("El Cliente fue dado de alta.")
                    self.limpiarCampos()
                    self.objectCreated.emit()
                else:
                    QtGui.QMessageBox.critical(self, 'Error', 'El Cliente ya existe.', 'Aceptar')
        else:
            self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def eliminar(self):
        """
        Da de baja el cliente selecionado.
        :return:
        """
        itemActual=self.tableClientes.currentItem()
        if itemActual==None:
            self.showMsjEstado("No se ha seleccionado ningun Cliente de la tabla")
        else:
            row = itemActual.row()
            dni = str(self.tableClientes.item(row, 0).text())
            if self.bajaValida(dni):
                query = ClienteModel.buscarAlta(ClienteModel.dni, self.sesion, dni)
                for instance in query.all():
                     self.cliente = instance
                self.cliente.borrar(self.sesion)
                self.showMsjEstado("El Cliente ha sido dado de baja")
                self.tableClientes.removeRow(row)
                self.objectDeleted.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'Existen remitos pendientes de pago para dicho '
                                                          'Cliente.', 'Aceptar')

    def modificar(self):
        """
        Modifica los datos del cliente seleccionado.
        :return:
        """
        itemActual=self.tableClientes.currentItem()
        if itemActual!=None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                row = itemActual.row()
                dni = str(self.tableClientes.item(row, 0).text())
                query = ClienteModel.buscarAlta(ClienteModel.dni, self.sesion, dni)
                for instance in query.all():
                    self.cliente = instance
                self.cliente.setNombre(str(self.lineNombre.text()))
                self.cliente.setApellido(str(self.lineApellido.text()))
                self.cliente.setDireccion(str(self.lineDireccion.text()))
                self.cliente.setTelefono(str(self.lineTelefono.text()))
                self.cliente.modificar(self.sesion)
                self.showMsjEstado("El cliente fue modificado")
                self.objectModified.emit()
                self.actualizar()
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Cliente de la tabla")

    def bajaValida(self, dni):
        """
        Verifica que el cliente no posea remitos sin pagar.
        :param dni: DNI del cliente para el cual se realiza la verificación.
        :return: bool
        """
        remito = RemitoModel.buscarAlta(RemitoModel.cliente, self.sesion, dni).all()
        for r in remito:
            if r.getCobrado() == None:
                return False
        return True

    def cargarCamposBaja(self):
        """
        Carga los campos con los datos del cliente seleccionado (Baja).
        :return:
        """
        self.lineNombre.setEnabled(False)
        self.lineApellido.setEnabled(False)
        self.cargarCamposMod()

    def buscar(self):
        """
        Busca al cliente de acuerdo a la información ingresada y carga los datos en la tabla (Baja y Modificaión).
        :return:
        """
        obj = self.sender().objectName()
        if obj == 'lineDni':
            clientes = ClienteModel.buscarAlta(ClienteModel.dni, self.sesion, str(self.lineDni.text())).all()
        elif obj == 'lineNombre':
            clientes = ClienteModel.buscarLike(ClienteModel.nombre, self.sesion,
                                               str(self.lineNombre.text())).all()
        elif obj == 'lineApellido':
            clientes = ClienteModel.buscarLike(ClienteModel.apellido, self.sesion,
                                               str(self.lineApellido.text())).all()
        elif obj == 'btnBuscar':
            if str(self.lineDni.text()) != "":
                clientes = ClienteModel.buscarAlta(ClienteModel.dni, self.sesion, str(self.lineDni.text())).all()
            elif str(self.lineNombre.text()) != "":
                clientes = ClienteModel.buscarLike(ClienteModel.nombre, self.sesion,
                                               str(self.lineNombre.text())).all()
            elif str(self.lineApellido.text()) != "":
                clientes = ClienteModel.buscarLike(ClienteModel.apellido, self.sesion,
                                               str(self.lineApellido.text())).all()
            else:
                self.showMsjEstado("Ingrese DNI, Nombre o Apellido del Cliente para realizar la"
                                   " busqueda.")
                return
        self.limpiarTabla(self.tableClientes)
        self.cargarObjetos(self.tableClientes, clientes,
            ("dni", "nombre", "apellido", "direccion", "telefono")
        )

    def actualizar(self):
        """
        Actualiza los componentes de las ventanas.
        :return:
        """
        self.limpiarCampos()
        self.limpiarTabla(self.tableClientes)
        self.cargarClientes()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineDni.clear()
        self.lineDni.setEnabled(True)
        self.lineNombre.clear()
        self.lineNombre.setEnabled(True)
        self.lineApellido.clear()
        self.lineApellido.setEnabled(True)
        self.lineDireccion.clear()
        self.lineTelefono.clear()
        self.tableClientes.setCurrentItem(None)

    def cargarCamposMod(self):
        """
        Carga los campos con los datos del cliente seleccionado (Modificación).
        :return:
        """
        self.lineDni.setEnabled(False)
        row=self.tableClientes.currentItem().row()
        infoItem=[]
        for col in range(0,self.tableClientes.columnCount()):
            infoItem.append(self.tableClientes.item(row,col).text())
        #Cargar la info del item en los lines
        self.lineDni.setText(infoItem[0])
        self.lineNombre.setText(infoItem[1])
        self.lineApellido.setText(infoItem[2])
        self.lineDireccion.setText(infoItem[3])
        self.lineTelefono.setText(infoItem[4])

    @classmethod
    def create(cls, mdi):
        """
        Configuración de la ventana Alta Cliente.
        :param mdi: referencia a la ventana Alta Cliente.
        :return: gui
        """
        gui = super(Cliente, cls).create(mdi)
        gui.groupBuscar.hide()
        gui.btnBuscar.hide()
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.limpiarCampos)
        return gui

    @classmethod
    def delete(cls, mdi):
        """
        Configuración de la ventana Baja Cliente.
        :param mdi: referencia a la ventana Baja Cliente.
        :return: gui
        """
        gui = super(Cliente, cls).delete(mdi)
        gui.lineDireccion.setEnabled(False)
        gui.lineTelefono.setEnabled(False)
        gui.lineDni.returnPressed.connect(gui.buscar)
        gui.lineNombre.returnPressed.connect(gui.buscar)
        gui.lineApellido.returnPressed.connect(gui.buscar)
        gui.cargarClientes()
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.btnBuscar.pressed.connect(gui.buscar)
        gui.tableClientes.itemClicked.connect(gui.cargarCamposBaja)
        return gui

    @classmethod
    def update(cls, mdi):
        """
        Configuración de la ventana Modificación Cliente.
        :param mdi: referencia a la ventana Modificación Cliente.
        :return: gui
        """
        gui = super(Cliente, cls).update(mdi)
        gui.cargarClientes()
        gui.tableClientes.itemClicked.connect(gui.cargarCamposMod)
        gui.lineDni.returnPressed.connect(gui.buscar)
        gui.lineNombre.returnPressed.connect(gui.buscar)
        gui.lineApellido.returnPressed.connect(gui.buscar)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.btnBuscar.pressed.connect(gui.buscar)
        return gui

