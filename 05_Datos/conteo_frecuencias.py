from collections import Counter

acciones = [
    "login", "ver_producto", "ver_producto", "añadir_carrito",
    "login", "ver_producto", "comprar", "login", "ver_producto",
    "añadir_carrito", "ver_producto", "login", "comprar",
    "ver_producto", "añadir_carrito", "login", "logout",
]

# Contar frecuencias
conteo = Counter(acciones)
print(f" el conteo es {conteo}")
total_acciones = sum(conteo.values())
print(f"el numero {total_acciones}")

# Top 3 acciones más frecuentes
top_3 = conteo.most_common(3)

print("Top 3 acciones:")
for accion, frecuencia in top_3:
    porcentaje = (frecuencia / total_acciones) * 100
    print(f"  {accion}: {frecuencia} veces ({porcentaje:.1f}%)")