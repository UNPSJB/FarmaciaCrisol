# coding: latin-1
__author__ = 'waldo'
from gui import MdiWidget, CRUDWidget
from ventanas import Ui_vtnMedicamento
from baseDatos import Medicamento as MedicamentoModel
from baseDatos import Monodroga as MonodrogaModel
from validarDatos import ValidarDatos
from baseDatos import Producto as ProductoModel
from PyQt4 import QtGui
class Medicamento(CRUDWidget, Ui_vtnMedicamento):
    """
    Lógica del ABM de medicamentos.
    """
    def __init__(self, mdi):
        """
        Constructor de la clase Medicamento.
        :param mdi:
        :return:
        """
        MdiWidget.__init__(self, mdi)
        self.sesion = self.mdi().window().getSesionBD()
        self.validadores(MedicamentoModel)
        self.monodroga = None

    def cargarMedicamentos(self):
        """
        Carga los datos de los medicamentos en las tablas de la ventana.
        :return:
        """
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarTodos("nombre_comercial", self.sesion).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def crear(self):
        """
        Da de alta un medicamento nuevo y lo almacena en la base de datos.
        :return:
        """
        if self.monodroga == None:
            self.showMsjEstado("No se ha seleccionado ninguna Monodroga de la tabla")
        else:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                medicamento = MedicamentoModel(str(self.lineNombre_Med.text()), self.monodroga,
                                               str(self.spinCantidad.value()))
                if medicamento.guardar(self.sesion):
                    self.showMsjEstado("El Medicamento fue dado de alta.")
                    self.limpiarCampos()
                    self.objectCreated.emit()
                else:
                    medicamento = MedicamentoModel.buscar(MedicamentoModel.nombre_comercial, self.sesion,
                                                      str(self.lineNombre_Med.text())).first()
                    if medicamento.getBaja():
                        medicamento.setBaja(False)
                        medicamento.modificar(self.sesion)
                        self.showMsjEstado("El Medicamento fue dado de alta.")
                        self.limpiarCampos()
                        self.objectCreated.emit()
                    else:
                        QtGui.QMessageBox.critical(self, 'Error', 'El Medicamento ya existe.', 'Aceptar')
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")

    def eliminar(self):
        """
        Da de baja el medicamento seleccionado
        :return:
        """
        itemActual = self.tablaMedicamento.currentItem()
        if itemActual == None:
            self.showMsjEstado("No se ha seleccionado ningun Medicamento de la tabla")
        else:
            row = itemActual.row()
            nombre_comercial = str(self.tablaMedicamento.item(row, 0).text())
            if self.bajaValida(ProductoModel, ProductoModel.id_medicamento, nombre_comercial):
                self.medicamento = MedicamentoModel.buscarAlta(MedicamentoModel.nombre_comercial,
                                                               self.sesion, nombre_comercial).first()
                self.medicamento.borrar(self.sesion)
                self.showMsjEstado("El Medicamento ha sido dado de baja.")
                self.tablaMedicamento.removeRow(row)
                self.objectDeleted.emit()
                self.actualizar()
            else:
                QtGui.QMessageBox.critical(self, 'Error', 'El Medicamento no puede ser dado de baja, '
                                                          'esta asignado a 1 ó más productos', 'Aceptar')

    def modificar(self):
        """
        Modifica los datos del medicamento seleccionado.
        :return:
        """
        itemActual = self.tablaMedicamento.currentItem()
        if itemActual != None:
            if ValidarDatos.validarCamposVacios(self.camposRequeridos):
                row = itemActual.row()
                nombre_comercial = str(self.tablaMedicamento.item(row, 0).text())
                self.medicamento = MedicamentoModel.buscarAlta(MedicamentoModel.nombre_comercial,
                                                    self.sesion, nombre_comercial).first()
                self.medicamento.setCantidadMonodroga(str(self.spinCantidad.value()))
                self.medicamento.setIdMonodroga(self.monodroga)
                self.medicamento.modificar(self.sesion)
                self.showMsjEstado("El Medicamento fue modificado")
                self.objectModified.emit()
                self.actualizar()
            else:
                self.showMsjEstado("Hay datos obligatorios que no fueron completados.")
        else:
            self.showMsjEstado("No se ha seleccionado un Medicamento de la tabla")

    def buscarMonodroga(self):
        """
        Busca y carga en la tabla los datos de una monodroga para un nombre ingresado.
        :return:
        """
        self.limpiarTabla(self.tablaMonodroga)
        self.cargarObjetos(self.tablaMonodroga,
            MonodrogaModel.buscarLike(MonodrogaModel.nombre, self.sesion,
                                      str(self.lineNombre_Mon.text())).all(),
            ("nombre", "tipo_venta", "descripcion")
        )

    def buscarMedicamento(self):
        """
        Busca y carga en la tabla los datos de un medicamento para un nombre ingresado.
        :return:
        """
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarObjetos(self.tablaMedicamento,
            MedicamentoModel.buscarLike(MedicamentoModel.nombre_comercial, self.sesion,
                                        str(self.lineNombre_Med.text())).all(),
            ("nombre_comercial", "id_monodroga", "cantidad_monodroga")
        )

    def actualizar(self):
        """
        Actualiza la ventana (campos y tablas).
        :return:
        """
        self.limpiarCampos()
        self.limpiarTabla(self.tablaMedicamento)
        self.cargarMedicamentos()

    def actualizarInfo(self):
        """
        Actualiza la información de las monodrogas mostrada en la tabla de Monodrogas.
        :return:
        """
        self.limpiarTabla(self.tablaMonodroga)
        self.cargarMonodrogas()

    def limpiarCampos(self):
        """
        Vacia los campos de la ventana.
        :return:
        """
        self.lineNombre_Med.clear()
        self.lineNombre_Med.setEnabled(True)
        self.lineNombre_Mon.clear()
        self.spinCantidad.setValue(1)
        self.tablaMonodroga.setCurrentItem(None)
        self.monodroga = None
        self.actualizarInfo()

    def cargarCampos(self):
        """
        Carga los campos con los datos del Medicamento y Monodroga seleccionados.
        :return:
        """
        self.lineNombre_Med.setEnabled(False)
        row = self.tablaMedicamento.currentItem().row()
        infoItem = []
        for col in range(0, self.tablaMedicamento.columnCount()):
            infoItem.append(self.tablaMedicamento.item(row, col).text())
        #Cargar la info del item en los lines
        self.lineNombre_Med.setText(infoItem[0])
        self.lineNombre_Mon.setText(infoItem[1])
        self.monodroga = infoItem[1]
        self.spinCantidad.setValue(int(infoItem[2]))

    def cargarMonodrogas(self):
        """
        Carga los campos con los datos de la Monodroga seleccionada.
        :return:
        """
        self.cargarObjetos(self.tablaMonodroga,
            MonodrogaModel.buscarTodos("nombre", self.sesion).all(),
            ("nombre", "tipo_venta", "descripcion")
        )

    def setMonodroga(self):
        """
        Setea la referencia a la monodroga con la monodroga seleccionado.
        :return:
        """
        row = self.tablaMonodroga.currentItem().row()
        self.monodroga = str(self.tablaMonodroga.item(row, 0).text())
        self.lineNombre_Mon.setText(self.monodroga)

    @classmethod
    def create(cls, mdi):
        """
        Configuración de la ventana Alta Medicamento.
        :param mdi: referencia a la ventana Alta Medicamento.
        :return: gui
        """
        gui = super(Medicamento, cls).create(mdi)
        gui.tablaMedicamento.hide()
        gui.btnBuscarMed.hide()
        gui.cargarMonodrogas()
        gui.lineNombre_Mon.returnPressed.connect(gui.buscarMonodroga)
        gui.btnBuscarMon.pressed.connect(gui.buscarMonodroga)
        gui.btnActualizar.pressed.connect(gui.actualizarInfo)
        gui.btnAceptar.pressed.connect(gui.crear)
        gui.btnCancelar.pressed.connect(gui.limpiarCampos)
        gui.tablaMonodroga.itemClicked.connect(gui.setMonodroga)
        return gui

    @classmethod
    def delete(cls, mdi):
        """
        Configuración de la ventana Baja Medicamento.
        :param mdi: referencia a la ventana Baja Medicamento.
        :return: gui
        """
        gui = super(Medicamento, cls).delete(mdi)
        gui.gbMonodroga.hide()
        gui.lineNombre_Med.returnPressed.connect(gui.buscarMedicamento)
        gui.btnBuscarMed.pressed.connect(gui.buscarMedicamento)
        gui.cargarMedicamentos()
        gui.btnAceptar.pressed.connect(gui.eliminar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.tablaMedicamento.itemClicked.connect(gui.cargarCampos)
        return gui

    @classmethod
    def update(cls, mdi):
        """
        Configuración de la ventana Modificación Medicamento.
        :param mdi: referencia a la ventana Modificación Medicamento.
        :return: gui
        """
        gui = super(Medicamento, cls).update(mdi)
        gui.cargarMedicamentos()
        gui.cargarMonodrogas()
        gui.lineNombre_Mon.returnPressed.connect(gui.buscarMonodroga)
        gui.lineNombre_Med.returnPressed.connect(gui.buscarMedicamento)
        gui.tablaMedicamento.itemClicked.connect(gui.cargarCampos)
        gui.btnActualizar.pressed.connect(gui.actualizarInfo)
        gui.btnAceptar.pressed.connect(gui.modificar)
        gui.btnCancelar.pressed.connect(gui.actualizar)
        gui.btnBuscarMon.pressed.connect(gui.buscarMonodroga)
        gui.btnBuscarMed.pressed.connect(gui.buscarMedicamento)
        gui.tablaMonodroga.itemClicked.connect(gui.setMonodroga)
        return gui