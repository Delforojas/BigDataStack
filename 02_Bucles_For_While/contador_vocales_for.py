# Contador de vocales

frase = input("Escribe una frase: ")
frase = frase.lower()  # Convertir a minúsculas para simplificar
    # Inicializa contadores para cada vocal...
a = e = i = o = u = 0 
    # Recorre la frase letra a letra...
for letra in frase:
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            o += 1
        elif letra == "u":
            u += 1
    # Aquí ya ha terminado el for
    
if a == 1:
        print(f"La frase contiene 1 letra {a} a")
elif a > 1:
        print(f"La frase contiene letras {a} a")
    
if e == 1:
        print(f"La frase contiene 1 letra {e} e")
elif e > 0:
        print(f"La frase contiene {e} es")
    
if i == 1:
        print(f"La frase contiene {i} es")
elif i > 0:
        print(f"La frase contiene {i} ies")

if o == 1:
        print(f"La frase contiene 1 letra {o} o")
elif o > 0:
        print(f"La frase contiene {o} os")
    
if u == 1:
        print(f"La frase contiene 1 letra {u} u") 
elif u > 0:
        print(f"La frase contiene {u} us")
        