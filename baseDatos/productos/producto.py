__author__ = 'waldo'
from baseDatos.productos.objetoBase import ObjetoBase
from sqlalchemy import func
from .medicamento import Medicamento

class Presentacion(ObjetoBase):

    def __init__(self, tipo, unidadMedida, cantidadFracciones, subPresentacion, superPresentacion):
        self.tipo=tipo
        self.unidadMedida=unidadMedida
        self.cantidadFracciones=cantidadFracciones
        self.subPresentacion=subPresentacion
        self.superPresentacion=superPresentacion

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

class Lote(ObjetoBase):
    def __init__(self, numeroLote, fechaVencimiento, cantidad, id_producto):
        self.numeroLote=numeroLote
        self.fechaVencimiento=fechaVencimiento
        self.cantidad=cantidad
        self.id_producto=id_producto

class Producto(ObjetoBase):

    def __init__(self, codigoBarra, id_medicamento, id_presentacion, importe):
        self.codigoBarra=codigoBarra
        self.id_medicamento=id_medicamento
        self.id_presentacion=id_presentacion
        self.cantidad=0
        self.importe=importe

    @classmethod
    def buscarCantidad(cls, sesion, lote):
        return sesion.query(lote.id_producto, cls.id_medicamento,
                 cls.id_presentacion, func.sum(lote.cantidad)).\
        filter(cls.codigoBarra == lote.id_producto).\
            group_by(lote.id_producto, cls.id_medicamento,
                 cls.id_presentacion)\
        .order_by(lote.id_producto)

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


    def getNombreMonodroga(self,sesion):
        instance=sesion.query(Medicamento.id_monodroga).\
            filter(Medicamento.nombreComercial == self.id_medicamento)
        return (instance.first().id_monodroga)