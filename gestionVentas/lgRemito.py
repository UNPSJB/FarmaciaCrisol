# coding: latin-1
__author__ = 'waldo'
from ventanas import Ui_vtnRegistrarCobroRemito, Ui_vtnVentaConRemito, Ui_vtnRemito
from gui import MdiWidget,CRUDWidget
from baseDatos.clientes import Cliente as ClienteModel
from baseDatos import Producto as ProductoModel
from baseDatos.ventas import Remito as RemitoModel
from baseDatos.ventas import DetalleRemito as DetalleRemitoModel
from baseDatos.obraSocial import ObraSocial as ObraSocialModel
from baseDatos.productos import LoteProducto as LoteProductoModel
from baseDatos.productos import Lote as LoteModel
from baseDatos.ventas import CobroCliente as CobroClienteModel
from PyQt4 import QtGui
from baseDatos.ventas import Factura as FacturaModel
from baseDatos.ventas import DetalleFactura as DetalleFacturaModel
from datetime import date
class Remito(CRUDWidget,Ui_vtnRemito):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()

    def actualizar(self):
        self.limpiarTabla(self.tableDetalles)
        self.limpiarTabla(self.tableRemito)
        self.cargar_remitos()

    def cargar_remitos(self):
        self.cargarObjetos(self.tableRemito,
            RemitoModel.obtenerTodosRemitos(self.sesion).all(),
            ("numero", "cliente", "fecha_emision")
        )

    def cargarDetalles(self):
        self.limpiarTabla(self.tableDetalles)
        self.tableDetalles.setVisible(True)
        self.lblDetalles.setVisible(True)
        self.lineNumero.setEnabled(False)
        itemActual=self.tableRemito.currentItem()
        valor=int(self.tableRemito.item(itemActual.row(),0).text())
        self.lineNumero.setText(str(valor))
        self.cargarObjetos(self.tableDetalles,
            RemitoModel.buscarDetalles(valor,self.sesion),
            ("nro_linea","producto","cantidad")
        )
        ##Para el calculo de subtotal. Como el subtotal es una dato calculado, no se puede hacer explicita la carga
        ##como sucede en el cargarObjetos
        importes=[]
        for a in self.sesion.query(DetalleRemitoModel).filter(DetalleRemitoModel.id_remito==valor):
            for b in self.sesion.query(ProductoModel).filter(ProductoModel.codigo_barra==a.producto):
                importes.append(b.importe * a.cantidad)
        for row in range(0,self.tableDetalles.rowCount()):
            self.tableDetalles.setItem(row, 3, QtGui.QTableWidgetItem(str(importes[row])))

    def eliminarDetalle(self):
        itemActual=self.tableDetalles.currentItem()
        ok=QtGui.QMessageBox.information(self,"Confirmacion","¿Desea eliminar este item?")
        if ok:
            linea=int(self.tableDetalles.item(itemActual.row(),0).text())
            producto=int(self.tableDetalles.item(itemActual.row(),1).text())
            cantidadRemito=int(self.tableDetalles.item(itemActual.row(),2).text())
            finalizeActualizacion=False
            while not finalizeActualizacion:
                cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
                if not ok:
                    QtGui.QMessageBox.information(self,"Aviso","No se ingreso cantidad")
                else:
                    if cantidad > cantidadRemito:
                        QtGui.QMessageBox.information(self,"Aviso","La cantidad ingresada supera la esperada")
                    else:
                        lote, ok=QtGui.QInputDialog.getText(self,"Lote","Ingrese lote")
                        if not ok:
                            QtGui.QMessageBox.information(self,"Aviso","No se ingreso lote")
                        else:
                            loteP=LoteProductoModel.buscarLoteProducto(self.sesion,producto,str(lote)).first()
                            if loteP==None:
                                QtGui.QMessageBox.information(self,"Aviso","El lote ingresado no se corresponde con el producto")
                            else:
                                loteP.aumentarCantidad(cantidad)
                                loteP.modificar(self.sesion)
                                cantidadRemito-=cantidad
                                self.tableDetalles.item(itemActual.row(),2).setText(str(cantidadRemito))
                                if cantidadRemito==0:
                                    finalizeActualizacion=True
            detalle=RemitoModel.getDetalle(int(self.lineNumero.text()),int(linea),self.sesion).first()
            detalle.borrar(self.sesion)
            self.tableDetalles.removeRow(itemActual.row())

        else:
            return

    def eliminar(self):
        itemActual=self.tableRemito.currentItem()
        if itemActual==None:
            self.showMsjEstado("No se ha seleccionado remito para eliminar")
        else:
            numeroRemito=int(self.tableRemito.item(itemActual.row(),0).text())
            remitoSeleccionado=RemitoModel.buscar(RemitoModel.numero,self.sesion,numeroRemito).first()
            if self.tableDetalles.rowCount()==0:
                remitoSeleccionado.borrar(self.sesion)
                self.tableRemito.removeRow(itemActual.row())
                self.objectDeleted.emit()
                self.limpiarVentana()
            else:
                QtGui.QMessageBox.information(self,"Aviso","Debe dar de baja cada detalle")

    def limpiarVentana(self):
        self.lineNumero.clear()
        self.lineNumero.setEnabled(True)

    @classmethod
    def delete(cls, mdi):
        gui=super(Remito,cls).delete(mdi)
        gui.cargar_remitos()
        gui.tableDetalles.setEnabled(True)
        gui.lblDetalles.hide()
        #TODO Averiguar como emplear el metodo clicked
        gui.tableRemito.clicked.connect(gui.cargarDetalles)
        gui.tableDetalles.itemDoubleClicked.connect(gui.eliminarDetalle)
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnActualizar.pressed.connect(gui.cargar_remitos)
        return gui

    @classmethod
    def update(cls, mdi):
        gui=super(Remito,cls).update(mdi)
        gui.cargar_remitos()
        gui.tableDetalles.hide()
        gui.lblDetalles.hide()
        gui.btnActualizar.pressed.connect(gui.cargar_remitos)
        gui.tableRemito.clicked.connect(gui.cargarDetalles)
        gui.tableDetalles.itemDoubleClicked.connect(gui.eliminarDetalle)
        gui.btnAceptar.pressed.connect(gui.limpiarVentana)
        return gui

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
        self.remito=None
        self.productosAgregados=0
        self.lotesVentas={}

    def cargar_productos(self):
        for n, obj in enumerate(ProductoModel.buscarTodos("codigo_barra",self.sesion).all()):
            self.tableProductos.insertRow(n)
            self.tableProductos.setItem(n, 0, QtGui.QTableWidgetItem(str(obj.codigo_barra)))
            self.tableProductos.setItem(n, 1, QtGui.QTableWidgetItem(str(obj.id_medicamento)))
            self.tableProductos.setItem(n, 2, QtGui.QTableWidgetItem(str(obj.id_presentacion)))
            self.tableProductos.setItem(n, 3, QtGui.QTableWidgetItem(obj.getNombreMonodroga(self.sesion)))
            self.tableProductos.setItem(n, 4, QtGui.QTableWidgetItem(str(obj.getCantidad(self.sesion))))
            self.tableProductos.setItem(n, 5, QtGui.QTableWidgetItem(str(obj.importe)))

    def cargar_clientes(self):
        self.cargarObjetos(self.tableClientes,
            ClienteModel.buscarTodos("dni", self.sesion).all(),
            ("dni", "nombre", "apellido")
        )

    def validadores(self):
        pass
        #TODO HACER ESTO
        ##Esta parte analiza los campos requeridos para el cliente
        #self.camposRequeridos = [ getattr(self, "line%s" % campo.title()) for campo in ClienteModel.requeridos ]
        #self.validarDatos = ValidarDatos()
        #ValidarDatos.setValidador(self.camposRequeridos)

    def buscarCliente(self):
        if self.lineDni.isEnabled():
            print("busqueda con filtrado")
        else:
            self.lineDni.setEnabled(True)
            self.lineApellido.setEnabled(True)
            self.lineNombre.setEnabled(True)
            self.lineNombre.clear()
            self.lineDni.clear()
            self.lineApellido.clear()
            self.limpiarTabla(self.tableClientes)
            self.tableClientes.setVisible(True)
            self.cargar_clientes()

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

    def descontarCantidad(self,detalle,producto,cantidad):
        query=LoteModel.obtenerLoteProducto(producto,self.sesion)
        valores=[]
        for a in query:
            loteProducto=LoteProductoModel.buscarLoteProducto(self.sesion,producto,a.codigo).first()
            if cantidad<=loteProducto.cantidad:
                loteProducto.descontarCantidad(cantidad)
                loteProducto.modificar(self.sesion)
                valores.append([loteProducto,cantidad])
                break
            else:
                cantidad-=loteProducto.cantidad
                valores.append([loteProducto,loteProducto.cantidad])
                loteProducto.descontarCantidad(loteProducto.cantidad)
                loteProducto.modificar(self.sesion)
        self.lotesVentas[detalle]=valores

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
                    rowItemActual=itemActual.row()
                    rows=self.tableRemito.rowCount()
                    if self.productosAgregados==0:
                        self.remito=RemitoModel(RemitoModel.obtenerNumero(self.sesion),int(self.lineDni.text()))
                        self.remito.guardar(self.sesion)
                    self.productosAgregados+=1
                    self.tableRemito.insertRow(rows)
                    self.tableRemito.setItem(rows, 0, QtGui.QTableWidgetItem(str(self.tableProductos.item(rowItemActual,0).text())))
                    self.tableRemito.setItem(rows, 1, QtGui.QTableWidgetItem(str(cantidad)))
                    self.tableRemito.setItem(rows, 2, QtGui.QTableWidgetItem(str(cantidad*float(self.tableProductos.item(rowItemActual,5).text()))))
                    self.detalle=DetalleRemitoModel(self.remito.numero,self.productosAgregados,
                        int(self.tableProductos.item(rowItemActual,0).text()),cantidad)
                    self.descontarCantidad(self.detalle,int(self.tableProductos.item(rowItemActual,0).text()),cantidad)
                    self.detalle.guardar(self.sesion)
                    self.limpiarTabla(self.tableProductos)
                    self.cargar_productos()

    def cambiarCantidad(self):
        itemActual=self.tableRemito.currentItem()
        cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
        #TODO Checkear que la cantidad no sea mayor a la que esta en la base
        #TODO ACTUALIZAR LA CANTIDAD
        if ok:
            importeUnitario=float(self.tableRemito.item(itemActual.row(),2).text())/int(self.tableRemito.item(itemActual.row(),1).text())
            itemCantidad=self.tableRemito.item(itemActual.row(),1)
            itemCantidad.setText(str(cantidad))
            itemImporte=self.tableRemito.item(itemActual.row(),2)
            itemImporte.setText(str(int(cantidad)*importeUnitario))

    def eliminarDetalle(self):
        print("Eliminando Detalle")

    def limpiarVentana(self):
        self.lineDni.setEnabled(True)
        self.lineDni.clear()
        self.lineNombre.setEnabled(True)
        self.lineNombre.clear()
        self.lineApellido.setEnabled(True)
        self.lineApellido.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_3.setEnabled(True)
        self.lineEdit_4.setEnabled(True)
        self.limpiarTabla(self.tableClientes)
        self.limpiarTabla(self.tableProductos)
        self.limpiarTabla(self.tableRemito)
        self.tableClientes.setVisible(True)
        self.cargar_clientes()
        self.cargar_productos()

    def aceptar(self):
        if self.remito==None:
            QtGui.QMessageBox.information(self,"Venta con Remito","No se ha efectuado ninguna venta")
        else:
            QtGui.QMessageBox.information(None,"Venta","La venta se ha realizado con exito")
            self.limpiarTabla(self.tableRemito)
        self.remito=None
        self.productosAgregados=0
        self.limpiarVentana()

    def cancelar(self):
        if self.remito!=None:
            ok=QtGui.QMessageBox.warning(self,"Aviso","¿Desea anular el remito creado?")
            if ok:
                self.remito.anular()
                QtGui.QMessageBox.information(self,"Aviso","Remito Anulado")
                for detalle in self.lotesVentas:
                    for loteVenta in self.lotesVentas[detalle]:
                        loteVenta[0].aumentarCantidad(loteVenta[1])
                        loteVenta[0].modificar(self.sesion)
                self.lotesVentas={}
                self.cargar_productos()
        self.remito=None
        self.productosAgregados=0
        self.limpiarVentana()

