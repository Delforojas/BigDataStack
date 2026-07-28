# Tenemos precios sin IVA

precios_sin_iva = [100, 250, 49.99, 899, 1299.50]

precios_con_iva = []

for precio in precios_sin_iva:

    precios_con_iva.append(precio * 1.21)

ordenado  = sorted(precios_con_iva)

print (ordenado)


precios_con_iva =[precio * 1.21 for precio in precios_sin_iva]
print (precios_con_iva)

caros = [ p for p in precios_con_iva if p > 200]
print (caros)

redondeados = [ round(p,2) for p in precios_con_iva]
print(redondeados)