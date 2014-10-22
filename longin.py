##Esta clase se encarga del logeo de los usuarios que utilizan el sistema
from baseDatos import *

class Login(object):
	
	#COnstructor que recibe el id del usuario, la pass ingresada y la session con la DB
	def __init__(self, idUsuario, password, session):
		self.idUsuario=str(idUsuario)
		self.password=str(password)
		self.session=session


	#Esta funcion retorna el rol correspondiente al usuario (si existe) y no 
	#devuelve None para indicar que el usuario no esta registrado

	def loginValido(self):
		role=None
		for role, in self.session.query(Usuario.role).\
						filter(Usuario.idUsuario==self.idUsuario).\
						filter(Usuario.password==self.password):
			return role

		return role
            
		
		