__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget
from ventanas import Ui_vtnAltaPresentacion, Ui_vtnBajaPresentacion, Ui_vtnModificarPresentacion
from validarDatos import ValidarDatos
from baseDatos import Presentacion
class AltaPresentacion(MdiWidget, Ui_vtnAltaPresentacion):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.columnHeaders = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
        self.campos = [self.lineTipo, self.lineUnidadMedida, self.lineCantFracc]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.tablaPresentacion.itemClicked.connect(self.setSubPresentacion)
        self.inicializarTabla()
        self.subPresentacion = None
        self.superPresentacion = None

    def inicializarTabla(self):
        presentaciones = self.buscarPresentaciones()
        self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeaders)

    def buscarPresentaciones(self):
        presentaciones = {}
        i = 0
        query = Presentacion.buscarTodos(Presentacion.tipo, self.sesion)
        for instance in query:
            item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
            presentaciones[i] = item
            i += 1
        return presentaciones

    def setSubPresentacion(self):
        self.subPresentacion = self.itemSeleccionado(self.tablaPresentacion)
        self.superPresentacion = str(self.lineTipo.text())

    def confirmarOperacion(self):
        if self.validarDatos.validarCamposVacios(self.campos):
            if self.validarFracciones():
                presentacion = Presentacion(str(self.lineTipo.text()),  str(self.lineUnidadMedida.text()),
                                    str(self.lineCantFracc.text()), self.subPresentacion, None)
                if presentacion.guardar(self.sesion):
                    self.showMsjEstado("La Presentación fue dada de alta.")
                    self.actualizarFraccionable()
                    self.actualizarVentana()
                    self.subPresentacion = None
                    self.superPresentacion = None
                else:
                    self.showMsjEstado("La Presentación ya existe.")
            else:
                self.showMsjEstado("Seleccione la Presentación en la cual puede fraccionarse la Presentación actual.")
        else:
            self.showMsjEstado("Unos o más datos obligatorios no fueron completados.")

    def validarFracciones(self):
        if int(self.lineCantFracc.text()) > 1:
            if self.subPresentacion != None:
                return True
            else:
                return False
        else:
            self.subPresentacion = None
            self.superPresentacion = None
            return True

    def actualizarFraccionable(self):
        if self.superPresentacion != None:
            tipo = self.itemSeleccionado(self.tablaPresentacion)
            query = Presentacion.buscar(Presentacion.tipo, self.sesion, tipo)
            for instance in query.all():
                 presentacion = instance
            presentacion.superPresentacion = self.superPresentacion
            self.sesion.commit()

    def actualizarVentana(self):
        self.lineTipo.setText("")
        self.lineUnidadMedida.setText("")
        self.lineCantFracc.setText("")
        self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
        self.inicializarTabla()

class BajaPresentacion(MdiWidget, Ui_vtnBajaPresentacion):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.columnHeaders = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
        self.campos = [self.lineTipo]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.tablaPresentacion.itemClicked.connect(self.obtenerPresentacion)
        self.presentacion = None
        self.btnBuscar.pressed.connect(self.buscarPresentacion)
        self.lineTipo.returnPressed.connect(self.buscarPresentacion)

    def buscarPresentacion(self):
        self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
        presentaciones = {}
        query = Presentacion.buscarLike(Presentacion.tipo, self.sesion, str(self.lineTipo.text()))
        i = 0
        for instance in query.all():
            item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
            presentaciones[i] = item
            i += 1
            self.presentacion = instance
        if len(presentaciones.items()) < 1:
            self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
        elif len(presentaciones.items()) > 1:
            self.presentacion = None
        self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeaders)

    def obtenerPresentacion(self):
        tipo = self.itemSeleccionado(self.tablaPresentacion)
        query = Presentacion.buscar(Presentacion.tipo, self.sesion, tipo)
        for instance in query.all():
             self.presentacion = instance

    def confirmarOperacion(self):
        if self.tablaPresentacion.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación de la tabla.")
        else:
            if self.presentacion == None:
                self.showMsjEstado("Seleccione una Presentación de la tabla.")
            else:
                self.presentacion.borrar(self.sesion)
                self.showMsjEstado("La Presentación fue dada de baja.")
                self.actualizarVentana()
                self.monodroga = None

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
        self.lineTipo.setText("")

