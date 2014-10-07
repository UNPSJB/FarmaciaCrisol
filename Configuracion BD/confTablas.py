from sqlalchemy import *
from sqlalchemy.orm import *
from confBaseDatos.lote import Lote
from confBaseDatos.medicamento import Medicamento
from confBaseDatos.monodroga import Monodroga
from confBaseDatos.presentacion import Presentacion
from confBaseDatos.producto import Producto


class Conexion():

	def __init__(self):
		self.engine=create_engine('postgresql://postgres:password@localhost:5432/farmacia')
		self.metadata=MetaData(self.engine)

	def crearSesion(self):
		Session=sessionmaker(bind=self.engine)
		session=Session()
		return session

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
			Column("tipoVta",Integer),
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

		metadata.create_all(bd.engine)
		mapper(Medicamento, tablaMedicamento)
		mapper(Producto, tablaProducto)
		mapper(Monodroga, tablaMonodroga)
		mapper(Lote, tablaLote)
		mapper(Presentacion, tablaPresentacion)