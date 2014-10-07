class Producto(object):

    def __init__(self, idProducto, id_medicamento, id_presentacion, id_lote, importe, cantidad):
        self.idProducto=idProducto
        self.id_medicamento=id_medicamento
        self.id_presentacion=id_presentacion
        self.id_lote=id_lote
        self.importe=importe
        self.cantidad=cantidad