class RegistrarCobroRemito(MdiWidget, Ui_vtnRegistrarCobroRemito):
    def __init__(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.cargar_obras()
        self.tableObras.hide()
        self.lineRazonSocial.setEnabled(False)
        self.btnBuscarOs.setEnabled(False)
        self.tableRemitos.setEnabled(False)
        self.rbtnRazonSocial.pressed.connect(self.habilitarObras)
        self.tableObras.itemDoubleClicked.connect(self.cargarLineObra)
        self.btnBuscarOs.pressed.connect(self.buscarObra)
        self.btnBuscarRemito.pressed.connect(self.buscarRemito)
        self.btnAgregar.pressed.connect(self.agregarRemito)
        self.lineNumero.returnPressed.connect(self.buscarRemito)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)
        self.obraSocialSeleccionada=None
        self.factura=None
        self.remitosAgregados=0
        self.detallesAgregados=0
        self.remitoActual=None
        self.remitosCobrados=[]
        self.importeTotal=0

    def buscarObra(self):
        if self.lineRazonSocial.isEnabled():
            print ("buscar con filtrado")
        else:
            self.lineRazonSocial.setEnabled(True)

    def cargarLineObra(self):
        if self.lineRazonSocial.isEnabled():
            itemActual=self.tableObras.currentItem()
            razonSocial=str(self.tableObras.item(itemActual.row(),0).text())
            self.obraSocialSeleccionada=razonSocial
            self.lineRazonSocial.setText(razonSocial)
            self.lineRazonSocial.setEnabled(False)
        else:
            QtGui.QMessageBox.warning(self,"Advertencia","Ya se ha seleccionado una obra social")

    def habilitarObras(self):
        if self.factura!=None:
            QtGui.QMessageBox.information(self,"Aviso","Ya existe una factura. "
                                                       "No se puede modificar la obra social")
        else:
            if not self.rbtnRazonSocial.isChecked():
                self.btnBuscarOs.setEnabled(True)
                self.lineRazonSocial.setEnabled(True)
                self.tableObras.setVisible(True)
            else:
                self.lineRazonSocial.clear()
                self.btnBuscarOs.setEnabled(False)
                self.lineRazonSocial.setEnabled(False)
                self.tableObras.setVisible(False)
                self.obraSocialSeleccionada=None

    def validadores(self):
        pass

    def cargar_obras(self):
        self.cargarObjetos(self.tableObras,
            ObraSocialModel.buscarTodos("razon_social", self.sesion).all(),
            ("razon_social", "cuit", "direccion")
        )

    def buscarRemito(self):
        if self.lineNumero.isEnabled():
            numeroRemito=self.lineNumero.text()
            if len(numeroRemito)==0:
                self.showMsjEstado("No se ha ingresado numero de remito")
            else:
                self.remitoActual=RemitoModel.existeRemito(int(numeroRemito),self.sesion)
                if self.remitoActual== None:
                    QtGui.QMessageBox.warning(self,"Advertencia","El remito ingresado no existe")
                else:
                    if self.remitoActual.estoyCobrado()!=None:
                        QtGui.QMessageBox.information(self,"Aviso","El remito ingresado ya sido cobrado")
                    else:
                        detallesRemitos=RemitoModel.buscarDetalles(int(numeroRemito),self.sesion)
                        self.limpiarTabla(self.tableRemitos)
                        self.cargarObjetos(self.tableRemitos,
                            detallesRemitos,("producto","cantidad")
                        )
                        importes=[]
                        for a in detallesRemitos:
                            for b in self.sesion.query(ProductoModel).filter(ProductoModel.codigo_barra==a.producto):
                                importes.append(b.importe * a.cantidad)
                        for row in range(0,self.tableRemitos.rowCount()):
                            self.tableRemitos.setItem(row, 2, QtGui.QTableWidgetItem(str(importes[row])))
                        self.lineNumero.setEnabled(False)
        else:
            self.lineNumero.clear()
            self.lineNumero.setEnabled(True)
            self.limpiarTabla(self.tableRemitos)

    def obtenerValoresTabla(self,tabla):
        values=[]
        for row in range(0,tabla.rowCount()):
            valuesItem=[]
            for col in range(0,tabla.columnCount()):
                valuesItem.append(tabla.item(row,col).text())
            values.append(valuesItem)
        return values

    def armarItemFactura(self,itemRemito,obraSocial,nroFactura,nroLinea):
        producto=str(itemRemito[0])
        cantidad=str(itemRemito[1])
        importe=str(itemRemito[2])
        if obraSocial==None:
            descuento=0
        else:
            descuento=obraSocial.getDescuento(producto,self.sesion)
        subtotal=(float(importe)*(1-descuento))
        detalleFactura=DetalleFacturaModel(nroFactura,producto,cantidad,subtotal,descuento,nroLinea)
        detalleFactura.guardar(self.sesion)
        #TODO AVERIGUAR PARA OBTENER UN REDONDEO A DOS DECIMALES
        itemFactura=[str(producto),str(cantidad),("%.2f" % subtotal),str(descuento)]
        return itemFactura

    def mostrarTotal(self):
        subtotales=[]
        for row in range(0,self.tableFactura.rowCount()):
            subtotales.append(float(self.tableFactura.item(row,2).text()))
        self.lblImporteTotal.setText("Importe Total: $%.2f" % sum(subtotales))
        self.importeTotal=sum(subtotales)

    def agregarRemito(self):
        if self.tableRemitos.rowCount()==0:
            self.showMsjEstado("No se ha seleccionado remito para agregar")
        else:
            if self.remitosAgregados==0:
                self.factura=FacturaModel(FacturaModel.generarNumero(self.sesion))
                self.factura.guardar(self.sesion)
            self.remitosAgregados+=1
            if self.obraSocialSeleccionada==None:
                obraSocial=None
            else:
                obraSocial=ObraSocialModel.getObraSocial(self.obraSocialSeleccionada,self.sesion)
            for row,item in enumerate(self.obtenerValoresTabla(self.tableRemitos)):
                self.tableFactura.insertRow(row)
                self.detallesAgregados+=1
                for col,value in enumerate(self.armarItemFactura(item,obraSocial,self.factura.numero,self.detallesAgregados)):
                    self.tableFactura.setItem(row,col,QtGui.QTableWidgetItem(str(value)))
            self.remitoActual.setCobrado(self.factura.numero)
            self.remitoActual.modificar(self.sesion)
            self.remitosCobrados.append(self.remitoActual)
            self.mostrarTotal()
            self.limpiarTabla(self.tableRemitos)
            self.lineNumero.setEnabled(True)
            self.lineNumero.clear()

    def limpiarForm(self):
        self.remitosAgregados=0
        self.detallesAgregados=0
        self.factura=None
        self.remitoActual=None
        self.importeTotal=0
        self.limpiarTabla(self.tableFactura)
        self.limpiarTabla(self.tableRemitos)
        self.lineRazonSocial.clear()
        self.lineNumero.clear()
        self.lineNumero.setEnabled(True)
        self.rbtnRazonSocial.setChecked(False)
        self.tableObras.hide()
        self.lblImporteTotal.setText("Importe Total: $0.00")

    def confirmarOperacion(self):
        if self.factura==None:
            QtGui.QMessageBox.information(self,"Aviso","No se ha realizado ningun cobro")
        else:
            efectivo,ok=QtGui.QInputDialog.getText(self,"Importe a pagar",("El importe a pagar es: $%.2f" % self.importeTotal))
            if float(efectivo) > self.importeTotal:
                QtGui.QMessageBox.information(self,"Cambio","Su vuelto es: $%.2f" % (float(efectivo)-self.importeTotal))
            else:
                 QtGui.QMessageBox.information(self,"Cambio","Su vuelto es: $0.00")
            cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Efectivo",self.importeTotal)
            cobroCliente.guardar(self.sesion)
            QtGui.QMessageBox.information(self,"Venta","El cobro ha sido exitoso")
            self.limpiarForm()

    def cancelarOperacion(self):
        if self.factura!=None:
            ok=QtGui.QMessageBox.warning(self,"Aviso","Existe una factura creada")
            if ok:
                self.limpiarForm()
                for remito in self.remitosCobrados:
                    remito.setCobrado(None)
                    remito.modificar(self.sesion)


    #TODO CONTROLAR QUE NO SE PUEDE SELECCIONAR OTRA OBRA SI EXISTE UNA FACTURA

