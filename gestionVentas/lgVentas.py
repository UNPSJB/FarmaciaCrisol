# coding: latin-1
__author__ = 'waldo'
from PyQt4 import QtGui
from gui import MdiWidget
from ventanas import Ui_vtnDevolucionDeCliente, Ui_vtnReintegroCliente, Ui_vtnVentaContado
from baseDatos.obraSocial import ObraSocial as ObraSocialModel
from baseDatos.productos import Producto as ProductoModel
from baseDatos.productos import Medicamento as MedicamentoModel
from baseDatos.productos import Monodroga as MonodrogaModel
from baseDatos.obraSocial import Descuento as DescuentoModel
from baseDatos.productos import Lote as LoteModel
from baseDatos.productos import LoteProducto as LoteProductoModel
from baseDatos.ventas import Factura as FacturaModel
from baseDatos.ventas import DetalleFactura as DetalleFacturaModel
from baseDatos.ventas import NotaCredito as NotaCreditoModel
from baseDatos.ventas import DetalleNotaCredito as DetalleNCModel
from baseDatos.ventas import CobroCliente as CobroClienteModel
from datetime import date

class DevolucionDeCliente(MdiWidget, Ui_vtnDevolucionDeCliente):
    def __init__(self,mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.btnBuscar.pressed.connect(self.buscarFactura)
        self.tableFactura.doubleClicked.connect(self.devolverDetalle)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)
        self.facturaSeleccionada=None
        self.notaCredito=None
        self.productosSeleccionados=0
        self.lotesDevueltos={}

    def validadores(self):
        pass

    def buscarFactura(self):
        if not self.lineNumero.isEnabled():
            self.lineNumero.setEnabled(True)
            self.lineNumero.clear()
            self.limpiarTabla(self.tableFactura)
        else:
            self.numeroFacturaActual=str(self.lineNumero.text())
            if len(self.numeroFacturaActual)==0:
                self.showMsjEstado("No se ha ingresado numero de factura")
            else:
                self.facturaSeleccionada=FacturaModel.existeFactura(int(self.numeroFacturaActual),self.sesion)
                if self.facturaSeleccionada==None:
                    QtGui.QMessageBox.information(self,"Aviso","La factura seleccionada no existe")
                else:
                    #TODO CARGAR SOLO LOS DETALLES DE FACTURA QUE NO ESTAN UNA NOTA DE CREDITO
                    if self.facturaSeleccionada.getNC()!=None:
                        QtGui.QMessageBox.information(self,"Aviso","La factura ya ha sido devuelta")
                    else:
                        self.lineNumero.setEnabled(False)
                        self.cargarObjetos(self.tableFactura,self.facturaSeleccionada.getDetalles(self.sesion),
                        ["producto","cantidad","importe"])

    def obtenerValoresItem(self,row):
        values=[]
        for col in range(0,self.tableFactura.columnCount()):
            values.append(self.tableFactura.item(row,col).text())
        return values

    def obtenerNumeroLinea(self,value):
        query=self.facturaSeleccionada.getDetalles(self.sesion).\
            filter(DetalleFacturaModel.id_factura==self.numeroFacturaActual,DetalleFacturaModel.producto==value)
        for a in query:
            return a.nro_linea

    def armarItem(self,item,cantidad, nroLineaNC):
        linea_factura=self.obtenerNumeroLinea(str(item[0]))
        row=self.tableNC.rowCount()
        self.tableNC.insertRow(row)
        for col, elemento in enumerate(item):
            self.tableNC.setItem(row,col,QtGui.QTableWidgetItem(item[col]))
        self.tableNC.item(row,1).setText(str(cantidad))
        detalleNC=DetalleNCModel(self.notaCredito.numero,nroLineaNC,self.facturaSeleccionada.numero,linea_factura)
        detalleNC.guardar(self.sesion)
        return detalleNC

    def devolverDetalle(self):
        itemActual=self.tableFactura.currentItem()
        ok=QtGui.QMessageBox.information(self,"Confirmacion","�Desea devolver este detalle?")
        if ok:
            producto=int(self.tableFactura.item(itemActual.row(),0).text())
            cantOriginal=cantidadFactura=int(self.tableFactura.item(itemActual.row(),1).text())
            finalizeActualizacion=False
            if self.productosSeleccionados==0:
                self.notaCredito=NotaCreditoModel(NotaCreditoModel.generarNumero(self.sesion))
                self.notaCredito.guardar(self.sesion)
            while not finalizeActualizacion:
                cantidad, ok=QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
                if not ok:
                    QtGui.QMessageBox.information(self,"Aviso","No se ingreso cantidad")
                else:
                    if cantidad > cantidadFactura:
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
                                self.lotesDevueltos[loteP]=cantidad
                                cantidadFactura-=cantidad
                                self.tableFactura.item(itemActual.row(),1).setText(str(cantidadFactura))
                                if cantidadFactura==0:
                                    finalizeActualizacion=True
                                    self.productosSeleccionados+=1
            self.armarItem(self.obtenerValoresItem(itemActual.row()),cantOriginal,self.productosSeleccionados)
            self.tableFactura.removeRow(itemActual.row())
        else:
            return

    def limpiarVentana(self):
        self.limpiarTabla(self.tableFactura)
        self.lineNumero.setEnabled(True)
        self.lineNumero.clear()
        self.limpiarTabla(self.tableNC)

    def calcularTotal(self):
        subtotales=[]
        for row in range(0,self.tableNC.rowCount()):
            subtotales.append(float(self.tableNC.item(row,2).text()))
        return sum(subtotales)

    def confirmarOperacion(self):
        self.productosSeleccionados=0
        if self.notaCredito!=None:
            self.facturaSeleccionada.setNC(self.notaCredito.numero)
            self.facturaSeleccionada.modificar(self.sesion)
            cobroC=CobroClienteModel.buscar(CobroClienteModel.id_factura,self.sesion,self.facturaSeleccionada.numero).first()
            if cobroC.tipo=="Efectivo":
                QtGui.QMessageBox.information(self,"Devolucion","El importe en efectivo a entregar es de: $%.2f" % self.calcularTotal())
            QtGui.QMessageBox.information(self,"Devolucion Cliente","La devolucion ha sido exitosa")
            self.notaCredito=None
            self.facturaSeleccionada=None
            self.productosSeleccionados=0
            self.limpiarVentana()
        else:
            QtGui.QMessageBox.information(self,"Devolucion Cliente","No se ha efectuado ninguna devolucion")
            self.limpiarVentana()

    def cancelarOperacion(self):
        self.productosSeleccionados=0
        if self.notaCredito!=None:
            ok=QtGui.QMessageBox.warning(self,"Advertencia","Ya se ha efectuado una nota de credito. �Desea Anularla?")
            if ok:
                for lote in self.lotesDevueltos:
                    lote.descontarCantidad(self.lotesDevueltos[lote])
                    lote.modificar(self.sesion)
                self.limpiarVentana()
                self.lotesDevueltos={}
                QtGui.QMessageBox.information(self,"Devolucion Cliente","La nota de credito ha sido anulada")
        else:
            self.limpiarVentana()

