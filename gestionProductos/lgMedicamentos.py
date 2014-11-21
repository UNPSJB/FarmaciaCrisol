__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget
from ventanas import Ui_vtnAltaMedicamento, Ui_vtnBajaMedicamento, Ui_vtnModificarMedicamento
from baseDatos import Medicamento, Monodroga
from validarDatos import ValidarDatos
class AltaMedicamento(MdiWidget, Ui_vtnAltaMedicamento):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.campos = [self.lineNomb, self.lineCantidad]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeaders = ["Nombre", "Tipo de Venta", "Descripción"]
        self.tablaMonodroga.itemClicked.connect(self.obtenerMonodroga)
        self.monodroga = None
        self.inicializarTabla()
        self.btnActMon.pressed.connect(self.inicializarTabla)

    def inicializarTabla(self):
        self.limpiarTabla(self.tablaMonodroga, self.columnHeaders)
        monodrogas = {}
        i = 0
        query = Monodroga.buscarTodos(Monodroga.nombre, self.sesion)
        for instance in query.all():
            item = [instance.nombre, instance.tipoVta, instance.descripcion]
            monodrogas[i] = item
            i += 1
        self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeaders)

    def obtenerMonodroga(self):
        nombre = self.itemSeleccionado(self.tablaMonodroga)
        query = Monodroga.buscar(Monodroga.nombre, self.sesion, nombre)
        for instance in query.all():
            self.monodroga = instance

    def confirmarOperacion(self):
        if self.validarDatos.validarCamposVacios(self.campos):
            if self.monodroga != None:
                medicamento = Medicamento(str(self.lineNomb.text()),  str(self.monodroga.nombre),
                                    str(self.lineCantidad.text()))
                if medicamento.guardar(self.sesion):
                    self.showMsjEstado("El Medicamento fue dado de alta.")
                    self.actualizarVentana()
                    self.monodroga = None
                else:
                    self.showMsjEstado("El Medicamento ya existe.")
            else:
                self.showMsjEstado("Seleccione una Monodroga de la tabla")
        else:
            self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def actualizarVentana(self):
        self.lineCantidad.setText("")
        self.lineNomb.setText("")

class BajaMedicamento(MdiWidget, Ui_vtnBajaMedicamento):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.campos = [self.lineNomb]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeaders = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
        self.tablaMedicamento.itemClicked.connect(self.obtenerMedicamento)
        self.btnBuscar.pressed.connect(self.buscarMedicamentos)
        self.lineNomb.returnPressed.connect(self.buscarMedicamentos)
        self.medicamento = None

    def buscarMedicamentos(self):
        self.limpiarTabla(self.tablaMedicamento, self.columnHeaders)
        medicamentos = {}
        query = Medicamento.buscarLike(Medicamento.nombreComercial, self.sesion, str(self.lineNomb.text()))
        i = 0
        for instance in query.all():
            item = [instance.nombreComercial, instance.id_monodroga, instance.cantidadMonodroga]
            medicamentos[i] = item
            i += 1
            self.medicamento = instance
        if len(medicamentos.items()) < 1:
            self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
        elif len(medicamentos.items()) > 1:
            self.medicamento = None
        self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeaders)

    def obtenerMedicamento(self):
        nombre = self.itemSeleccionado(self.tablaMedicamento)
        query = Medicamento.buscar(Medicamento.nombreComercial, self.sesion, nombre)
        for instance in query.all():
             self.medicamento = instance

    def confirmarOperacion(self):
        if self.tablaMedicamento.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento de la tabla.")
        else:
            if self.medicamento == None:
                self.showMsjEstado("Seleccione un Medicamento de la tabla.")
            else:
                self.medicamento.borrar(self.sesion)
                self.showMsjEstado("El Medicamento fue dado de baja.")
                self.actualizarVentana()
                self.medicamento = None

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaMedicamento, self.columnHeaders)
        self.lineNomb.setText("")
