__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget
from ventanas import Ui_vtnModificarMonodroga, Ui_vtnAltaMonodroga, Ui_vtnBajaMonodroga
from baseDatos import Monodroga
from validarDatos import ValidarDatos


class AltaMonodroga(MdiWidget, Ui_vtnAltaMonodroga):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.nombre = None
        self.campos = [self.lineNomb]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)

    def confirmarOperacion(self):
        if self.validarDatos.validarCamposVacios(self.campos):
            monodroga = Monodroga(str(self.lineNomb.text()),  str(self.cmbTipoVenta.currentText()),
                                str(self.txtDescripcion.toPlainText()))
            if monodroga.guardar(self.sesion):
                self.showMsjEstado("La Monodroga fue dada de alta.")
                self.actualizarVentana()
            else:
                self.showMsjEstado("La Monodroga ya existe.")
        else:
            self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def actualizarVentana(self):
        self.lineNomb.setText("")
        self.txtDescripcion.setText("")


class BajaMonodroga(MdiWidget, Ui_vtnBajaMonodroga):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.btnBuscar.pressed.connect(self.buscarMonodrogas)
        self.lineNomb.returnPressed.connect(self.buscarMonodrogas)
        self.tablaMonodroga.itemClicked.connect(self.obtenerMonodroga)
        self.monodroga = None
        self.campos = [self.lineNomb]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeaders = ["Nombre", "Tipo de Venta", "Descripción"]

    def buscarMonodrogas(self):
        self.limpiarTabla(self.tablaMonodroga, self.columnHeaders)
        monodrogas = {}
        query = Monodroga.buscarLike(Monodroga.nombre, self.sesion, str(self.lineNomb.text()))
        i = 0
        for instance in query.all():
            item = [instance.nombre, instance.tipoVta, instance.descripcion]
            monodrogas[i] = item
            i += 1
            self.monodroga = instance
        if len(monodrogas.items()) < 1:
            self.showMsjEstado("No existen Monodrogas que coincidan con el nombre ingresado en la busqueda.")
        elif len(monodrogas.items()) > 1:
            self.monodroga = None
        self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeaders)

    def confirmarOperacion(self):
        if self.tablaMonodroga.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione una Monodroga de la tabla.")
        else:
            if self.monodroga == None:
                self.showMsjEstado("Seleccione una Monodroga de la tabla.")
            else:
                self.monodroga.borrar(self.sesion)
                self.showMsjEstado("La Monodroga fue dada de baja.")
                self.actualizarVentana()
                self.monodroga = None

    def obtenerMonodroga(self):
        nombre = self.itemSeleccionado(self.tablaMonodroga)
        query = Monodroga.buscar(Monodroga.nombre, self.sesion, nombre)
        for instance in query.all():
             self.monodroga = instance

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaMonodroga, self.columnHeaders)
        self.lineNomb.setText("")

class ModificarMonodroga(MdiWidget, Ui_vtnModificarMonodroga):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.btnBuscar.pressed.connect(self.buscarMonodroga)
        self.lineNomb.returnPressed.connect(self.buscarMonodroga)
        self.tablaMonodroga.itemClicked.connect(self.obtenerMonodroga)
        self.monodroga = None
        self.campos = [self.lineNomb]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeaders = ["Nombre", "Tipo de Venta", "Descripción"]

    def buscarMonodroga(self):
        self.limpiarTabla(self.tablaMonodroga, self.columnHeaders)
        monodrogas = {}
        i = 0
        query = Monodroga.buscarLike(Monodroga.nombre, self.sesion, str(self.lineNomb.text()))
        for instance in query.all():
            item = [instance.nombre, instance.tipoVta, instance.descripcion]
            monodrogas[i] = item
            i += 1
            self.monodroga = instance
        if len(monodrogas.items()) < 1:
            self.showMsjEstado("No existen Monodrogas que coincidan con el nombre ingresado en la busqueda.")
        elif len(monodrogas.items()) > 1:
            self.monodroga = None
        else:
            self.cargarCampos()
        self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeaders)

    def cargarCampos(self):
        if self.monodroga.tipoVta == "Libre":
            self.cmbTipoVenta.setCurrentIndex(0)
        elif self.monodroga.tipoVta == "Receta":
            self.cmbTipoVenta.setCurrentIndex(1)
        else:
            self.cmbTipoVenta.setCurrentIndex(2)
        self.txtDescripcion.setText(self.monodroga.descripcion)
        self.lineNomb.setText(self.monodroga.nombre)

    def confirmarOperacion(self):
        if self.tablaMonodroga.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione una Monodroga de la tabla.")
        else:
            if self.monodroga == None:
                self.showMsjEstado("Seleccione una Monodroga de la tabla.")
            else:
                if self.validarDatos.validarCamposVacios(self.campos):
                    self.monodroga.tipoVta = str(self.cmbTipoVenta.currentText())
                    self.monodroga.descripcion = str(self.txtDescripcion.toPlainText())
                    self.monodroga.nombre = str(self.lineNomb.text())
                    self.monodroga.modificar(self.sesion)
                    self.showMsjEstado("Los datos de la Monodroga fueron modificados.")
                    self.actualizarVentana()
                    self.monodroga = None
                else:
                    self.showMsjEstado("No pueden haber datos sin completar.")

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaMonodroga, self.columnHeaders)
        self.lineNomb.setText("")
        self.txtDescripcion.setText("")
        monodrogas = {}
        monodrogas[0] = [self.monodroga.nombre, self.monodroga.tipoVta, self.monodroga.descripcion]
        self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeaders)

    def obtenerMonodroga(self):
        nombre = self.itemSeleccionado(self.tablaMonodroga)
        query = Monodroga.buscar(Monodroga.nombre, self.sesion, nombre)
        for instance in query.all():
            self.monodroga = instance
        self.cargarCampos()