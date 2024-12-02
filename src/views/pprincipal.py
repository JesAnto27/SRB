from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QPixmap
from PyQt6 import uic
from views.client_view import ClientView  # Importamos la vista de clientes

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("src/views/pprincipal.ui", self)  # Carga el diseño de pprincipal.ui

        # Conectar botones a sus respectivas acciones
        self.btnUsuarios2.clicked.connect(self.mostrar_usuarios)
        self.btnSalir.clicked.connect(self.cerrar_sesion)

        # Nuevo botón para gestionar clientes
        self.btnClientes.clicked.connect(self.mostrar_clientes)

    def mostrar_usuarios(self):
        """
        Cambia a la página de Usuarios en el QStackedWidget
        """
        self.stackedWidget.setCurrentWidget(self.page)  # Cambia a la página de Usuarios

    def mostrar_clientes(self):
        """
        Abre la ventana de gestión de clientes
        """
        self.client_view = ClientView()  # Crea una nueva instancia de la vista de clientes
        self.client_view.show()  # Muestra la ventana de clientes

    def cerrar_sesion(self):
        """
        Cierra la ventana principal y vuelve al login.
        """
        self.close()  # Cerrar la ventana principal

        # Reabrir el formulario de login
        from src.views.login import Login
        self.login = Login()
        self.login.show()

