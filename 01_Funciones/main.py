from simulador_ahorro import simular_ahorros
from numero_secreto import adivinar_numero
from multiplicar import multiplicar_numero
from contrasena import contrasena
from contador_vocales import contador_vocales
from mini_cajero import mini_cajero
from media_notas import media_notas
from acumulador_gastos import acumulador_gastos
from conversor_monedas import conversor_monedas
from validador_contrasenas import validador_contrasena
from calculadora_funciones import calculadora 


def mostrar_menu():

    print("\n--- MENÚ DE EJERCICIOS ---")
    print("1. Tabla de multiplicar")
    print("2. Contador de vocales")
    print("3. Adivina el número")
    print("4. Simulador de ahorro")
    print("5. Introduce la contraseña")
    print("6. Mini Cajero")
    print("7. Media notas")
    print("8. Acumulador de Gastos")
    print("9. Conversor de monedas")
    print("10. Validador Contraseñas")
    print("11. Calculadora")

    print("0. Salir")

while True:

    mostrar_menu()

    opcion = input("Selecciona una opción: ")

    if opcion == "1":

        multiplicar_numero()

    elif opcion == "2":

        contador_vocales()

    elif opcion == "3":

        adivinar_numero()

    elif opcion == "4":

        simular_ahorros()

    elif opcion == "5":
        
        contrasena()

    elif opcion == "6":
        
        mini_cajero()
    
    elif opcion == "7":
        
        media_notas()
    
    elif opcion == "8":
        
        acumulador_gastos()
    
    elif opcion == "9":
        
        conversor_monedas()

    elif opcion == "10":
        
        validador_contrasena()
    elif opcion == "11":
        
        calculadora()

    elif opcion == "0":

        print("Programa finalizado.")

        break

    else:

        print("Opción incorrecta.")