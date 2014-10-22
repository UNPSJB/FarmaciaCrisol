__author__ = 'waldo'
from gui import MdiWidget
from ventanas import Ui_vtnBajaLote, Ui_vtnModificarLote
class BajaLote(MdiWidget, Ui_vtnBajaLote):
    def confirmarOperacion(self):
        self.showMsjEstado("El Lote fue dado de baja.")

class ModificarLote(MdiWidget, Ui_vtnModificarLote):
    def confirmarOperacion(self):
        self.showMsjEstado("Los datos del Lote fueron modificados.")