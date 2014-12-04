from baseDatos.productos import ObjetoBase
class Cliente (ObjetoBase):
    requeridos = ("dni", "nombre", "apellido", "direccion")
    noRequeridos = ("telefono", )

    def __init__(self, dni, nombre, apellido, direccion, telefono):
        ObjetoBase.__init__(self)
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def getDni(self):
        return self.dni

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getDireccion(self):
        return self.direccion

    def getTelefono(self):
        return self.telefono

    def setDni(self, dni):
        self.dni = dni

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setDireccion(self,direccion):
        self.direccion=direccion

    def setTelefono(self, telefono):
        self.telefono=telefono