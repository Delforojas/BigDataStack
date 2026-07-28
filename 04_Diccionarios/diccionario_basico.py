# Un registro de venta como diccionario
venta = {
    "id": "VNT-2024-001",
    "fecha": "2024-01-15",
    "cliente": "María García",
    "producto": "Monitor 4K",
    "cantidad": 2,
    "precio_unitario": 349.99,
    "impuesto": 0.21,
    #"descuento":222
}

# Acceder a valores por clave
print(venta["producto"])
print(venta["cantidad"])
print(venta["precio_unitario"])

descuento = venta.get("descuento", 0)  # 0 si no existe
print(f"Descuento: {descuento}")

venta["total"] = venta["cantidad"] * venta["precio_unitario"] * (1 + venta["impuesto"])

print(f"Total: {venta['total']:.2f}€")