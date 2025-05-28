import db
from db import ver_contactos

def menu():
    print("\nAGENDA DE CONTACTOS")
    print("1. Agregar contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Eliminar contacto")
    print("6. Salir")

def mostrar_contactos():
                contactos = ver_contactos()
                if contactos:
                    for c in contactos:
                        print(f"ID: {c[0]} | Nombre: {c[1]} | Teléfono: {c[2]} | Email: {c[3]}")
                else:
                    print("No hay contactos guardados.")

if __name__ == "__main__":
    db.crear_db()
   

    while True:
        menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            try:
                print("Agregar contacto")
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                db.agregar_contacto(nombre, telefono, email)
            except Exception as e:
                print("Error al agregar contacto:", e)
                continue

        elif opcion == "2":
            mostrar_contactos()
        elif opcion == "3":
                try:
                    print("Buscar contacto")
                    id_buscar = input("ID del contacto a buscar: ")
                    contacto = db.buscar_contacto(id_buscar)
                    if contacto:
                        print(f"ID: {contacto[0]} | Nombre: {contacto[1]} | Teléfono: {contacto[2]} | Email: {contacto[3]}")
                    else:
                        print("No se encontró el contacto.")
                except Exception as e:
                    print("Error al buscar contacto:", e)
                    continue
        elif opcion == "4":
                try:
                    print("Editar contacto")
                    id_editar = input("ID del contacto a editar: ")
                    nombre = input("Nuevo nombre: ")
                    telefono = input("Nuevo teléfono: ")
                    email = input("Nuevo email: ")
                    db.actualizar_contacto(id_editar, nombre, telefono, email)
                except Exception as e:
                    print("Error al editar contacto:", e)
                    continue
        elif opcion == "5":
                try:
                    print("Eliminar contacto")
                    id_eliminar = input("ID del contacto a eliminar: ")
                    db.eliminar_contacto(id_eliminar)
                except Exception as e:
                    print("Error al eliminar contacto:", e)
                    continue
        

        elif opcion == "6":
            print("¡Hasta luego!")
            break
        # Aquí irán las funciones como agregar, ver, buscar...
