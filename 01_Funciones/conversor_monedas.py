# Conversor de monedas
# Tasas de cambio
def conversor_monedas():
   TASA_DOLAR = 1.08
   TASA_LIBRA = 0.86
   TASA_YEN = 161

   def dollares(euros):
      dolares = euros * TASA_DOLAR
      print (f"{euros:.0f} euros son {dolares:.2f} dolares")

   def libras(euros):
      libras = euros * TASA_LIBRA
      print (f"{euros:.0f} euros son {libras:.2f} libras")

   def yenes(euros):
      yenes = euros * TASA_YEN
      print (f"{euros:.0f} euros son {yenes:.2f} yenes")


   def mostrar_menu():

      print("\n--- MENÚ DE EJERCICIOS ---")
      print("1. Convertir a Dolares")
      print("2. Convertir a Libras")
      print("3. Converir a yenes ")
      print("0. Salir")

   while True:
      
      mostrar_menu()

      opcion= input("Selecciona una opcion: ")

      if opcion == "1":
         euros = float(input("Cantidad en euros: "))
         dollares(euros)

      elif opcion == "2":
         euros = float(input("Cantidad en euros: "))
         libras(euros)

      elif opcion == "3":
         euros = float(input("Cantidad en euros: "))
         yenes(euros)  
      
      elif opcion == "0":
            print ("Programa Finalizado")
            break 
      