class ModificarPresentacion(MdiWidget, Ui_vtnModificarPresentacion):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.columnHeaders = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
        self.campos = [self.lineTipo, self.lineUnidadMedida, self.lineCantFracc]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.tablaPresentacion.itemClicked.connect(self.obtenerPresentacion)
        self.tablaPresFracc.itemClicked.connect(self.setSubPresentacion)
        self.presentacion = None
        self.subPresentacion = None
        self.btnBuscar.pressed.connect(self.buscarPresentacion)
        self.lineTipo.returnPressed.connect(self.buscarPresentacion)
        self.inicializarTabla()

    def inicializarTabla(self):
        presentaciones = self.buscarPresentaciones()
        self.limpiarTabla(self.tablaPresFracc, self.columnHeaders)
        self.cargarTabla(self.tablaPresFracc, presentaciones, self.columnHeaders)

    def buscarPresentaciones(self):
        presentaciones = {}
        i = 0
        query = Presentacion.buscarTodos(Presentacion.tipo, self.sesion)
        for instance in query:
            item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
            presentaciones[i] = item
            i += 1
        return presentaciones

    def buscarPresentacion(self):
        self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
        presentaciones = {}
        query = Presentacion.buscarLike(Presentacion.tipo, self.sesion, str(self.lineTipo.text()))
        i = 0
        for instance in query.all():
            item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
            presentaciones[i] = item
            i += 1
            self.presentacion = instance
            self.subPresentacion = instance.subPresentacion
        self.limpiarCampos()
        if len(presentaciones.items()) < 1:
            self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
        elif len(presentaciones.items()) > 1:
            self.presentacion = None
            self.subPresentacion = None
        else:
            self.cargarCampos()
        self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeaders)

    def obtenerPresentacion(self):
        tipo = self.itemSeleccionado(self.tablaPresentacion)
        query = Presentacion.buscar(Presentacion.tipo, self.sesion, tipo)
        for instance in query.all():
            self.presentacion = instance
            self.subPresentacion = instance.subPresentacion
        self.cargarCampos()

    def cargarCampos(self):
        self.lineTipo.setText(self.presentacion.tipo)
        self.lineUnidadMedida.setText(self.presentacion.unidadMedida)
        self.lineCantFracc.setText(str(self.presentacion.cantidadFracciones))

    def limpiarCampos(self):
        self.lineTipo.setText("")
        self.lineUnidadMedida.setText("")
        self.lineCantFracc.setText("")

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaPresentacion, self.columnHeaders)
        self.limpiarCampos()
        presentacion = {}
        presentacion[0] = [self.presentacion.tipo, self.presentacion.unidadMedida,
                         self.presentacion.cantidadFracciones, self.presentacion.subPresentacion]
        self.cargarTabla(self.tablaPresentacion, presentacion, self.columnHeaders)
        self.inicializarTabla()

    def setSubPresentacion(self):
        self.subPresentacion = self.itemSeleccionado(self.tablaPresFracc)

    def confirmarOperacion(self):
        if self.tablaPresentacion.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación de la tabla.")
        else:
            if self.presentacion == None:
                self.showMsjEstado("Seleccione una Presentacion de la tabla.")
            else:
                if self.validarDatos.validarCamposVacios(self.campos):
                    if self.validarFracciones():
                        self.presentacion.tipo = str(self.lineTipo.text())
                        self.presentacion.unidadMedida = str(self.lineUnidadMedida.text())
                        self.presentacion.cantidadFracciones = str(self.lineCantFracc.text())
                        self.presentacion.subPresentacion = self.subPresentacion
                        self.presentacion.modificar(self.sesion)
                        self.showMsjEstado("Los datos de la Presentación fueron modificados.")
                        self.actualizarVentana()
                        self.presentacion = None
                        self.subPresentacion = None
                    else:
                        self.showMsjEstado("Seleccione la Presentación en la cual puede fraccionarse la Presentación actual.")
                else:
                    self.showMsjEstado("No pueden haber datos sin completar.")

    def validarFracciones(self):
        if int(self.lineCantFracc.text()) > 1:
            if self.subPresentacion != None:
                return True
            else:
                return False
        else:
            self.subPresentacion = None
            return True