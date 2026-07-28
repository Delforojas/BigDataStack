productos = [
    {"nombre": "Laptop", "categoria": "electrónica", "precio": 1299},
    {"nombre": "Camiseta", "categoria": "ropa", "precio": 25},
    {"nombre": "Monitor", "categoria": "electrónica", "precio": 399},
    {"nombre": "Pantalón", "categoria": "ropa", "precio": 55},
    {"nombre": "Teclado", "categoria": "electrónica", "precio": 89},
    {"nombre": "Zapatos", "categoria": "ropa", "precio": 120},
]


por_categorias = {}

for g in productos:
  cat = g["categoria"]
  if cat in por_categorias:
    por_categorias[cat] += 1
  else:
    por_categorias[cat] = 1

# Muestra el resultado
for cat, prods in por_categorias.items():
    nombres = [p["nombre"] for p in productos if p["categoria"] == cat]
    print(f"{cat}: {nombres}")