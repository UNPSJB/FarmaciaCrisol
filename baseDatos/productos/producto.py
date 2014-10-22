__author__ = 'waldo'

productos = []

class Presentacion(object):

    def __init__(self,tipo, unidadMedida, cantidadFracciones,subPresentacion):
        self.tipo=tipo
        self.unidadMedida=unidadMedida
        self.cantidadFracciones=cantidadFracciones
        self.subPresentacion=subPresentacion

    # def __init__(self, tipo, unidad, cantidad):
    #     self.tipo = tipo
    #     self.unidad = unidad
    #     self.cantidad = cantidad
    #     self.super_presentacion = None
    #     self.sub_presentaciones = []
    #
    # def __str__(self):
    #     return "%s" % self.tipo
    #
    # def agregar_subpresentacion(self, presentacion):
    #     self.sub_presentaciones.append(presentacion)
    #     presentacion.super_presentacion = self

class Lote(object):
    def __init__(self,numeroLote, fechaVencimiento):
        self.numeroLote=numeroLote
        self.fechaVencimiento=fechaVencimiento

class Producto(object):

    def __init__(self, idProducto, id_medicamento, id_presentacion, id_lote, importe, cantidad):
        self.idProducto=idProducto
        self.id_medicamento=id_medicamento
        self.id_presentacion=id_presentacion
        self.id_lote=id_lote
        self.importe=importe
        self.cantidad=cantidad

    # def __init__(self, codigo, importe, cantidad, presentacion, lote, medicamento):
    #     self.codigo = codigo
    #     self.importe = importe
    #     self.cantidad = cantidad
    #     self.presentacion = presentacion
    #     self.lote = lote
    #     self.medicamento = medicamento
    #     productos.append(self)

    # def vender(self, cantidad):
    #     while self.cantidad < cantidad:
    #         prod = self.obtener_super_producto()
    #         prod.fraccionar(self)
    #     self.cantidad -= cantidad
    #
    # def obtener_super_producto(self):
    #     sp = self.presentacion.super_presentacion
    #     prods = [ p for p in productos if p.presentacion == sp and p.medicamento == self.medicamento ]
    #     if prods:
    #         return prods[0]
    #     raise Exception("no puedo mas")
    #
    # def fraccionar(self, producto):
    #     while self.cantidad == 0:
    #         prod = self.obtener_super_producto()
    #         prod.fraccionar(self)
    #     self.cantidad -= 1
    #     producto.cantidad += self.presentacion.cantidad
    #
    # def __str__(self):
    #     return "%s - %s (%d)" % (self.medicamento, self.presentacion, self.cantidad)