1
class ModificarMedicamento(MdiWidget, Ui_vtnModificarMedicamento):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.btnBuscarMon.pressed.connect(self.buscarMonodroga)
        self.lineNombMon.returnPressed.connect(self.buscarMonodroga)
        self.btnBuscarMed.pressed.connect(self.buscarMedicamento)
        self.lineNombMed.returnPressed.connect(self.buscarMedicamento)
        self.tablaMonodroga.itemClicked.connect(self.setMonodroga)
        self.tablaMedicamento.itemClicked.connect(self.obtenerMedicamento)
        self.campos = [self.lineNombMed, self.lineNombMon, self.lineCantidad]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeadersMon = ["Nombre", "Tipo de Venta", "Descripción"]
        self.columnHeadersMed = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
        self.medicamento = None
        self.monodroga = None

    def buscarMedicamento(self):
        self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
        medicamentos = {}
        query = Medicamento.buscarLike(Medicamento.nombreComercial, self.sesion, str(self.lineNombMed.text()))
        i = 0
        for instance in query.all():
            item = [instance.nombreComercial, instance.id_monodroga, instance.cantidadMonodroga]
            medicamentos[i] = item
            i += 1
            self.medicamento = instance
            self.monodroga = instance.id_monodroga
        if len(medicamentos.items()) < 1:
            self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
        elif len(medicamentos.items()) > 1:
            self.medicamento = None
            self.monodroga = None
        else:
            self.cargarCampos()
        self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeadersMed)

    def obtenerMedicamento(self):
        nombre = self.itemSeleccionado(self.tablaMedicamento)
        query = Medicamento.buscar(Medicamento.nombreComercial, self.sesion, nombre)
        for instance in query.all():
            self.medicamento = instance
            self.monodroga = instance.id_monodroga
        self.cargarCampos()

    def buscarMonodroga(self):
        self.limpiarTabla(self.tablaMonodroga, self.columnHeadersMon)
        monodrogas = {}
        i = 0
        query = Monodroga.buscarLike(Monodroga.nombre, self.sesion, str(self.lineNombMon.text()))
        for instance in query.all():
            item = [instance.nombre, instance.tipoVta, instance.descripcion]
            monodrogas[i] = item
            i += 1
            self.monodroga = instance.nombre
        if len(monodrogas.items()) < 1:
            self.showMsjEstado("No existen Monodrogas que coincidan con el nombre ingresado en la busqueda.")
        elif len(monodrogas.items()) > 1:
            self.monodroga = None
        else:
            self.lineNombMon.setText(self.monodroga)
        self.cargarTabla(self.tablaMonodroga, monodrogas, self.columnHeadersMon)

    def setMonodroga(self):
        self.monodroga = self.itemSeleccionado(self.tablaMonodroga)
        self.lineNombMon.setText(self.monodroga)

    def cargarCampos(self):
        self.lineNombMed.setText(self.medicamento.nombreComercial)
        self.lineNombMon.setText(self.medicamento.id_monodroga)
        self.lineCantidad.setText(str(self.medicamento.cantidadMonodroga))

    def limpiarCampos(self):
        self.lineNombMon.setText("")
        self.lineNombMed.setText("")
        self.lineCantidad.setText("")

    def confirmarOperacion(self):
        if self.tablaMedicamento.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento de la tabla.")
        else:
            if self.medicamento == None:
                self.showMsjEstado("Seleccione un Medicamento de la tabla.")
            else:
                if self.validarDatos.validarCamposVacios(self.campos):
                    if self.monodroga != None:
                        self.medicamento.nombreComercial = str(self.lineNombMed.text())
                        self.medicamento.id_monodroga = self.monodroga
                        self.medicamento.cantidadMonodroga = str(self.lineCantidad.text())
                        self.medicamento.modificar(self.sesion)
                        self.showMsjEstado("Los datos del Medicamento fueron modificados.")
                        self.actualizarVentana()
                        self.medicamento = None
                        self.monodroga = None
                    else:
                        self.showMsjEstado("Seleccione una Monodroga de la tabla.")
                else:
                    self.showMsjEstado("No pueden haber datos sin completar.")

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
        self.limpiarTabla(self.tablaMonodroga, self.columnHeadersMon)
        self.limpiarCampos()
        medicamento = {}
        medicamento[0] = [self.medicamento.nombreComercial, self.medicamento.id_monodroga,
                         self.medicamento.cantidadMonodroga]
        self.cargarTabla(self.tablaMedicamento, medicamento, self.columnHeadersMed)