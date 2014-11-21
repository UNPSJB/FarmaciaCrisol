from baseDatos.productos import ObjetoBase

class Cliente (ObjetoBase):
    requeridos = ( "dni", "nombre", "apellido", "direccion" )
    noRequeridos=("telefono",)

    def __init__(self,dni,nombre,apellido,direccion,telefono):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.telefono=telefono

    def getDni(self):
        return self.dni

    def getNombre(self):
        return self.nombre

    def setNombre(self,nombre):
        self.nombre=nombre

    def getApellido(self):
        return self.apellido

    def setApellido(self, apellido):
        self.apellido=apellido

    def getDireccion(self):
        return self.direccion

    def getTelefono(self):
        return self.telefono

    def setDireccion(self,direccion):
        self.direccion=direccion

    def setTelefono(self, telefono):
        self.telefono=telefono
