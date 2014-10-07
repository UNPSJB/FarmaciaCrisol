from datetime import date
from confBaseDatos import Medicamento, Producto, Lote, Monodroga, Presentacion
from confBaseDatos.confTablas import CreacionTabla, Conexion

createTables=CreacionTabla()

bdConexion=Conexion()
session=bdConexion.crearSesion()

lote=Lote(1232,date.today())
monodroga=Monodroga("ibuprofeno",2,"para el dolor de cabeza")
presentacion=Presentacion("tableta","mg",12,"pastilla")
medicamento=Medicamento("ibuprofeno 600","ibuprofeno",600)
producto=Producto(123,"ibuprofeno 600","tableta",1234,13.4,100)

session.add(lote)
#session.add(monodroga)
#session.add(presentacion)
#session.add(medicamento)
#session.add(producto)
session.commit()