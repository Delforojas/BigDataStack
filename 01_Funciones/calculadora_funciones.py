# Calculadora con funciones

def calculadora ():
    def mostrar_resultado(resultado):
        print(resultado)
        print("Elige otra operación")

    def sumar(a, b):
        mostrar_resultado(a + b)

    def restar(a, b):
        mostrar_resultado(a - b)

    def multiplicar(a, b):
        mostrar_resultado(a * b)

    def dividir(a, b):
        if b == 0:
            print("❌ Error: no se puede dividir entre 0.")
            return
        mostrar_resultado(a / b)

    def pedir_numeros():
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        return a, b

    def mostrar_menu():
          print("\n--- Calculadora ---")
          print("1. Sumar")
          print("2. Restar")
          print("3. Multiplicar ")
          print("4. Dividir ")
          print("0. Salir")


    while True:
          
          mostrar_menu()

          opcion= input("Selecciona una opcion: ")

          if opcion == "1":
            a , b = pedir_numeros()
            sumar (a,b)
                  
          elif opcion == "2":
            a , b = pedir_numeros()
            restar (a,b)

          elif opcion == "3":
            a,b = pedir_numeros()
            multiplicar(a,b)
          
          elif opcion == "4":
            a,b = pedir_numeros()
            dividir(a,b)
          
          elif opcion == "0":
                print ("Programa Finalizado")
                break 