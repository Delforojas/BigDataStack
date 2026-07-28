ventas_mes = [
    {"cliente": "Ana", "importe": 320.00},
    {"cliente": "Luis", "importe": 890.50},
    {"cliente": "María", "importe": 150.00},
    {"cliente": "Pedro", "importe": 1200.00},
    {"cliente": "Sara", "importe": 45.99},
    {"cliente": "Jorge", "importe": 670.00},
]

# Filtra ventas mayores a 500€ usando list comprehension
ventas_vip =[ v for v in ventas_mes if v["importe"] > 500]
print(len(ventas_vip))

# Calcula el total de ventas VIP
total_vip = sum([v["importe"]for v in ventas_vip])
print(total_vip)

print("Clientes VIP (>500€):")

for venta in ventas_vip :
  print ({venta["cliente"]})
print(f"\nTotal VIP: {total_vip:.2f}€")
