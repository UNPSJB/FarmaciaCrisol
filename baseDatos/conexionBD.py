__author__ = 'waldo'
from sqlalchemy import *
from sqlalchemy.orm import *
from .productos import *
from .clientes import *
from .ventas import *


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

        tablaLote=Table('lote',metadata,
            Column("numeroLote", String, primary_key=True),
            Column("fechaVencimiento",Date),
            Column('cantidad',Integer),
            Column('id_producto',Integer, ForeignKey("producto.codigoBarra"))
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
            Column("subPresentacion",String),
            Column("superPresentacion",String)
        )

        tablaProducto=Table('producto',metadata,
            Column('codigoBarra',Integer, primary_key=True),
            Column('id_medicamento',String, ForeignKey("medicamento.nombreComercial")),
            Column('id_presentacion',String, ForeignKey("presentacion.tipo")),
            Column('cantidad',Integer,nullable=False),
            Column('importe',Float)
        )

        Cliente.tabla = Table('cliente',metadata,
            Column('dni',Integer, primary_key=True),
            Column('nombre',String),
            Column('apellido',String),
            Column('direccion',String),
            Column('telefono',String)
        )

        LoteProducto.tabla = Table('lote_producto',metadata,
            Column('id_lote',String, ForeignKey("lote.numeroLote"),primary_key=True),
            Column('id_producto',Integer,ForeignKey("producto.codigoBarra"),primary_key=True),
            Column('cantidad',Integer,nullable=False)
        )

        Remito.tabla=Table('remito',metadata,
            Column('numero',Integer,Sequence('numero_seq'),primary_key=True),
            Column('cliente',Integer,ForeignKey("cliente.dni")),
            Column('fecha_emision',Date)
        )

        DetalleRemito.tabla=Table('detalle_remito',metadata,
            Column('id_remito',Integer,ForeignKey("remito.numero"),primary_key=True),
            Column('nro_linea',Integer,Sequence('nro_linea_seq'),primary_key=True),
            Column('producto',ForeignKey("producto.codigoBarra")),
            Column('cantidad',Integer)
        )

        metadata.create_all(bd.engine)

        mapper(Medicamento, tablaMedicamento)
        mapper(Producto, tablaProducto)
        mapper(Monodroga, tablaMonodroga)
        mapper(Lote, tablaLote)
        mapper(Presentacion, tablaPresentacion)
        mapper(Cliente, Cliente.tabla)
        mapper(LoteProducto,LoteProducto.tabla)
        mapper(Remito,Remito.tabla)
        mapper(DetalleRemito,DetalleRemito.tabla)