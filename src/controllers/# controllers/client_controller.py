from models.client_model import create_client, get_client_by_email, update_client, delete_client

def add_client(nombre, apellido_paterno, email, telefono):
    create_client(nombre, apellido_paterno, email, telefono)

def find_client_by_email(email):
    return get_client_by_email(email)

def edit_client(id, nombre, apellido_paterno, email, telefono):
    update_client(id, nombre, apellido_paterno, email, telefono)

def remove_client(id):
    delete_client(id)
