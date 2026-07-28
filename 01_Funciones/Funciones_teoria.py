
# DEFINIR una función (escribir la receta)
def saludar(nombre):
    """Muestra un saludo personalizado."""
    print(f"¡Hola, {nombre}! Bienvenido al programa.")

# LLAMAR a la función (usar la receta)
saludar("Ana")      # ¡Hola, Ana! Bienvenido al programa.
saludar("Carlos")   # ¡Hola, Carlos! Bienvenido al programa.
saludar("María")    # ¡Hola, María! Bienvenido al programa.

def calcular_iva(precio, porcentaje_iva=21):
    """Calcula el precio con IVA incluido."""
    iva = precio * (porcentaje_iva / 100)
    total = precio + iva
    return total

print(calcular_iva(100))

precio_final = calcular_iva(100)
print(f"100€ + IVA = {precio_final}€")

precio_reducido = calcular_iva(100, 10)
print(f"100€ + IVA reducido = {precio_reducido}€")


