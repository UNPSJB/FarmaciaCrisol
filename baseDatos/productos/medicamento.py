__author__ = 'waldo'
from baseDatos.productos.objetoBase import ObjetoBase
class Monodroga(ObjetoBase):
    def __init__(self, nombre, tipoVta, descripcion):
        self.nombre=nombre
        self.tipoVta=tipoVta
        self.descripcion=descripcion

    # def monodrogas(self, sesion, var):
    #     query = self.buscar(sesion, self, self.nombre, var)
    #     monodrogas = {}
    #     monodroga = None
    #     i = 0
    #     for instance in query.all():
    #         item = [instance.nombre, instance.tipoVta, instance.descripcion]
    #         monodrogas[i] = item
    #         i += 1
    #         monodroga = instance
    #     return monodrogas

class Medicamento(ObjetoBase):
    def __init__(self, nombreComercial, id_monodroga, cantidadMonodroga):
        self.nombreComercial=nombreComercial
        self.id_monodroga=id_monodroga
        self.cantidadMonodroga=cantidadMonodroga

    def __str__(self):
        return "%s" % self.nombreComercial
