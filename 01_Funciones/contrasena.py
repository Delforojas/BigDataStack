def contrasena ():
    password_correcta = "123"
    intentos = 0

    password = input("Introduce la contraseña: ")

    while password != password_correcta:
        intentos = intentos + 1
        if intentos >= 3:
            print("¡Demasiados intentos! Cuenta bloqueada.")
            break  # 'break' sale del bucle inmediatamente
        print(f"Incorrecta. Te quedan {3 - intentos} intentos.")
        password = input("Introduce la contraseña: ")
      
    if password == password_correcta:
        print("¡Acceso concedido! Bienvenido.")


