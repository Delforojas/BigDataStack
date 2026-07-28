with open("datos_ejemplo.txt", "w", encoding="utf-8") as f:
    f.write("producto,cantidad,precio\n")
    f.write("Laptop,5,1299.99\n")
    f.write("Monitor,12,349.50\n")
    f.write("Teclado,30,79.99\n")

print("Archivo creado.")

# Leer el archivo completo
with open("datos_ejemplo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
print(contenido)

# Leer línea por línea (mejor para archivos grandes)
with open("datos_ejemplo.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())