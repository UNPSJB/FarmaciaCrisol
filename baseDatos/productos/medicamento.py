__author__ = 'waldo'

class Monodroga(object):

    def __init__(self, nombre, tipoVta, descripcion):
        self.nombre=nombre
        self.tipoVta=tipoVta
        self.descripcion=descripcion

class Medicamento(object):

    def __init__(self, nombreComercial, id_monodroga, cantidadMonodroga):
        self.nombreComercial=nombreComercial
        self.id_monodroga=id_monodroga
        self.cantidadMonodroga=cantidadMonodroga

    def __str__(self):
        return "%s" % self.nombreComercial
