"""for i in range (0,20):
  print (i)

for i in range(0,20):
  if i%2 == 0:
    print (f"pares {i}")

for i in range (0,50):
  if i%2 != 0:
    print(f"impares {i}")

suma = 0
for numero in range (0 ,100):
  suma += numero
  print (f" {suma} ")
  

palabra = input(("introduce una palabra "))
contador = 0
vocales = 0

for letra in palabra:
  contador+=1

print(contador)

vocales = ["a", "e", "i", "o", "u"]
contadorvocales = 0

for letra in palabra:  
    if letra in vocales:
      contadorvocales += 1
print (contadorvocales)

especifica= 0
buscar = input ("que letra buscas ??")

contador = 0

for letra in palabra:

    if letra == buscar:

        contador += 1

print(contador)

palabra = input("Introduce una palabra: ")

invertida = ""

for letra in palabra:

    invertida = letra + invertida

print(invertida)


invertida = ""

for letra in palabra:

    invertida = letra + invertida

if palabra == invertida:
       
      print ("es palindromo")

else:
      print(" no es palindromo")"""

numeros = [3, 8, 5, 2, 9]
"""
for n in numeros:
  print(n)
for n in numeros:
  if n%2 == 0: 
    print(f"pares {n}")

for n in numeros:
  if n%2 != 0: 
    print(f"impares {n}")

impares = 0
for n in numeros:
  if n%2 != 0: 
    impares +=1
print (f"Hay {impares}")


for n in numeros:
  m = n * 2
  print (f"{n} * 2 = {m}")

for n in numeros:
  m = n * 10
  print (f"{n} * 10 = {m}")


for n in numeros:
   if n > 5 :
     print(n)
   

cuadrados =[]
for n in numeros:
  cuadrado = n * n 
  cuadrados.append(cuadrado)
print (cuadrados)

"""


numeros = [3, 8, 5,8, 2, 9 ,8]
suma = 0

for n in numeros :
  suma += n
  media = suma / len(numeros)

print (media)


ocho = 0

for n in numeros :
  if n == 8 :
    ocho += 1
print (f"el numero 8 aparece {ocho}")

introducido = int(input ("introduce un numero"))
numero = 0

for n in numeros: 
      if n == introducido:
        numero +=1

print (numero)

for n in numeros: 
      if n == introducido:
        
        print (f"el numero {introducido} existe ")
        break 
else:
         print("no existe")


mayor = max ( numeros)
for n in numeros:
    if n == mayor :
        break 
