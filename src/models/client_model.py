# models/client_model.py
import pymysql
from database.connection import get_db_connection

def create_client(nombre, apellido_paterno, email, telefono):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO clientes (nombre, apellido_paterno, email, telefono)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (nombre, apellido_paterno, email, telefono))
    connection.commit()
    cursor.close()
    connection.close()

def get_client_by_email(email):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "SELECT * FROM clientes WHERE email = %s"
    cursor.execute(query, (email,))
    client = cursor.fetchone()
    cursor.close()
    connection.close()
    return client

def update_client(id, nombre, apellido_paterno, email, telefono):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        UPDATE clientes 
        SET nombre = %s, apellido_paterno = %s, email = %s, telefono = %s
        WHERE id = %s
    """
    cursor.execute(query, (nombre, apellido_paterno, email, telefono, id))
    connection.commit()
    cursor.close()
    connection.close()

def delete_client(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = "DELETE FROM clientes WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
