from ventanas import Ui_vtnAltaMonodroga
from gui import MdiWidget
from validarDatos import ValidarDatos
from gestionProductos import lgMonodrogas
from gui import MyMdi
from PyQt4 import QtGui


class ControladorMonodroga (Ui_vtnAltaMonodroga,MdiWidget):

    def __init__(self, action,subwin, vtnPrincipal):
        self.subwin=subwin
        modelo=lgMonodrogas.AltaMonodroga
        mdi = MyMdi(vtnPrincipal)
        mdi.setWidget(self.setSubwin(mdi))
        vtnPrincipal.centralWidget().addSubWindow(mdi)
        if not (action == vtnPrincipal.actionIngresar):
            mdi.hide()
        mdi.setMinimumHeight(500)
        mdi.setMinimumWidth(500)
        action.triggered.connect(mdi.show)

    def actualizarVentana(self):
        self.lineNomb.setText("")
        self.txtDescripcion.setText("")

    def getVista(self):
        return self.vista

    def setSubwin(self, mdi):
        MdiWidget.__init__(self, mdi)
        self.subwin.sesion = self.mdi().window().getSesionBD()
        self.subwin.nombre = None
        self.campos = [self.lineNomb]
        self.subwin.validarDatos = ValidarDatos()
        self.subwin.validarDatos.setValidator(self.campos)

