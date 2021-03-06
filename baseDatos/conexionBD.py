__author__ = 'waldo'
from sqlalchemy import *
from sqlalchemy.orm import *
from baseDatos.productos import Presentacion, Producto, Lote, Medicamento, Monodroga, LoteProducto
from baseDatos.clientes import Cliente
from baseDatos.ventas import Remito, DetalleRemito, Factura, DetalleFactura, NotaCredito, DetalleNotaCredito, CobroCliente
from baseDatos.obraSocial import ObraSocial, Descuento, FacturaLiquidacion, CobroObraSocial
from baseDatos.usuario import Usuario
class Conexion():
    def __init__(self):
        self.engine = create_engine('postgresql://postgres:password@localhost:5432/farmacia')
        self.metadata = MetaData(self.engine)

    def crearSesion(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session

class CreacionTabla():

    def __init__(self):
        bd = Conexion()
        metadata = MetaData()

        Lote.tabla = Table('lote', metadata,
            Column("codigo", String, primary_key=True),
            Column("fecha_vencimiento", Date)
        )

        Monodroga.tabla = Table("monodroga", metadata,
            Column("nombre", String, primary_key=True),
            Column("tipo_venta", String, nullable=False),
            Column("descripcion", String, nullable=False),
            Column('baja', Boolean, nullable=False)
        )

        Medicamento.tabla = Table('medicamento', metadata,
            Column('nombre_comercial', String, primary_key=True),
            Column('id_monodroga', String, ForeignKey("monodroga.nombre")),
            Column('cantidad_monodroga', Integer),
            Column('baja', Boolean, nullable=False)
        )

        Presentacion.tabla = Table("presentacion", metadata,
            Column("tipo", String, primary_key=True),
            Column("unidad_medida", String, nullable=False),
            Column("cantidad_fracciones", Integer, nullable=False),
            Column("sub_presentacion", String),
            Column("super_presentacion", String),
            Column('baja', Boolean, nullable=False)
        )

        Producto.tabla = Table('producto', metadata,
            Column('codigo_barra', Integer, primary_key=True),
            Column('id_medicamento', String, ForeignKey("medicamento.nombre_comercial")),
            Column('id_presentacion', String, ForeignKey("presentacion.tipo")),
            Column('importe', Float),
            Column('baja', Boolean, nullable=False)
        )

        Cliente.tabla = Table('cliente', metadata,
            Column('dni', Integer, primary_key=True),
            Column('nombre', String),
            Column('apellido', String),
            Column('direccion', String),
            Column('telefono', String),
            Column('baja', Boolean, nullable=False)
        )

        LoteProducto.tabla = Table('lote_producto', metadata,
            Column('id_lote', String, ForeignKey("lote.codigo"), primary_key=True),
            Column('id_producto', Integer, ForeignKey("producto.codigo_barra"), primary_key=True),
            Column('cantidad', Integer, nullable=False)
        )

        Remito.tabla=Table('remito',metadata,
            Column('numero',Integer,primary_key=True),
            Column('cliente',Integer,ForeignKey("cliente.dni")),
            Column('fecha_emision',Date),
            Column('cobrado',Integer),
            Column('anulado',Boolean),
            Column('baja', Boolean, nullable=False)
        )

        DetalleRemito.tabla=Table('detalle_remito',metadata,
            Column('id_remito',Integer,ForeignKey("remito.numero"),primary_key=True),
            Column('nro_linea',Integer,primary_key=True),
            Column('producto',ForeignKey("producto.codigo_barra")),
            Column('cantidad',Integer),
            Column('baja', Boolean, nullable=False)
        )

        ObraSocial.tabla=Table('obra_social',metadata,
            Column('razon_social',String,primary_key=True),
            Column('cuit',String,nullable=False),
            Column('direccion',String,nullable=False)
        )

        Descuento.tabla=Table('descuento',metadata,
            Column('producto',Integer, ForeignKey("producto.codigo_barra"),primary_key=True),
            Column('obra_social',String,ForeignKey("obra_social.razon_social"),primary_key=True),
            Column('descuento',Float)
        )

        NotaCredito.tabla=Table('nota_credito',metadata,
            Column('numero',Integer,primary_key=True),
            Column('fecha_emision',Date,nullable=False),
            Column('anulado',Boolean)
        )

        DetalleNotaCredito.tabla=Table('detalle_nc',metadata,
            Column('nro_nota',Integer,ForeignKey("nota_credito.numero"),primary_key=True),
            Column('nro_linea',Integer,primary_key=True),
            Column('nro_factura',Integer),
            Column('linea_factura',Integer)
        )

        Factura.tabla=Table('factura',metadata,
            Column('numero',Integer,primary_key=True),
            Column('fecha_emision',Date),
            Column('nota_credito',Integer,ForeignKey("nota_credito.numero")),
            Column('anulado',Boolean)
        )

        DetalleFactura.tabla=Table('detalle_factura',metadata,
            Column('id_factura',Integer,ForeignKey("factura.numero"),primary_key=True),
            Column('nro_linea',Integer,primary_key=True),
            Column('producto',ForeignKey("producto.codigo_barra")),
            Column('cantidad',Integer, nullable=False),
            Column('importe',Float,nullable=False),
            Column('descuento',Float)
        )

        CobroCliente.tabla=Table('cobro_cliente',metadata,
            Column('numero',Integer,primary_key=True),
            Column('id_factura',ForeignKey("factura.numero")),
            Column('tipo',String, nullable=False),
            Column('importe',Float,nullable=False),
            Column('nota_credito',ForeignKey("nota_credito.numero"))
        )


        FacturaLiquidacion.tabla=Table('factura_liquidacion',metadata,
            Column('numero',Integer,primary_key=True),
            Column('fecha_emision',Date),
            Column('nro_factura',Integer,ForeignKey("factura.numero"))
        )

        CobroObraSocial.tabla=Table('cobro_obra_social',metadata,
            Column('fecha',Date),
            Column('numero',Integer,primary_key=True),
            Column('cheque_deposito',Integer),
            Column('importe',Float,nullable=False),
            Column('id_factura_liquidacion',Integer,ForeignKey("factura_liquidacion.numero"))
        )

        Usuario.tabla=Table('usuario',metadata,
			Column('id_usuario',String, primary_key=True),
			Column('password',String, nullable=False),
			Column('role',String)
		)

        metadata.create_all(bd.engine)
        mapper(Medicamento, Medicamento.tabla)
        mapper(Producto, Producto.tabla)
        mapper(Monodroga, Monodroga.tabla)
        mapper(Lote, Lote.tabla)
        mapper(Presentacion, Presentacion.tabla)
        mapper(Cliente, Cliente.tabla)
        mapper(LoteProducto, LoteProducto.tabla)
        mapper(Remito, Remito.tabla)
        mapper(DetalleRemito, DetalleRemito.tabla)
        mapper(ObraSocial, ObraSocial.tabla)
        mapper(Descuento, Descuento.tabla)
        mapper(Factura, Factura.tabla)
        mapper(DetalleFactura, DetalleFactura.tabla)
        mapper(NotaCredito, NotaCredito.tabla)
        mapper(DetalleNotaCredito, DetalleNotaCredito.tabla)
        mapper(CobroCliente, CobroCliente.tabla)
        mapper(FacturaLiquidacion, FacturaLiquidacion.tabla)
        mapper(CobroObraSocial, CobroObraSocial.tabla)
        mapper(Usuario, Usuario.tabla)