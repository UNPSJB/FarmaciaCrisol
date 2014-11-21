__author__ = 'waldo'
from ventanas import Ui_vtnBajaRemito, Ui_vtnModificarRemito, Ui_vtnRegistrarCobroRemito, Ui_vtnVentaConRemito
from gui import MdiWidget
from baseDatos.clientes import Cliente as ClienteModel
from baseDatos import Producto as ProductoModel
from PyQt4 import QtGui
from baseDatos.ventas import *
from datetime import date

class BajaRemito(MdiWidget, Ui_vtnBajaRemito):
    pass

class ModificarRemito(MdiWidget, Ui_vtnModificarRemito):
    pass

class RegistrarCobroRemito(MdiWidget, Ui_vtnRegistrarCobroRemito):
    pass

class VentaConRemito(MdiWidget, Ui_vtnVentaConRemito):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.btnBuscarCliente.pressed.connect(self.buscarCliente)
        self.tableClientes.itemDoubleClicked.connect(self.cargarLines)
        self.btnBuscarProducto.pressed.connect(self.buscarProducto)
        self.tableProductos.itemDoubleClicked.connect(self.agregarProducto)
        self.tableRemito.itemDoubleClicked.connect(self.cambiarCantidad)
        self.btnEliminar.pressed.connect(self.eliminarDetalle)
        self.btnAceptar.pressed.connect(self.aceptar)
        self.btnCancelar.pressed.connect(self.cancelar)
        self.cargar_clientes()
        self.cargar_productos()
        self.gbProducto.hide()
        self.gbRemito.hide()


    def cargar_productos(self):
        for n, obj in enumerate(ProductoModel.buscarTodos("id_medicamento",self.sesion).all()):
            self.tableProductos.insertRow(n)
            self.tableProductos.setItem(n, 0, QtGui.QTableWidgetItem(str(obj.codigoBarra)))
            self.tableProductos.setItem(n, 1, QtGui.QTableWidgetItem(str(obj.id_medicamento)))
            self.tableProductos.setItem(n, 2, QtGui.QTableWidgetItem(str(obj.id_presentacion)))
            self.tableProductos.setItem(n, 3, QtGui.QTableWidgetItem(obj.getNombreMonodroga(self.sesion)))
            self.tableProductos.setItem(n, 4, QtGui.QTableWidgetItem(str(obj.cantidad)))
            self.tableProductos.setItem(n, 5, QtGui.QTableWidgetItem(str(obj.importe)))

    def cargar_clientes(self):
        self.cargarObjetos(self.tableClientes,
            ClienteModel.buscarTodos("dni", self.sesion).all(),
            ("dni", "nombre", "apellido")
        )

    def validadores(self):
        pass
        ##Esta parte analiza los campos requeridos para el cliente
        #self.camposRequeridos = [ getattr(self, "line%s" % campo.title()) for campo in ClienteModel.requeridos ]
        #self.validarDatos = ValidarDatos()
        #ValidarDatos.setValidador(self.camposRequeridos)

    def buscarCliente(self):
        print ("Buscando cliente")

    def cargarLines(self):
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
        self.tableClientes.hide()
        self.gbProducto.setVisible(True)
        self.gbRemito.setVisible(True)

    def buscarProducto(self):
        print("Buscando producto")

    def agregarProducto(self):
        itemActual=self.tableProductos.currentItem()
        if itemActual==None:
            self.showMsjEstado("No se ha seleccionado ningun producto para agregar")
        else:
            cantidad, ok = QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
            if not ok:
                self.showMsjEstado("No se ha seleccionado cantidad del producto")
            else:
                if cantidad>int(self.tableProductos.item(itemActual.row(),4).text()):
                    self.showMsjEstado("La cantidad seleccionada es mayor a la actual")
                else:
                    #TODO Buscar la forma de hacerlo generico a la carga de la tabla
                    if self.tableRemito.rowCount()==0:
                        self.remito=Remito(self.lineDni.text(),date.today())
                        self.remito.guardar(self.sesion)
                    rowItemActual=itemActual.row()
                    rows=self.tableRemito.rowCount()
                    self.tableRemito.insertRow(rows)
                    self.tableRemito.setItem(rows, 0, QtGui.QTableWidgetItem(str((self.tableProductos.item(rowItemActual,0).text()))))
                    self.tableRemito.setItem(rows, 1, QtGui.QTableWidgetItem(str(cantidad)))
                    self.tableRemito.setItem(rows, 2, QtGui.QTableWidgetItem(str(cantidad*float(self.tableProductos.item(rowItemActual,5).text()))))
                    self.detalle=DetalleRemito(self.remito.numero,int(self.tableProductos.item(rowItemActual,0).text()),cantidad)
                    self.detalle.guardar(self.sesion)

    def cambiarCantidad(self):
        #TODO Use de DoubleCliked hirent
        #TODO Resguardar la GUI en un pull de GUIS para recuperar los datos
        itemActual=self.tableRemito.currentItem()
        cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
        if ok:
            importeUnitario=float(self.tableRemito.item(itemActual.row(),2).text())/int(self.tableRemito.item(itemActual.row(),1).text())
            itemCantidad=self.tableRemito.item(itemActual.row(),1)
            itemCantidad.setText(str(cantidad))
            itemImporte=self.tableRemito.item(itemActual.row(),2)
            itemImporte.setText(str(int(cantidad)*importeUnitario))

    def eliminarDetalle(self):
        print("Eliminando Detalle")

    def limpiarLines(self):
        self.lineDni.setEnabled(True)
        self.lineDni.clear()
        self.lineNombre.setEnabled(True)
        self.lineNombre.clear()
        self.lineApellido.setEnabled(True)
        self.lineApellido.clear()

    def aceptar(self):
        QtGui.QMessageBox.information(None,"Venta","La venta se ha realizado con exito")
        self.limpiarTabla(self.tableRemito,["Codigo","Cantidad","Importe"])
        self.limpiarLines()

    def cancelar(self):
        print("Cancelando operacion")

    #TODO FALTA RESOLVER EL PROBLEMA DE LA ACTUALIZACION DE LA CANTIDAD
    #TODO REFRESO DE LAS PANTALLAS
    #TODO PROBLEMAS CON EL MANEJO DE LOS REMITOS