# -*- coding:utf-8 -*-
from baseDatos.productos import ObjetoBase

class Remito(ObjetoBase):

    def __init__(self, cliente, fechaEmision):
        self.cliente=cliente
        self.fecha_emision=fechaEmision

    def getFechaEmision(self):
        return self.fechaEmision


class DetalleRemito(ObjetoBase):

    def __init__(self,id_remito,producto,cantidad):
        self.id_remito=id_remito
        #TODO Resolver el problema de la enumeracion de la linea
        self.producto=producto
        self.cantidad=cantidad



