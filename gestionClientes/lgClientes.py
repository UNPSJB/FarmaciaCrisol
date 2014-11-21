__author__ = 'leandro'
from PyQt4 import QtCore
from gui import MdiWidget
from ventanas import Ui_vtnAltaCliente, Ui_vtnBajaCliente, Ui_vtnModificarCliente, Ui_vtnCliente
from validarDatos import ValidarDatos
from baseDatos.clientes import Cliente as ClienteModel

class CRUDWidget(MdiWidget):
    objectCreated = QtCore.pyqtSignal()
    objectModified = QtCore.pyqtSignal()
    objectDeleted = QtCore.pyqtSignal()
    instances = {
        'C': None,
        'R': None,
        'U': None,
        'D': None,
    }

    def actualizar(self):
        pass

    @classmethod
    def actionWidget(cls, tipo):
        return cls.instances[tipo]

    @classmethod
    def create(cls, mdi):
        cls.instances['C'] = gui = cls(mdi)
        gui.setWindowTitle("Alta %s" % cls.__name__)
        modificar = cls.actionWidget('U')
        if modificar:
            gui.objectCreated.connect(modificar.actualizar)
        borrar = cls.actionWidget('D')
        if borrar:
            gui.objectCreated.connect(borrar.actualizar)
        leer = cls.actionWidget('R')
        if leer:
            gui.objectCreated.connect(leer.actualizar)
        return gui

    @classmethod
    def read(cls, mdi):
        cls.instances['R'] = gui = cls(mdi)
        gui.setWindowTitle("Alta %s" % cls.__name__)
        alta = cls.actionWidget('C')
        if alta:
            alta.objectCreated.connect(gui.actualizar)
        modificar = cls.actionWidget('U')
        if modificar:
            modificar.objectModified.connect(gui.actualizar)
        borrar = cls.actionWidget('D')
        if borrar:
            borrar.objectDeleted.connect(gui.actualizar)
        return gui

    @classmethod
    def update(cls, mdi):
        cls.instances['U'] = gui = cls(mdi)
        gui.setWindowTitle("Modificación %s" % cls.__name__)
        alta = cls.actionWidget('C')
        if alta:
            alta.objectCreated.connect(gui.actualizar)
        borrar = cls.actionWidget('D')
        if borrar:
            borrar.objectDeleted.connect(gui.actualizar)
            gui.objectModified.connect(borrar.actualizar)
        return gui

    @classmethod
    def delete(cls, mdi):
        cls.instances['D'] = gui = cls(mdi)
        gui.setWindowTitle("Baja %s" % cls.__name__)
        gui.objectModified.connect(gui.actualizar)
        modificar = cls.actionWidget('U')
        if modificar:
            modificar.objectModified.connect(gui.actualizar)
            gui.objectModified.connect(modificar.actualizar)
        leer = cls.actionWidget('R')
        if leer:
            gui.objectDeleted.connect(leer.actualizar)
        alta = cls.actionWidget('C')
        if alta:
            alta.objectCreated.connect(gui.actualizar)
        return gui

class Cliente(CRUDWidget, Ui_vtnCliente):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()

    def validadores(self):
        ##Esta parte analiza los campos requeridos para el cliente
        self.camposRequeridos = [ getattr(self, "line%s" % campo.title()) for campo in ClienteModel.requeridos ]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.camposRequeridos)
        ##Esta parte analiza los campos que son opcionales
        camposNoRequeridos=[ getattr(self,"line%s" % campo.title()) for campo in ClienteModel.noRequeridos]
        ValidarDatos.setValidador(camposNoRequeridos)

    def cargar_clientes(self):
        self.cargarObjetos(self.tableClientes,
            ClienteModel.buscarTodos("dni", self.sesion).all(),
            ("dni", "nombre", "apellido", "direccion", "telefono")
        )

    def crear(self):
        if self.validarDatos.validarCamposVacios(self.camposRequeridos):
           atributos = {}
           for col in ClienteModel.tabla.columns:
               value = getattr(self, "line%s" % col.name.title()).text()
               atributos[col.name] = value
           cliente = ClienteModel(**atributos)
           if cliente.guardar(self.sesion):
               self.showMsjEstado("El Cliente fue dado de alta.")
               self.limpiarLines()
               self.objectCreated.emit()
           else:
               self.showMsjEstado("El Cliente ya existe.")
        else:
            self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def eliminar(self):
        itemActual=self.tableClientes.currentItem()
        if itemActual==None:
            self.showMsjEstado("No se ha seleccionado ningun Cliente de la tabla")
        else:
            row=itemActual.row()
            dni=self.tableClientes.item(row,0).text()
            query=ClienteModel.buscar(ClienteModel.dni,self.sesion,dni)
            for instance in query.all():
                 self.cliente = instance
            self.cliente.borrar(self.sesion)
            self.showMsjEstado("El Cliente ha sido eliminado")
            self.tableClientes.removeRow(row)
            self.objectDeleted.emit()
            self.actualizar()

    def modificar(self):
        itemActual=self.tableClientes.currentItem()
        if itemActual!=None:
            if self.validarDatos.validarCamposVacios(self.camposRequeridos):
                row=itemActual.row()
                dni=self.tableClientes.item(row,0).text()
                query=ClienteModel.buscar(ClienteModel.dni,self.sesion,dni)
                for instance in query.all():
                    self.cliente = instance
                self.cliente.setNombre(self.lineNombre.text())
                self.cliente.setApellido(self.lineApellido.text())
                self.cliente.setDireccion(self.lineDireccion.text())
                self.cliente.setTelefono(self.lineTelefono.text())
                self.cliente.modificar(self.sesion)
                self.showMsjEstado("El cliente fue modificado")
                self.objectModified.emit()
                self.actualizar()
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Cliente de la tabla")

    def cargarLines(self):
        #Deshabilitar los lines restantes
        self.lineDni.setEnabled(False)
        self.lineNombre.setEnabled(False)
        self.lineApellido.setEnabled(False)
        #Recuperar la informacion de un item
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

    #TODO Falta ver como obtener el nombre del campo que lanzo el evento
    def buscar(self):
        sender=self.sender()
        print (sender.objectName())

    def actualizar(self):
        self.limpiarLines()
        self.limpiarTabla(self.tableClientes,["DNI","Nombre","Apellido","Direccion","Telefono"])
        self.cargar_clientes()

    def limpiarLines(self):
        self.lineDni.clear()
        self.lineDni.setEnabled(True)
        self.lineNombre.clear()
        self.lineNombre.setEnabled(True)
        self.lineApellido.clear()
        self.lineApellido.setEnabled(True)
        self.lineDireccion.clear()
        self.lineTelefono.clear()

    def modificarItem(self):
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
        gui = super(Cliente, cls).create(mdi)
        gui.groupBuscar.hide()
        gui.validadores()
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.limpiarLines)
        return gui

    @classmethod
    def delete(cls, mdi):
        gui = super(Cliente, cls).delete(mdi)
        gui.lineDireccion.setEnabled(False)
        gui.lineTelefono.setEnabled(False)
        gui.lineDni.returnPressed.connect(gui.buscar)
        gui.validadores()
        gui.cargar_clientes()
        gui.lineDni.returnPressed.connect(gui.buscar)
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.tableClientes.itemClicked.connect(gui.cargarLines)
        return gui

    @classmethod
    def update(cls, mdi):
        gui = super(Cliente, cls).update(mdi)
        gui.validadores()
        gui.cargar_clientes()
        gui.tableClientes.itemClicked.connect(gui.modificarItem)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        return gui

