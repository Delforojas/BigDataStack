# PROYECTO: Gestor de Gastos Personales
gastos = []

def agregar_gasto(gastos):
    """Pide datos al usuario y añade un gasto a la lista."""
    print("")
    concepto = input("  ¿Qué compraste? ")
    cantidad = float(input("  ¿Cuánto costó? (€): "))
    print("  Categorías: comida, transporte, ocio, hogar, otros")
    categoria = input("  Categoría: ").lower()

    gasto = {
        "concepto": concepto,
        "cantidad": cantidad,
        "categoria": categoria
    }
    gastos.append(gasto)  # Añadir a la lista
    print(f"  ✓ Gasto registrado: {concepto} ({cantidad:.2f}€)")


def ver_gastos(gastos):
    """Muestra todos los gastos registrados."""
    if len(gastos) == 0:
        print("  No hay gastos registrados todavía.")
        return

    print("")
    print(f"  {'#':<4}{'Concepto':<20}{'Cantidad':<12}{'Categoría'}")
    print("  " + "-" * 50)

    total = 0
    for i in range(len(gastos)):
        g = gastos[i]
        print(f"  {i+1:<4}{g['concepto']:<20}{g['cantidad']:<12.2f}{g['categoria']}")
        total = total + g["cantidad"]

    print("  " + "-" * 50)
    print(f"  TOTAL: {total:.2f}€ ({len(gastos)} gastos)")

def resumen_categorias(gastos):
    """Muestra el total gastado por categoría."""
    if len(gastos) == 0:
        print("  No hay gastos registrados.")
        return

    # Acumular por categoría
    categorias = {}
    for gasto in gastos:
        cat = gasto["categoria"]
        if cat in categorias:
            categorias[cat] = categorias[cat] + gasto["cantidad"]
        else:
            categorias[cat] = gasto["cantidad"]

    # Mostrar resumen
    print("")
    print("  === RESUMEN POR CATEGORÍA ===")
    total_general = 0
    for cat in categorias:
        total_cat = categorias[cat]
        total_general = total_general + total_cat
        print(f"  {cat:<15} {total_cat:>8.2f}€")

    print(f"  {'TOTAL':<15} {total_general:>8.2f}€")


def buscar_gastos(gastos):
    """Busca gastos por categoría o por importe mínimo."""
    print("  Buscar por: (1) categoría  (2) importe mínimo")
    tipo = input("  Opción: ")

    encontrados = []
    if tipo == "1":
        cat = input("  ¿Qué categoría? ").lower()
        for gasto in gastos:
            if gasto["categoria"] == cat:
                encontrados.append(gasto)
    elif tipo == "2":
        minimo = float(input("  ¿Importe mínimo? (€): "))
        for gasto in gastos:
            if gasto["cantidad"] >= minimo:
                encontrados.append(gasto)

    if len(encontrados) == 0:
        print("  No se encontraron gastos con esos criterios.")
    else:
        print(f"  Encontrados: {len(encontrados)} gastos")
        for g in encontrados:
            print(f"    - {g['concepto']}: {g['cantidad']:.2f}€ ({g['categoria']})")




def mostrar_menu ():
  print("\n--- Gestor de Gastos ---") 
  print("1. Agregar Gastos")
  print("2. Ver Gastos")
  print("3. Resumen categorias")
  print("4. Buscar Gastos")
  print("0. Salir ")


while True:
  mostrar_menu()

  opcion= input("Selecciona una opcion: ")

  if opcion == "1":
    agregar_gasto()

  elif opcion == "2":
    ver_gastos()
  
  elif opcion == "3":
    resumen_categorias()

  elif opcion == "0":
    print("Programa finalizado")
    break 