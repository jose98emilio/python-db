import sqlite3
import os

def crear_db():
    if not os.path.exists("contactos.db"):
        conn = sqlite3.connect("contactos.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contactos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                telefono TEXT NOT NULL,
                email TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print("Base de datos creada exitosamente")
    else:
        print("La base de datos ya existe")

def agregar_contacto(nombre, telefono, email):
    conn = sqlite3.connect("contactos.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contactos (nombre, telefono, email) VALUES (?, ?, ?)", (nombre, telefono, email))
    conn.commit()
    conn.close()
    return "Contacto guardado exitosamente"

def ver_contactos():
    conn = sqlite3.connect("contactos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    conn.close()
    return contactos

def buscar_contacto(nombre="",telefono="", email=""):
    conn = sqlite3.connect("contactos.db")
    cursor = conn.cursor()
    query="SELECT * FROM contactos WHERE 1=1"
    params = []
    if nombre:
        query += " AND nombre LIKE ?"
        params.append(f"%{nombre}%")

    if telefono:
        query += " AND telefono LIKE ?"
        params.append(f"%{telefono}%")

    if email:
        query += " AND email LIKE ?"
        params.append(f"%{email}%")
    cursor.execute(query, params)
    contacto = cursor.fetchone()
    conn.close()
    return contacto

def actualizar_contacto(id_actualizar, nombre, telefono, email):
    conn = sqlite3.connect("contactos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE contactos SET nombre=?, telefono=?, email=? WHERE id=?", (nombre, telefono, email, id_actualizar))
    conn.commit()
    conn.close()
    return "Contacto actualizado exitosamente"

def eliminar_contacto(id_eliminar):
    conn = sqlite3.connect("contactos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactos WHERE id=?", (id_eliminar,))
    conn.commit()
    conn.close()
    return "Contacto eliminado exitosamente"
