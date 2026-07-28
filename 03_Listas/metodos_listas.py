productos_stock = ["laptop", "monitor", "teclado", "ratón"]

# Añadir elementos
productos_stock.append("webcam")           # Añade al final
productos_stock.insert(0, "servidor") 
productos_stock.insert(2, "22222")

# Longitud
print(f"Productos en stock: {len(productos_stock)}")
print(productos_stock)


productos_stock.remove("ratón")
eliminado = productos_stock.pop()

print(eliminado)



# Ordenar
precios = [299.99, 49.99, 899.00, 129.50, 1499.00]
precios.sort()                  # Ordena la lista original (in-place)
precios_desc = sorted(precios, reverse=True)

print(precios)
print(precios_desc)