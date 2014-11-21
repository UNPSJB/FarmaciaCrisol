__author__ = 'waldo'
# coding: latin-1
from gui import MdiWidget
from ventanas import Ui_vtnBajaLote, Ui_vtnModificarLote, Ui_vtnAltaLote
from validarDatos import ValidarDatos
from baseDatos import Producto, Lote
from datetime import datetime, timedelta
from PyQt4 import QtCore
class AltaLote(MdiWidget, Ui_vtnAltaLote):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.campos = [self.lineNumero, self.lineCant]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeaders = ["Código de Barra", "Medicamento", "Presentación", "Importe"]
        self.tablaProducto.itemClicked.connect(self.obtenerProducto)
        self.btnActualizarProductos.pressed.connect(self.inicializarTabla)
        self.producto = None
        self.inicializarTabla()

    def inicializarTabla(self):
        self.limpiarTabla(self.tablaProducto, self.columnHeaders)
        productos = {}
        i = 0
        query = Producto.buscarTodos(Producto.codigoBarra, self.sesion)
        for instance in query.all():
            item = [instance.codigoBarra, instance.id_medicamento, instance.id_presentacion, instance.importe]
            productos[i] = item
            i += 1
        self.cargarTabla(self.tablaProducto, productos, self.columnHeaders)

    def obtenerProducto(self):
        self.producto = self.itemSeleccionado(self.tablaProducto)

    def confirmarOperacion(self):
        if self.producto == None:
                self.showMsjEstado("Seleccione un Producto de la tabla.")
        else:
            if self.validarDatos.validarCamposVacios(self.campos):
                if self.fechaValida():
                    lote = Lote(str(self.lineNumero.text()),  str(self.dateFechVenc.text()),
                            str(self.lineCant.text()), str(self.producto))
                    if lote.guardar(self.sesion):
                        self.showMsjEstado("El Lote fue dado de alta.")
                        self.actualizarVentana()
                        self.producto = None
                    else:
                        self.showMsjEstado("El Lote ya existe.")
            else:
                    self.showMsjEstado("Uno o más datos obligatorios no fueron completados.")

    def actualizarVentana(self):
        self.lineNumero.setText("")
        self.lineCant.setText("")

    def fechaValida(self):
        fecha = datetime.today() + timedelta(days=90) # Suma a la fecha actual 90 días
        formato = "%d/%m/%y"  # Asigna un formato dia mes año
        fechaVenc = datetime.strptime(str(self.dateFechVenc.text()), formato)
        if fechaVenc < fecha:
            self.showMsjEstado("Ingrese una fecha mayor a la de la fecha actual, "
                               "más un periodo de 90 días mínimo. Ejemplo: %s" % fecha.strftime(formato))
            return False
        return True



class BajaLote(MdiWidget, Ui_vtnBajaLote):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.campos = [self.lineNumero]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeaders = ["Número", "Fecha de Vencimiento", "Cantidad", "Producto"]
        self.tablaLote.itemClicked.connect(self.obtenerLote)
        self.btnBuscar.pressed.connect(self.buscarLotes)
        self.lineNumero.returnPressed.connect(self.buscarLotes)
        self.lote = None

    def buscarLotes(self):
        lotes = {}
        self.limpiarTabla(self.tablaLote, self.columnHeaders)
        query = Lote.buscarLike(Lote.numeroLote, self.sesion, str(self.lineNumero.text()))
        i = 0
        for instance in query.all():
            item = [instance.numeroLote, instance.fechaVencimiento, instance.cantidad, instance.id_producto]
            lotes[i] = item
            i += 1
            self.lote = instance
        if len(lotes.items()) < 1:
            self.showMsjEstado("No existen Lotes que coincidan con el número ingresado en la busqueda.")
        elif len(lotes.items()) > 1:
            self.lote = None
        self.cargarTabla(self.tablaLote, lotes, self.columnHeaders)

    def obtenerLote(self):
        numero = self.itemSeleccionado(self.tablaLote)
        query = Lote.buscar(Lote.numeroLote, self.sesion, numero)
        for instance in query.all():
             self.lote = instance

    def confirmarOperacion(self):
        if self.tablaLote.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione un Lote de la tabla.")
        else:
            if self.lote == None:
                self.showMsjEstado("Seleccione un Lote de la tabla.")
            else:
                self.lote.borrar(self.sesion)
                self.showMsjEstado("El Lote fue dado de baja.")
                self.actualizarVentana()
                self.lote = None

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaLote, self.columnHeaders)
        self.lineNumero.setText("")

