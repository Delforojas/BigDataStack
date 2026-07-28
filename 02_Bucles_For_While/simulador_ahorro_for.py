# Simulador de ahorro mensual

objetivo = float(input("¿Cuánto necesitas ahorrar? (€): "))
ahorro_mensual = float(input("¿Cuánto puedes ahorrar al mes? (€): "))

ahorrado = 0
meses = 0


while ahorrado < objetivo :
    ahorrado = ahorrado + ahorro_mensual
    porcentaje = (ahorrado / objetivo) * 100
    meses +=1 

    if porcentaje > 100:    
        porcentaje = 100
    barra = "█" * int(porcentaje / 5) + "░" * (20 - int(porcentaje / 5))
    print(f"Mes {meses:2d}: {ahorrado:8.2f}€ [{barra}] {porcentaje:.0f}%")

    if ahorrado >= objetivo :
      break 
        
    print (f"Te quedan {objetivo - ahorrado} para llegar a tu objetivo")
    print (f"Con esa cantidad podras alcanzar tu objetivo en {objetivo/ahorrado} meses")
    print (f"Llevas {meses} meses ahorrando , nos vemos el proximo mes")

    
    
   
if objetivo <= ahorrado :
    print(f"Has alcanzado tu objetivo. Ahorraste {ahorrado} € en {meses} meses.")
    print(f"Te sobran {ahorrado - objetivo} euros.")
