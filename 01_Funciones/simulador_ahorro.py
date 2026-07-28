# Simulador de ahorro mensual
def simular_ahorros ():
    objetivo = float(input("¿Cuánto necesitas ahorrar? (€): "))
    ahorro_mensual = float(input("¿Cuánto puedes ahorrar al mes? (€): "))
    
    porcentaje= 0
    ahorrado = 0
    meses = 0


    while ahorrado < objetivo :
        ahorrado = ahorrado + ahorro_mensual
        porcentaje = (ahorrado / objetivo) * 100
        
        meses +=1 
      
            
        print (f"Te quedan {objetivo - ahorrado} para llegar a tu objetivo")
        print (f"Con esa cantidad podras alcanzar tu objetivo en {objetivo/ahorrado:.2f} meses")
        print (f"Llevas {meses:.2f} meses ahorrando , nos vemos el proximo mes")
      
      
    if objetivo <= ahorrado :
        print(f"Has alcanzado tu objetivo. Ahorraste {ahorrado} € en {meses:.2f} meses.")
        print(f"Te sobran {ahorrado - objetivo} euros.")