class ReintegroCliente(MdiWidget, Ui_vtnReintegroCliente):
    def __init__(self,mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.cargarObras()
        self.btnBuscarOs.pressed.connect(self.buscarOs)
        self.tableOs.itemDoubleClicked.connect(self.obtenerObra)
        self.btnBuscarFac.pressed.connect(self.buscarFactura)
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)


    def cargarObras(self):
        self.cargarObjetos(self.tableOs,
            ObraSocialModel.buscarTodos("razon_social", self.sesion).all(),
            ("razon_social", "cuit", "direccion")
        )

    def buscarOs(self):
        if self.lineRazon.isEnabled():
            print("buscar por filtrado")
        else:
            self.lineRazon.clear()
            self.lineRazon.setEnabled(True)
            self.lineCuit.clear()
            self.lineCuit.setEnabled(True)
            self.tableOs.setEnabled(True)

    def obtenerObra(self):
        rowActual=self.tableOs.currentItem().row()
        self.lineRazon.setText(str(self.tableOs.item(rowActual,0).text()))
        self.lineRazon.setEnabled(False)
        self.lineCuit.setText(str(self.tableOs.item(rowActual,1).text()))
        self.lineCuit.setEnabled(False)
        self.tableOs.setEnabled(False)

    def buscarFactura(self):
        if not self.lineNumeroFac.isEnabled():
            self.lineNumeroFac.setEnabled(True)
            self.lineNumeroFac.clear()
            self.limpiarTabla(self.tableFactura)
        else:
            self.numeroFacturaActual=str(self.lineNumeroFac.text())
            if len(self.numeroFacturaActual)==0:
                self.showMsjEstado("No se ha ingresado numero de factura")
            else:
                self.facturaSeleccionada=FacturaModel.existeFactura(int(self.numeroFacturaActual),self.sesion)
                if self.facturaSeleccionada==None:
                    QtGui.QMessageBox.information(self,"Aviso","La factura seleccionada no existe")
                else:
                    self.lineNumeroFac.setEnabled(False)
                    self.cargarObjetos(self.tableFactura,self.facturaSeleccionada.getDetalles(self.sesion),
                        ["producto","cantidad","importe"])

    def confirmarOperacion(self):
        pass

    def cancelarOperacion(self):
        pass

