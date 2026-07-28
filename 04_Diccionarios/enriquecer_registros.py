ventas = [
    {"producto": "USB", "precio_unitario": 12.99, "cantidad": 3},
    {"producto": "Monitor", "precio_unitario": 349.99, "cantidad": 1},
    {"producto": "Laptop", "precio_unitario": 899.00, "cantidad": 2},
    {"producto": "Cable", "precio_unitario": 8.50, "cantidad": 10},
]

for venta in ventas:
    # Calcula el total
    venta["total"] =  venta["precio_unitario"] * venta["cantidad"]
    
    if venta["total"] < 100:
        venta["categoria_importe"] = "pequeña"
    elif venta["total"] <= 500:
        venta["categoria_importe"] = "mediana"
    else:
        venta["categoria_importe"] = "grande"


for v in ventas:
    print(f"{v['producto']}: {v['total']:.2f}€ ({v['categoria_importe']})")