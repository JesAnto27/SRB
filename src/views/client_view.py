# views/client_view.py
from PyQt6 import QtWidgets
from controllers.client_controller import add_client, find_client_by_email, edit_client, remove_client

class ClientView(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Gestión de Clientes')

        # Elementos de la interfaz (Campos de texto, botones, etc.)
        self.nombre_input = QtWidgets.QLineEdit(self)
        self.apellido_input = QtWidgets.QLineEdit(self)
        self.email_input = QtWidgets.QLineEdit(self)
        self.telefono_input = QtWidgets.QLineEdit(self)

        self.add_button = QtWidgets.QPushButton('Agregar Cliente', self)
        self.edit_button = QtWidgets.QPushButton('Editar Cliente', self)
        self.delete_button = QtWidgets.QPushButton('Eliminar Cliente', self)

        # Conectar botones a métodos
        self.add_button.clicked.connect(self.add_client)
        self.edit_button.clicked.connect(self.edit_client)
        self.delete_button.clicked.connect(self.delete_client)

        # Layout y disposición de los elementos
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.nombre_input)
        layout.addWidget(self.apellido_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.telefono_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

    def add_client(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        email = self.email_input.text()
        telefono = self.telefono_input.text()
        add_client(nombre, apellido, email, telefono)

    def edit_client(self):
        email = self.email_input.text()
        client = find_client_by_email(email)
        if client:
            nombre = self.nombre_input.text()
            apellido = self.apellido_input.text()
            telefono = self.telefono_input.text()
            edit_client(client[0], nombre, apellido, email, telefono)

    def delete_client(self):
        email = self.email_input.text()
        client = find_client_by_email(email)
        if client:
            remove_client(client[0])
