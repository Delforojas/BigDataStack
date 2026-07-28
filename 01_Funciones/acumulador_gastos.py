def acumulador_gastos ():
    gastos = [12.50, 8.99, 45.00, 3.20, 22.15]

    total = 0  # El acumulador empieza en 0

    for gasto in gastos:
          total = total + gasto
          print(f"  + {gasto:.2f}€ → Acumulado: {total:.2f}€")

    print(f"Total de gastos: {total:.2f}€")