class VentaContado(MdiWidget, Ui_vtnVentaContado):

    def __init__(self,mdi):
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores()
        self.cargar_obras()
        self.lineCuit.setEnabled(False)
        self.lineObra.setEnabled(False)
        self.btnBuscar.setEnabled(False)
        self.tableObra.setVisible(False)
        self.tableObra.itemDoubleClicked.connect(self.cargarObra)
        self.tableProductos.itemDoubleClicked.connect(self.agregarProducto)
        self.btnBuscar.pressed.connect(self.limpiarObra)
        self.productosAgregados=0
        self.btnAceptar.pressed.connect(self.confirmarOperacion)
        self.btnCancelar.pressed.connect(self.cancelarOperacion)
        self.rbtnObra.pressed.connect(self.habilitarObras)
        self.btnActualizar.pressed.connect(self.actualizar)
        self.lotesVentas={}
        self.facturaCobrada=False
        self.obraSocialSeleccionada=None
        self.factura = None
        self.cargarProductosSinObra()

    def actualizar(self):
        if self.obraSocialSeleccionada != None:
            self.cargar_productos(self.obraSocialSeleccionada)
        else:
            self.cargarProductosSinObra()
        for row,producto in enumerate(ProductoModel.buscarTodos(ProductoModel.codigo_barra,self.sesion)):
            self.tableProductos.setItem(row,6,QtGui.QTableWidgetItem(str(producto.getCantidad(self.sesion))))

    def habilitarObras(self):
        if self.factura!=None:
            QtGui.QMessageBox.information(self,"Aviso","Ya existe una factura. "
                                                       "No se puede seleccionar otra obra social")
        else:
            if not self.rbtnObra.isChecked():
                self.btnBuscar.setEnabled(True)
                self.lineObra.setEnabled(True)
                self.lineCuit.setEnabled(True)
                self.tableObra.setVisible(True)
            else:
                self.lineObra.clear()
                self.lineCuit.clear()
                self.btnBuscar.setEnabled(False)
                self.lineObra.setEnabled(False)
                self.lineCuit.setEnabled(False)
                self.tableObra.setVisible(False)
                self.obraSocialSeleccionada=None
                self.cargarProductosSinObra()

    def cargarProductosSinObra(self):

        self.limpiarTabla(self.tableProductos)

        query=self.sesion.query(ProductoModel.codigo_barra,ProductoModel.id_medicamento,ProductoModel.id_presentacion,MonodrogaModel.nombre,ProductoModel.importe).\
            join(MedicamentoModel).filter(ProductoModel.id_medicamento==MedicamentoModel.nombre_comercial).\
            join(MonodrogaModel).filter(MedicamentoModel.id_monodroga==MonodrogaModel.nombre).\
            filter(ProductoModel.baja == False)

        for n, obj in enumerate(query):
            self.tableProductos.insertRow(n)
            self.tableProductos.setItem(n, 0, QtGui.QTableWidgetItem(str(obj[0])))
            self.tableProductos.setItem(n, 1, QtGui.QTableWidgetItem(str(obj[1])))
            self.tableProductos.setItem(n, 2, QtGui.QTableWidgetItem(str(obj[2])))
            self.tableProductos.setItem(n, 3, QtGui.QTableWidgetItem(str(obj[3])))
            self.tableProductos.setItem(n, 4, QtGui.QTableWidgetItem(str(0)))
            self.tableProductos.setItem(n, 5, QtGui.QTableWidgetItem(str(obj[4])))

        for row,producto in enumerate(ProductoModel.buscarTodos(ProductoModel.codigo_barra,self.sesion)):
            self.tableProductos.setItem(row,6,QtGui.QTableWidgetItem(str(producto.getCantidad(self.sesion))))

    def cargarObra(self):
        rowActual=self.tableObra.currentItem().row()
        self.lineObra.setText(str(self.tableObra.item(rowActual,0).text()))
        self.lineCuit.setText(str(self.tableObra.item(rowActual,1).text()))
        self.tableObra.hide()
        self.lineObra.setEnabled(False)
        self.lineCuit.setEnabled(False)
        self.cargar_productos(self.lineObra.text())
        self.gbProducto.setVisible(True)

    def limpiarObra(self):
        if self.tableObra.isVisible():
            #TODO Implementar la busqueda por criterio en la tabla
            pass
        else:
            self.lineObra.clear()
            self.lineObra.clear()
            self.lineCuit.clear()
            self.lineObra.setEnabled(True)
            self.lineCuit.setEnabled(True)
            self.tableObra.setVisible(True)
            self.limpiarTabla(self.tableProductos)
            self.gbProducto.hide()

    def validadores(self):
        pass

    def cargar_obras(self):
        self.cargarObjetos(self.tableObra,
            ObraSocialModel.buscarTodos("razon_social", self.sesion).all(),
            ("razon_social", "cuit", "direccion")
        )

    def cargar_productos(self, obraSocial):

        self.limpiarTabla(self.tableProductos)

        query=self.sesion.query(ProductoModel.codigo_barra,ProductoModel.id_medicamento,ProductoModel.id_presentacion,MonodrogaModel.nombre,DescuentoModel.descuento,ProductoModel.importe).\
            join(MedicamentoModel).filter(ProductoModel.id_medicamento==MedicamentoModel.nombre_comercial).\
            join(MonodrogaModel).filter(MedicamentoModel.id_monodroga==MonodrogaModel.nombre).\
            join(DescuentoModel).filter(DescuentoModel.producto==ProductoModel.codigo_barra).\
            filter(DescuentoModel.obra_social==obraSocial, ProductoModel.baja == False)

        for n, obj in enumerate(query):
            self.tableProductos.insertRow(n)
            for m, campo in enumerate(obj):
                self.tableProductos.setItem(n, m, QtGui.QTableWidgetItem(str(campo)))

        for row,producto in enumerate(ProductoModel.buscarTodos(ProductoModel.codigo_barra,self.sesion)):
            self.tableProductos.setItem(row,6,QtGui.QTableWidgetItem(str(producto.getCantidad(self.sesion))))

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
        cantidad, ok = QtGui.QInputDialog.getInt(self,"Cantidad","Ingrese cantidad del producto",1,1,2000,5)
        if not ok:
            self.showMsjEstado("No se ha seleccionado cantidad del producto")
        else:
            cantidadProducto=int(self.tableProductos.item(itemActual.row(),6).text())
            if cantidad>cantidadProducto:
                QtGui.QMessageBox.information(self,"Aviso","La cantidad ingresada es mayor que la del stock")
            else:
                if self.productosAgregados==0:
                    self.factura=FacturaModel(FacturaModel.generarNumero(self.sesion))
                    self.factura.guardar(self.sesion)
                self.productosAgregados+=1
                rowItemActual=itemActual.row()
                rows=self.tableFactura.rowCount()
                self.tableFactura.insertRow(rows)
                #TODO HAY QUE CARGAR LOS DEMAS DATOS DE LA FACTURA
                #--Carga de items en la tabla--*
                importeActual=float(self.tableProductos.item(rowItemActual,5).text())
                descuentoActual=float(self.tableProductos.item(rowItemActual,4).text())
                subtotal=importeActual*(1-descuentoActual)
                ####-------------------------#####
                detalleFactura=DetalleFacturaModel(self.factura.numero,int(self.tableProductos.item(rowItemActual,0).text()),cantidad,
                    subtotal*cantidad,descuentoActual,self.productosAgregados
                )
                self.descontarCantidad(detalleFactura,int(self.tableProductos.item(rowItemActual,0).text()),cantidad)
                self.tableFactura.setItem(rows,0,QtGui.QTableWidgetItem(str(detalleFactura.producto)))
                self.tableFactura.setItem(rows,1,QtGui.QTableWidgetItem(str(detalleFactura.cantidad)))
                self.tableFactura.setItem(rows, 2, QtGui.QTableWidgetItem(str("%.2f"%(subtotal*cantidad))))

                detalleFactura.guardar(self.sesion)
                if self.obraSocialSeleccionada!=None:
                    self.cargar_productos(str(self.lineObra.text()))
                else:
                    self.cargarProductosSinObra()

    def limpiarVentana(self):
        self.lineObra.clear()
        self.lineObra.setEnabled(True)
        self.lineCuit.clear()
        self.lineCuit.setEnabled(True)
        self.tableObra.setVisible(False)
        self.limpiarTabla(self.tableProductos)
        self.limpiarTabla(self.tableFactura)
        self.cargarProductosSinObra()
        self.obraSocialSeleccionada=None

    def cancelarOperacion(self):
        if self.factura!=None:
            ok=QtGui.QMessageBox.warning(self,"Aviso","�Desea anular la factura creada?")
            if ok:
                self.factura.anular()
                QtGui.QMessageBox.information(self,"Aviso","Factura Anulada")
                for detalle in self.lotesVentas:
                    for loteVenta in self.lotesVentas[detalle]:
                        loteVenta[0].aumentarCantidad(loteVenta[1])
                        loteVenta[0].modificar(self.sesion)
                self.lotesVentas={}
        self.factura=None
        self.productosAgregados=0
        self.limpiarVentana()

    def calcularTotal(self):
        subtotales=[]
        for row in range(0,self.tableFactura.rowCount()):
            subtotales.append(float(self.tableFactura.item(row,2).text()))
        importeTotal=sum(subtotales)
        return importeTotal

    def cobrarEfectivo(self):
        efectivo,ok=QtGui.QInputDialog.getText(self,"Cobro Efectivo",("El importe total es: $%.2f. Por favor ingrese monto" % self.calcularTotal()))
        try:
            if float(efectivo)>self.calcularTotal():
                QtGui.QMessageBox.information(self,"Cobro Efectivo","Su vuelto es:%.2f" % (float(efectivo)-self.calcularTotal()))
            cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Efectivo",self.calcularTotal())
            cobroCliente.guardar(self.sesion)
            self.facturaCobrada=True
        except ValueError:
            pass

    def cobrarTarjDebito(self):
        efectivo,ok=QtGui.QInputDialog.getText(self,"Cobro Tarjeta Debito",("El importe total es: $%.2f. Por favor ingrese monto" % self.calcularTotal()))
        try:
            if float(efectivo)==self.calcularTotal():
                cobroCliente=CobroClienteModel(CobroClienteModel.obtenerNumero(self.sesion),self.factura.numero,"Tarjeta Debito",self.calcularTotal())
                cobroCliente.guardar(self.sesion)
                self.facturaCobrada=True
            else:
                QtGui.QMessageBox.information(self,"Aviso","El monto ingresado no coincide con el total de la factura")
        except ValueError:
            pass

    def cobrarNC(self):
        print ("Cobro con NC")

    def cobrarTarjCredito(self):
        print("Cobro con Tarj de Credito")

    def cobrar(self):
        opcionActual=str(self.cboPago.currentText())
        if opcionActual=="Efectivo":
            self.cobrarEfectivo()
        elif opcionActual=="Nota de Cr�dito":
            self.cobrarNC()
        elif opcionActual=="Tarjeta de D�bito":
            self.cobrarTarjDebito()
        else:
            self.cobrarTarjCredito()
        #TODO Hay que buscar todos los detalles asociados a la nota de credito y fijarse si esta completa o no

    def confirmarOperacion(self):
        if self.factura==None:
            QtGui.QMessageBox.information(self,"Aviso","No se ha efectuado ninguna venta")
        else:
            self.cobrar()
            if self.facturaCobrada:
                QtGui.QMessageBox.information(self,"Venta","La venta se ha realizado con exito")
                self.factura=None
                self.productosAgregados=0
                self.limpiarVentana()
            else:
                QtGui.QMessageBox.information(self,"Aviso","La factura aun no ha sido cobrada")
                #TODO FALTA HACER LA PARTE DE LOS COBROS CON TARJETA DB, CR Y NC