class ModificarLote(MdiWidget, Ui_vtnModificarLote):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.btnBuscarLote.pressed.connect(self.buscarLotes)
        self.lineNumero.returnPressed.connect(self.buscarLotes)
        self.btnBuscarProd.pressed.connect(self.buscarProducto)
        self.lineCodBarra.returnPressed.connect(self.buscarProducto)
        self.tablaLote.itemClicked.connect(self.obtenerLote)
        self.tablaProducto.itemClicked.connect(self.setProducto)
        self.campos = [self.lineNumero, self.lineCant, self.lineCodBarra]
        self.validarDatos = ValidarDatos()
        ValidarDatos.setValidador(self.campos)
        self.columnHeadersLote = ["Número", "Fecha de Vencimiento", "Cantidad", "Producto"]
        self.columnHeadersProd = ["Código de Barra", "Medicamento", "Presentación", "Importe"]
        self.lote = None
        self.producto = None

    def buscarLotes(self):
        lotes = {}
        self.limpiarTabla(self.tablaLote, self.columnHeadersLote)
        query = Lote.buscarLike(Lote.numeroLote, self.sesion, str(self.lineNumero.text()))
        i = 0
        for instance in query.all():
            item = [instance.numeroLote, instance.fechaVencimiento, instance.cantidad, instance.id_producto]
            lotes[i] = item
            i += 1
            self.lote = instance
        if len(lotes.items()) < 1:
            self.showMsjEstado("No existen Lotes que coincidan con el número ingresado en la busqueda.")
            self.limpiarCampos()
            self.producto = None
        elif len(lotes.items()) > 1:
            self.lote = None
            self.producto = None
        else:
            self.cargarCampos()
        self.cargarTabla(self.tablaLote, lotes, self.columnHeadersLote)

    def obtenerLote(self):
        numero = self.itemSeleccionado(self.tablaLote)
        query = Lote.buscar(Lote.numeroLote, self.sesion, numero)
        for instance in query.all():
            self.lote = instance
            self.cargarCampos()

    def buscarProducto(self):
        productos = {}
        campo = [self.lineCodBarra]
        if self.validarDatos.validarCamposVacios(campo):
            self.limpiarTabla(self.tablaProducto, self.columnHeadersProd)
            query = Producto.buscar(Producto.codigoBarra, self.sesion, str(self.lineCodBarra.text()))
            i = 0
            for instance in query.all():
                item = [instance.codigoBarra, instance.id_medicamento, instance.id_presentacion, instance.importe]
                productos[i] = item
                i += 1
                self.producto = instance.codigoBarra
            if len(productos.items()) < 1:
                self.showMsjEstado("No existen Productos que coincidan con el código de barra ingresado en la busqueda.")
        else:
            self.showMsjEstado("Ingrese el código de barra del Producto para poder realizar la busqueda.")
        self.cargarTabla(self.tablaProducto, productos, self.columnHeadersProd)

    def setProducto(self):
        self.producto = self.itemSeleccionado(self.tablaProducto)
        self.lineCodBarra.setText(self.producto)

    def cargarCampos(self):
        self.lineNumero.setText(self.lote.numeroLote)
        self.lineCodBarra.setText(str(self.lote.id_producto))
        self.lineCant.setText(str(self.lote.cantidad))
        formato = "%d/%m/%y"  # Asigna un formato dia mes año
        fechaVenc = self.lote.fechaVencimiento.strftime(formato)
        formato = "dd/MM/yy"
        fecha = QtCore.QDate.fromString(fechaVenc, formato)
        self.dateFechVenc.setDate(fecha)
        self.producto = self.lote.id_producto

    def limpiarCampos(self):
        self.lineNumero.setText("")
        self.lineCodBarra.setText("")
        self.lineCant.setText("")

    def confirmarOperacion(self):
        if self.tablaLote.rowCount() < 1:
            self.showMsjEstado("Realice una nueva busqueda y seleccione un Lote de la tabla.")
        else:
            if self.lote == None:
                self.showMsjEstado("Seleccione un Lote de la tabla.")
            else:
                if self.validarDatos.validarCamposVacios(self.campos):
                    if self.fechaValida():
                        if self.producto != None:
                            self.lote.numeroLote = str(self.lineNumero.text())
                            self.lote.fechaVencimiento = str(self.dateFechVenc.text())
                            self.lote.cantidad = str(self.lineCant.text())
                            self.lote.id_producto = self.producto
                            self.lote.modificar(self.sesion)
                            self.showMsjEstado("Los datos del Lote fueron modificados.")
                            self.actualizarVentana()
                            self.lote = None
                            self.producto = None
                        else:
                            self.showMsjEstado("Seleccione un Producto de la tabla.")
                else:
                    self.showMsjEstado("No pueden haber datos sin completar.")

    def actualizarVentana(self):
        self.limpiarTabla(self.tablaLote, self.columnHeadersLote)
        self.limpiarTabla(self.tablaProducto, self.columnHeadersProd)
        self.limpiarCampos()
        lote = {}
        lote[0] = [self.lote.numeroLote, self.lote.fechaVencimiento,
                         self.lote.cantidad, self.lote.id_producto]
        self.cargarTabla(self.tablaLote, lote, self.columnHeadersLote)

    def fechaValida(self):
        formato = "%d/%m/%y"  # Asigna un formato dia mes año
        fechaVencMod = datetime.strptime(str(self.dateFechVenc.text()), formato)
        formato = "%Y-%m-%d"
        fechaVencAct = datetime.strptime(str(self.lote.fechaVencimiento), formato)
        # comprueba si la fecha fue modificada en tal caso comprueba que sea una fecha valida
        if fechaVencAct != fechaVencMod:
            fecha = datetime.today() + timedelta(days=90) # Suma a la fecha actual 90 días,TODO los 90 obtenerlos de un archivo de config
            if fechaVencMod < fecha:
                self.showMsjEstado("Ingrese una fecha mayor a la de la fecha actual, "
                                   "más un periodo de 90 días mínimo. Ejemplo: %s" % fecha.strftime(formato))
                return False
        return True
