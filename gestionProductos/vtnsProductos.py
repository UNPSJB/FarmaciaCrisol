__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget
from ventanas import Ui_vtnAltaProducto, Ui_vtnBajaProducto, \
    Ui_vtnModificarProducto, Ui_vtnFraccionarProducto, Ui_vtnAjusteNegativoStock
from validarDatos import ValidarDatos
from baseDatos import Medicamento, Presentacion, Producto
class AltaProducto(MdiWidget, Ui_vtnAltaProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.campos = [self.lineNombMed, self.lineTipoPres, self.lineCodBarra, self.lineImp]
        self.validarDatos = ValidarDatos()
        self.validarDatos.setValidator(self.campos)
        self.btnBuscarMed.pressed.connect(self.buscarMedicamento)
        self.btnBuscarPres.pressed.connect(self.buscarPresentacion)
        self.lineNombMed.returnPressed.connect(self.buscarMedicamento)
        self.lineTipoPres.returnPressed.connect(self.buscarPresentacion)
        self.tablaMedicamento.itemClicked.connect(self.setMedicamento)
        self.tablaPresentacion.itemClicked.connect(self.setPresentacion)
        self.columnHeadersPres = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
        self.columnHeadersMed = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
        self.medicamento = None
        self.presentacion = None

    def buscarMedicamento(self):
        self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
        medicamentos = {}
        query = self.sesion.query(Medicamento).filter(Medicamento.nombreComercial
                    .like('%'+str(self.lineNombMed.text())+'%')).order_by(Medicamento.nombreComercial)
        i = 0
        for instance in query.all():
            item = [instance.nombreComercial, instance.id_monodroga, instance.cantidadMonodroga]
            medicamentos[i] = item
            i += 1
            self.medicamento = instance.nombreComercial
        if len(medicamentos.items()) < 1:
            self.showMsjEstado("No existen Medicamentos que coincidan con el nombre ingresado en la busqueda.")
        elif len(medicamentos.items()) > 1:
            self.medicamento = None
        else:
            self.lineNombMed.setText(self.medicamento)
        self.cargarTabla(self.tablaMedicamento, medicamentos, self.columnHeadersMed)

    def buscarPresentacion(self):
        self.limpiarTabla(self.tablaPresentacion, self.columnHeadersPres)
        presentaciones = {}
        query = self.sesion.query(Presentacion).filter(Presentacion.tipo
                    .like('%'+str(self.lineTipoPres.text())+'%')).order_by(Presentacion.tipo)
        i = 0
        for instance in query.all():
            item = [instance.tipo, instance.unidadMedida, instance.cantidadFracciones, instance.subPresentacion]
            presentaciones[i] = item
            i += 1
            self.presentacion = instance.tipo
        if len(presentaciones.items()) < 1:
            self.showMsjEstado("No existen Presentaciones que coincidan con el tipo ingresado en la busqueda.")
        elif len(presentaciones.items()) > 1:
            self.presentacion = None
        else:
            self.lineTipoPres.setText(self.presentacion)
        self.cargarTabla(self.tablaPresentacion, presentaciones, self.columnHeadersPres)

    def setPresentacion(self):
        self.presentacion = self.itemSeleccionado(self.tablaPresentacion)
        self.lineTipoPres.setText(self.presentacion)

    def setMedicamento(self):
        self.medicamento = self.itemSeleccionado(self.tablaMedicamento)
        self.lineNombMed.setText(self.medicamento)

    def confirmarOperacion(self):
        if self.tablaMedicamento.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione un Medicamento de la tabla.")
        else:
            if self.medicamento == None:
                    self.showMsjEstado("Seleccione un Medicamento de la tabla.")
            else:
                if self.tablaPresentacion.rowCount() < 1:
                    self.showMsjEstado("Realice una nueva busqueda y seleccione una Presentación de la tabla.")
                else:
                    if self.presentacion == None:
                        self.showMsjEstado("Seleccione una Presentacion de la tabla.")
                    else:
                        if self.validarDatos.validarCamposVacios(self.campos):
                            producto = Producto(str(self.lineCodBarra.text()),  str(self.lineNombMed.text()),
                                    str(self.lineTipoPres.text()), str(self.lineNroLote.text()),
                                    str(self.lineImp.text()), str(self.lineCantidad.text()))
                            if producto.guardarProducto(self.sesion):
                                self.showMsjEstado("El Producto fue dado de alta.")
                                self.actualizarVentana()
                                self.presentacion = None
                                self.medicamento = None
                            else:
                                self.showMsjEstado("La Presentación ya existe.")
                        else:
                            self.showMsjEstado("Uno o más datos obligatorios no fueron completados.")

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaMedicamento, self.columnHeadersMed)
        self.limpiarTabla(self.tablaPresentacion, self.columnHeadersPres)
        self.lineNombMed.setText("")
        self.lineTipoPres.setText("")
        self.lineCodBarra.setText("")
        self.lineImp.setText("")

