# PROYECTO: Agenda de contactos
contactos = []

def mostrar_menu():
    print("")
    print("  📱 AGENDA DE CONTACTOS")
    print("  1. Añadir contacto")
    print("  2. Buscar por nombre")
    print("  3. Listar todos")
    print("  4. Eliminar contacto")
    print("  5. Salir")




def agregar_contacto (contactos):
    nombre = input(" Nombre: ")
    telefono = input(" Teléfono: ")
    email = input(" Email: ")

    contactos.append({"nombre":nombre , "telefono":telefono , "email":email })
    print(f" {nombre} añadido a la agenda." )


def buscar_contacto (contactos):
    busqueda = input ("Buscar nombre: ").lower()
    encontrados =[]
    for c in contactos:
        if busqueda in c["nombre"].lower():
          encontrados.append(c)
    if len(encontrados)== 0:
        print(" No se encontraron contactos.")
    else:
        for c in encontrados:
            print (f"📌 {c["nombre"]  |  c["telefono"]  |  c["email"] }")
