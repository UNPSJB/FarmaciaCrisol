__author__ = 'waldo'
from sqlalchemy import *
from sqlalchemy.orm import *
from .productos import *
from .usuario import Usuario

class Conexion():

	def __init__(self):
		self.crearBD
		self.engine=create_engine('postgresql://postgres:password@localhost:5432/farmacia')
		self.metadata=MetaData(self.engine)

	def crearSesion(self):
		Session=sessionmaker(bind=self.engine)
		session=Session()
		return session

	@staticmethod
	def crearBD(self):
		try:
			my_db=create_engine('postgresql://postgres:password@localhost:5432')
			conn=my_db.connect()
			conn.execute('create database farmacia')
			conn.connect().execute('commit')
			conn.close()
		except:
			print ("No se pudo crear la base de datos")

			
class CreacionTabla():

	def __init__(self):
		bd=Conexion()
		metadata=MetaData()

		print ("Creacion de Tablas")

		tablaLote=Table('lote',metadata,
			Column("numeroLote", Integer, primary_key=True),
			Column("fechaVencimiento",Date)
		)

		tablaMonodroga=Table("monodroga",metadata,
			Column("nombre",String, primary_key=True),
			Column("tipoVta",String, nullable=False),
			Column("descripcion",String, nullable=False)
		)

		tablaMedicamento=Table('medicamento',metadata,
			Column('nombreComercial',String, primary_key=True),
			Column('id_monodroga',String, ForeignKey("monodroga.nombre")),
			Column('cantidadMonodroga',Integer)
		)

		tablaPresentacion=Table("presentacion",metadata,
			Column("tipo",String, primary_key=True),
			Column("unidadMedida",String, nullable=False),
			Column("cantidadFracciones", Integer, nullable=False),
            Column("subPresentacion",String)
		)

		tablaProducto=Table('producto',metadata,
			Column('idProducto',Integer, primary_key=True),
			Column('id_medicamento',String, ForeignKey("medicamento.nombreComercial")),
			Column('id_presentacion',String, ForeignKey("presentacion.tipo")),
			Column('id_lote',Integer, ForeignKey("lote.numeroLote")),
			Column('importe',Float),
			Column('cantidad',Integer)
		)

		tablaUsuario=Table('usuario',metadata, 
			Column('idUsuario',String, primary_key=True),
			Column('password',String, nullable=False),
			Column('role',String)
		)

		metadata.create_all(bd.engine)
		mapper(Medicamento, tablaMedicamento)
		mapper(Producto, tablaProducto)
		mapper(Monodroga, tablaMonodroga)
		mapper(Lote, tablaLote)
		mapper(Presentacion, tablaPresentacion)
		mapper(Usuario,tablaUsuario)