# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vtnVentanaPrincipal.ui'
#
# Created: Tue Oct 28 16:56:01 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        vtnPrincipal.setObjectName(_fromUtf8("vtnPrincipal"))
        vtnPrincipal.resize(800, 600)
        self.centralwidget = QtGui.QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.verticalLayout.addWidget(self.mdiArea)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(vtnPrincipal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuUsuario = QtGui.QMenu(self.menubar)
        self.menuUsuario.setObjectName(_fromUtf8("menuUsuario"))
        self.menuVenta = QtGui.QMenu(self.menubar)
        self.menuVenta.setObjectName(_fromUtf8("menuVenta"))
        self.menuProducto = QtGui.QMenu(self.menubar)
        self.menuProducto.setObjectName(_fromUtf8("menuProducto"))
        self.menuMedicamento = QtGui.QMenu(self.menuProducto)
        self.menuMedicamento.setObjectName(_fromUtf8("menuMedicamento"))
        self.menuProducto_2 = QtGui.QMenu(self.menuProducto)
        self.menuProducto_2.setObjectName(_fromUtf8("menuProducto_2"))
        self.menuMonodroga = QtGui.QMenu(self.menuProducto)
        self.menuMonodroga.setObjectName(_fromUtf8("menuMonodroga"))
        self.menuPresentacion = QtGui.QMenu(self.menuProducto)
        self.menuPresentacion.setObjectName(_fromUtf8("menuPresentacion"))
        self.menuLote = QtGui.QMenu(self.menuProducto)
        self.menuLote.setObjectName(_fromUtf8("menuLote"))
        self.menuCliente = QtGui.QMenu(self.menubar)
        self.menuCliente.setObjectName(_fromUtf8("menuCliente"))
        self.menuListar = QtGui.QMenu(self.menubar)
        self.menuListar.setObjectName(_fromUtf8("menuListar"))
        self.menuAyuda = QtGui.QMenu(self.menubar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        vtnPrincipal.setStatusBar(self.statusbar)
        self.actionIngresar = QtGui.QAction(vtnPrincipal)
        self.actionIngresar.setObjectName(_fromUtf8("actionIngresar"))
        self.actionSalir = QtGui.QAction(vtnPrincipal)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionSalir_2 = QtGui.QAction(vtnPrincipal)
        self.actionSalir_2.setObjectName(_fromUtf8("actionSalir_2"))
        self.actionVentaConRemito = QtGui.QAction(vtnPrincipal)
        self.actionVentaConRemito.setObjectName(_fromUtf8("actionVentaConRemito"))
        self.actionVentaContado = QtGui.QAction(vtnPrincipal)
        self.actionVentaContado.setObjectName(_fromUtf8("actionVentaContado"))
        self.actionModificarRemito = QtGui.QAction(vtnPrincipal)
        self.actionModificarRemito.setObjectName(_fromUtf8("actionModificarRemito"))
        self.actionBajaRemito = QtGui.QAction(vtnPrincipal)
        self.actionBajaRemito.setObjectName(_fromUtf8("actionBajaRemito"))
        self.actionRegistrarCobroRemito = QtGui.QAction(vtnPrincipal)
        self.actionRegistrarCobroRemito.setObjectName(_fromUtf8("actionRegistrarCobroRemito"))
        self.actionReintegroCliente = QtGui.QAction(vtnPrincipal)
        self.actionReintegroCliente.setObjectName(_fromUtf8("actionReintegroCliente"))
        self.actionDevolucionDeCliente = QtGui.QAction(vtnPrincipal)
        self.actionDevolucionDeCliente.setObjectName(_fromUtf8("actionDevolucionDeCliente"))
        self.actionBaja_Producto = QtGui.QAction(vtnPrincipal)
        self.actionBaja_Producto.setObjectName(_fromUtf8("actionBaja_Producto"))
        self.actionModificar_Producto = QtGui.QAction(vtnPrincipal)
        self.actionModificar_Producto.setObjectName(_fromUtf8("actionModificar_Producto"))
        self.actionBaja_Medicamento = QtGui.QAction(vtnPrincipal)
        self.actionBaja_Medicamento.setObjectName(_fromUtf8("actionBaja_Medicamento"))
        self.actionModificar_Medicamento = QtGui.QAction(vtnPrincipal)
        self.actionModificar_Medicamento.setObjectName(_fromUtf8("actionModificar_Medicamento"))
        self.actionBaja_Monodroga = QtGui.QAction(vtnPrincipal)
        self.actionBaja_Monodroga.setObjectName(_fromUtf8("actionBaja_Monodroga"))
        self.actionModificar_Monodroga = QtGui.QAction(vtnPrincipal)
        self.actionModificar_Monodroga.setObjectName(_fromUtf8("actionModificar_Monodroga"))
        self.actionBaja_Presentaci_n = QtGui.QAction(vtnPrincipal)
        self.actionBaja_Presentaci_n.setObjectName(_fromUtf8("actionBaja_Presentaci_n"))
        self.actionAltaProducto = QtGui.QAction(vtnPrincipal)
        self.actionAltaProducto.setObjectName(_fromUtf8("actionAltaProducto"))
        self.actionBajaProducto = QtGui.QAction(vtnPrincipal)
        self.actionBajaProducto.setObjectName(_fromUtf8("actionBajaProducto"))
        self.actionModificarProducto = QtGui.QAction(vtnPrincipal)
        self.actionModificarProducto.setObjectName(_fromUtf8("actionModificarProducto"))
        self.actionAltaMedicamento = QtGui.QAction(vtnPrincipal)
        self.actionAltaMedicamento.setObjectName(_fromUtf8("actionAltaMedicamento"))
        self.actionBajaMedicamento = QtGui.QAction(vtnPrincipal)
        self.actionBajaMedicamento.setObjectName(_fromUtf8("actionBajaMedicamento"))
        self.actionModificarMedicamento = QtGui.QAction(vtnPrincipal)
        self.actionModificarMedicamento.setObjectName(_fromUtf8("actionModificarMedicamento"))
        self.actionAltaMonodroga = QtGui.QAction(vtnPrincipal)
        self.actionAltaMonodroga.setObjectName(_fromUtf8("actionAltaMonodroga"))
        self.actionBajaMonodroga = QtGui.QAction(vtnPrincipal)
        self.actionBajaMonodroga.setObjectName(_fromUtf8("actionBajaMonodroga"))
        self.actionModificarMonodroga = QtGui.QAction(vtnPrincipal)
        self.actionModificarMonodroga.setObjectName(_fromUtf8("actionModificarMonodroga"))
        self.actionAltaPresentacion = QtGui.QAction(vtnPrincipal)
        self.actionAltaPresentacion.setObjectName(_fromUtf8("actionAltaPresentacion"))
        self.actionBajaPresentacion = QtGui.QAction(vtnPrincipal)
        self.actionBajaPresentacion.setObjectName(_fromUtf8("actionBajaPresentacion"))
        self.actionModificarPresentacion = QtGui.QAction(vtnPrincipal)
        self.actionModificarPresentacion.setObjectName(_fromUtf8("actionModificarPresentacion"))
        self.actionBajaLote = QtGui.QAction(vtnPrincipal)
        self.actionBajaLote.setObjectName(_fromUtf8("actionBajaLote"))
        self.actionModificarLote = QtGui.QAction(vtnPrincipal)
        self.actionModificarLote.setObjectName(_fromUtf8("actionModificarLote"))
        self.actionFraccionarProducto = QtGui.QAction(vtnPrincipal)
        self.actionFraccionarProducto.setObjectName(_fromUtf8("actionFraccionarProducto"))
        self.actionAltaCliente = QtGui.QAction(vtnPrincipal)
        self.actionAltaCliente.setObjectName(_fromUtf8("actionAltaCliente"))
        self.actionBajaCliente = QtGui.QAction(vtnPrincipal)
        self.actionBajaCliente.setObjectName(_fromUtf8("actionBajaCliente"))
        self.actionModificarCliente = QtGui.QAction(vtnPrincipal)
        self.actionModificarCliente.setObjectName(_fromUtf8("actionModificarCliente"))
        self.actionAjusteNegativoStock = QtGui.QAction(vtnPrincipal)
        self.actionAjusteNegativoStock.setObjectName(_fromUtf8("actionAjusteNegativoStock"))
        self.actionListar = QtGui.QAction(vtnPrincipal)
        self.actionListar.setObjectName(_fromUtf8("actionListar"))
        self.actionAyuda = QtGui.QAction(vtnPrincipal)
        self.actionAyuda.setObjectName(_fromUtf8("actionAyuda"))
        self.actionAcercaDe = QtGui.QAction(vtnPrincipal)
        self.actionAcercaDe.setObjectName(_fromUtf8("actionAcercaDe"))
        self.actionAltaLote = QtGui.QAction(vtnPrincipal)
        self.actionAltaLote.setObjectName(_fromUtf8("actionAltaLote"))
        self.menuUsuario.addAction(self.actionIngresar)
        self.menuUsuario.addSeparator()
        self.menuUsuario.addAction(self.actionSalir_2)
        self.menuVenta.addAction(self.actionVentaConRemito)
        self.menuVenta.addAction(self.actionRegistrarCobroRemito)
        self.menuVenta.addAction(self.actionModificarRemito)
        self.menuVenta.addAction(self.actionBajaRemito)
        self.menuVenta.addSeparator()
        self.menuVenta.addAction(self.actionVentaContado)
        self.menuVenta.addSeparator()
        self.menuVenta.addAction(self.actionReintegroCliente)
        self.menuVenta.addSeparator()
        self.menuVenta.addAction(self.actionDevolucionDeCliente)
        self.menuMedicamento.addAction(self.actionAltaMedicamento)
        self.menuMedicamento.addSeparator()
        self.menuMedicamento.addAction(self.actionBajaMedicamento)
        self.menuMedicamento.addSeparator()
        self.menuMedicamento.addAction(self.actionModificarMedicamento)
        self.menuProducto_2.addAction(self.actionAltaProducto)
        self.menuProducto_2.addSeparator()
        self.menuProducto_2.addAction(self.actionBajaProducto)
        self.menuProducto_2.addSeparator()
        self.menuProducto_2.addAction(self.actionModificarProducto)
        self.menuProducto_2.addSeparator()
        self.menuProducto_2.addAction(self.actionFraccionarProducto)
        self.menuMonodroga.addAction(self.actionAltaMonodroga)
        self.menuMonodroga.addSeparator()
        self.menuMonodroga.addAction(self.actionBajaMonodroga)
        self.menuMonodroga.addSeparator()
        self.menuMonodroga.addAction(self.actionModificarMonodroga)
        self.menuPresentacion.addAction(self.actionAltaPresentacion)
        self.menuPresentacion.addSeparator()
        self.menuPresentacion.addAction(self.actionBajaPresentacion)
        self.menuPresentacion.addSeparator()
        self.menuPresentacion.addAction(self.actionModificarPresentacion)
        self.menuLote.addAction(self.actionAltaLote)
        self.menuLote.addSeparator()
        self.menuLote.addAction(self.actionBajaLote)
        self.menuLote.addSeparator()
        self.menuLote.addAction(self.actionModificarLote)
        self.menuProducto.addAction(self.menuProducto_2.menuAction())
        self.menuProducto.addSeparator()
        self.menuProducto.addAction(self.menuMedicamento.menuAction())
        self.menuProducto.addSeparator()
        self.menuProducto.addAction(self.menuMonodroga.menuAction())
        self.menuProducto.addSeparator()
        self.menuProducto.addAction(self.menuPresentacion.menuAction())
        self.menuProducto.addSeparator()
        self.menuProducto.addAction(self.menuLote.menuAction())
        self.menuProducto.addSeparator()
        self.menuProducto.addAction(self.actionAjusteNegativoStock)
        self.menuCliente.addAction(self.actionAltaCliente)
        self.menuCliente.addSeparator()
        self.menuCliente.addAction(self.actionBajaCliente)
        self.menuCliente.addSeparator()
        self.menuCliente.addAction(self.actionModificarCliente)
        self.menuListar.addAction(self.actionListar)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addSeparator()
        self.menuAyuda.addAction(self.actionAcercaDe)
        self.menubar.addAction(self.menuUsuario.menuAction())
        self.menubar.addAction(self.menuVenta.menuAction())
        self.menubar.addAction(self.menuProducto.menuAction())
        self.menubar.addAction(self.menuCliente.menuAction())
        self.menubar.addAction(self.menuListar.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(vtnPrincipal)
        QtCore.QMetaObject.connectSlotsByName(vtnPrincipal)

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(_translate("vtnPrincipal", "Crisol", None))
        self.menuUsuario.setTitle(_translate("vtnPrincipal", "Usuario", None))
        self.menuVenta.setTitle(_translate("vtnPrincipal", "Venta", None))
        self.menuProducto.setTitle(_translate("vtnPrincipal", "Producto", None))
        self.menuMedicamento.setTitle(_translate("vtnPrincipal", "Medicamento", None))
        self.menuProducto_2.setTitle(_translate("vtnPrincipal", "Producto", None))
        self.menuMonodroga.setTitle(_translate("vtnPrincipal", "Monodroga", None))
        self.menuPresentacion.setTitle(_translate("vtnPrincipal", "Presentación", None))
        self.menuLote.setTitle(_translate("vtnPrincipal", "Lote", None))
        self.menuCliente.setTitle(_translate("vtnPrincipal", "Cliente", None))
        self.menuListar.setTitle(_translate("vtnPrincipal", "Listar", None))
        self.menuAyuda.setTitle(_translate("vtnPrincipal", "Ayuda", None))
        self.actionIngresar.setText(_translate("vtnPrincipal", "Ingresar", None))
        self.actionIngresar.setStatusTip(_translate("vtnPrincipal", "Ingresar Usuario y Contraseña", None))
        self.actionIngresar.setShortcut(_translate("vtnPrincipal", "Ctrl+I", None))
        self.actionSalir.setText(_translate("vtnPrincipal", "Salir", None))
        self.actionSalir_2.setText(_translate("vtnPrincipal", "Salir", None))
        self.actionSalir_2.setStatusTip(_translate("vtnPrincipal", "Cerrar Aplicación", None))
        self.actionSalir_2.setShortcut(_translate("vtnPrincipal", "Ctrl+Q", None))
        self.actionVentaConRemito.setText(_translate("vtnPrincipal", "Venta con Remito", None))
        self.actionVentaContado.setText(_translate("vtnPrincipal", "Venta Contado", None))
        self.actionModificarRemito.setText(_translate("vtnPrincipal", "Modificar Remito", None))
        self.actionBajaRemito.setText(_translate("vtnPrincipal", "Baja Remito", None))
        self.actionRegistrarCobroRemito.setText(_translate("vtnPrincipal", "Registrar Cobro Remito", None))
        self.actionReintegroCliente.setText(_translate("vtnPrincipal", "Reintegro Cliente", None))
        self.actionDevolucionDeCliente.setText(_translate("vtnPrincipal", "Devolución Cliente", None))
        self.actionBaja_Producto.setText(_translate("vtnPrincipal", "Baja Producto", None))
        self.actionModificar_Producto.setText(_translate("vtnPrincipal", "Modificar Producto", None))
        self.actionBaja_Medicamento.setText(_translate("vtnPrincipal", "Baja Medicamento", None))
        self.actionModificar_Medicamento.setText(_translate("vtnPrincipal", "Modificar Medicamento", None))
        self.actionBaja_Monodroga.setText(_translate("vtnPrincipal", "Baja Monodroga", None))
        self.actionModificar_Monodroga.setText(_translate("vtnPrincipal", "Modificar Monodroga", None))
        self.actionBaja_Presentaci_n.setText(_translate("vtnPrincipal", "Baja Presentación", None))
        self.actionAltaProducto.setText(_translate("vtnPrincipal", "Alta", None))
        self.actionBajaProducto.setText(_translate("vtnPrincipal", "Baja", None))
        self.actionModificarProducto.setText(_translate("vtnPrincipal", "Modificar", None))
        self.actionAltaMedicamento.setText(_translate("vtnPrincipal", "Alta", None))
        self.actionBajaMedicamento.setText(_translate("vtnPrincipal", "Baja", None))
        self.actionModificarMedicamento.setText(_translate("vtnPrincipal", "Modificar", None))
        self.actionAltaMonodroga.setText(_translate("vtnPrincipal", "Alta", None))
        self.actionBajaMonodroga.setText(_translate("vtnPrincipal", "Baja", None))
        self.actionModificarMonodroga.setText(_translate("vtnPrincipal", "Modificar", None))
        self.actionAltaPresentacion.setText(_translate("vtnPrincipal", "Alta", None))
        self.actionBajaPresentacion.setText(_translate("vtnPrincipal", "Baja", None))
        self.actionModificarPresentacion.setText(_translate("vtnPrincipal", "Modificar", None))
        self.actionBajaLote.setText(_translate("vtnPrincipal", "Baja", None))
        self.actionModificarLote.setText(_translate("vtnPrincipal", "Modificar", None))
        self.actionFraccionarProducto.setText(_translate("vtnPrincipal", "Fraccionar", None))
        self.actionAltaCliente.setText(_translate("vtnPrincipal", "Alta", None))
        self.actionBajaCliente.setText(_translate("vtnPrincipal", "Baja", None))
        self.actionModificarCliente.setText(_translate("vtnPrincipal", "Modificar", None))
        self.actionAjusteNegativoStock.setText(_translate("vtnPrincipal", "Ajuste Negativo Stock", None))
        self.actionListar.setText(_translate("vtnPrincipal", "Generar Listado", None))
        self.actionAyuda.setText(_translate("vtnPrincipal", "Ayuda", None))
        self.actionAcercaDe.setText(_translate("vtnPrincipal", "Acerca de ...", None))
        self.actionAltaLote.setText(_translate("vtnPrincipal", "Alta", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    vtnPrincipal = QtGui.QMainWindow()
    ui = Ui_vtnPrincipal()
    ui.setupUi(vtnPrincipal)
    vtnPrincipal.show()
    sys.exit(app.exec_())

