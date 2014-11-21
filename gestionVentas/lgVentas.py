__author__ = 'waldo'
from gui import MdiWidget
from ventanas import Ui_vtnDevolucionDeCliente, Ui_vtnReintegroCliente, Ui_vtnVentaContado
class DevolucionDeCliente(MdiWidget, Ui_vtnDevolucionDeCliente):
    pass

class ReintegroCliente(MdiWidget, Ui_vtnReintegroCliente):
    pass

class VentaContado(MdiWidget, Ui_vtnVentaContado):
    pass