class BajaProducto(MdiWidget, Ui_vtnBajaProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.campos = [self.lineCodBarra]
        self.validarDatos = ValidarDatos()
        self.validarDatos.setValidator(self.campos)
        self.columnHeaders = ["Código de Barra", "Medicamento", "Presentación", "Lote", "Importe", "Cantidad"]
        self.tablaProducto.itemClicked.connect(self.obtenerProducto)
        self.btnBuscar.pressed.connect(self.buscarProductos)
        self.lineCodBarra.returnPressed.connect(self.buscarProductos)
        self.producto = None

    def buscarProductos(self):
        self.limpiarTabla(self.tablaProducto, self.columnHeaders)
        productos = {}
        query = self.sesion.query(Producto).filter(Producto.codigoBarra
                    .like('%'+str(self.lineCodBarra.text())+'%')).order_by(Producto.codigoBarra)
        i = 0
        for instance in query.all():
            item = [instance.codigoBarra, instance.id_medicamento, instance.id_presentacion, instance.id_lote,
                    instance.importe, instance.cantidad]
            productos[i] = item
            i += 1
            self.producto = instance
        if len(productos.items()) < 1:
            self.showMsjEstado("No existen Productos que coincidan con el código de barra ingresado en la busqueda.")
        elif len(productos.items()) > 1:
            self.producto = None
        self.cargarTabla(self.tablaProducto, productos, self.columnHeaders)

    def obtenerProducto(self):
        codBarra = self.itemSeleccionado(self.tablaProducto)
        query = self.sesion.query(Producto).filter(Producto.codigoBarra == codBarra)
        for instance in query.all():
             self.producto = instance

    def confirmarOperacion(self):
        if self.tablaProducto.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione un Producto de la tabla.")
        else:
            if self.producto == None:
                self.showMsjEstado("Seleccione un Producto de la tabla.")
            else:
                self.sesion.delete(self.producto)
                self.sesion.commit()
                self.showMsjEstado("El Producto fue dado de baja.")
                self.actualizarVentana()
                self.producto = None

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaProducto, self.columnHeaders)
        self.lineCodBarra.setText("")

class ModificarProducto(MdiWidget, Ui_vtnModificarProducto):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        # self.campos = [self.lineCodBarra, self.lineNombMed, self.lineTipoPres, self.lineImp]
        # self.validarDatos = ValidarDatos()
        # self.validarDatos.setValidator(self.campos)
        # self.columnHeadersProd = ["Código de Barra", "Medicamento", "Presentación", "Lote", "Importe", "Cantidad"]
        # self.tablaProducto.itemClicked.connect(self.obtenerProducto)
        # self.btnBuscarProd.pressed.connect(self.buscarProductos)
        # self.lineCodBarra.returnPressed.connect(self.buscarProductos)
        # self.producto = None
        # self.columnHeadersMed = ["Nombre Comercial", "Monodroga", "Cantidad de Monodroga"]
        # self.tablaMedicamento.itemClicked.connect(self.obtenerMedicamento)
        # self.btnBuscarMed.pressed.connect(self.buscarMedicamentos)
        # self.lineNombMed.returnPressed.connect(self.buscarMedicamentos)
        # self.medicamento = None
        # self.columnHeadersPres = ["Tipo", "Unidad de Medida", "Cantidad de Fracciones", "Fraccionable"]
        # self.tablaPresentacion.itemClicked.connect(self.obtenerPresentacion)
        # self.btnBuscarPres.pressed.connect(self.buscarPresentaciones)
        # self.lineTipoPres.returnPressed.connect(self.buscarPresentaciones)
        # self.presentacion = None

    def confirmarOperacion(self):
        self.showMsjEstado("Los datos del Producto fueron modificados.")

class FraccionarProducto(MdiWidget, Ui_vtnFraccionarProducto):
    def confirmarOperacion(self):
        self.showMsjEstado("El Producto fue fraccionado.")

class AjusteNegativoStock(MdiWidget, Ui_vtnAjusteNegativoStock):
    pass
