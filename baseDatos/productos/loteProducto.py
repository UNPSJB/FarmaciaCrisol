from baseDatos.productos import ObjetoBase

class LoteProducto(ObjetoBase):

    def __init__(self, id_lote, id_prodcuto):
        self.id_lote=id_lote
        self.id_producto=id_producto

