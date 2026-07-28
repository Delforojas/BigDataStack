def adivinar_numero(max_intentos):
    numero_secreto = 42
    intentos = 0

    print("=== ADIVINA EL NÚMERO ===")
    print("He pensado un número entre 1 y 100...")
    print("")
    numero  = int(input("Introduce un numero: "))

    while numero_secreto !=  numero :
        intentos = intentos + 1 
        if numero > numero_secreto   :
            print (f"Mas bajo")
        elif numero < numero_secreto :
            print (f"Mas alto")
        if intentos >= max_intentos :
            print("¡Demasiados intentos! .")
            break
        numero  = int(input("Introduce un numero: "))
    if numero_secreto == numero : 
        print (f"Has acertado! el numero que estabamos buscando es {numero_secreto}")
        print(f"Lo has conseguido en {intentos} intentos")

