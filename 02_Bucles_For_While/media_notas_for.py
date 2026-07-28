#Media notas 

notas = [7.5, 4.2, 9.0, 3.8, 6.1, 8.4, 5.0]
aprobados = 0
suspensos = 0

for nota in notas:
    if nota >= 5:
        aprobados = aprobados + 1
    else:
        suspensos = suspensos + 1

print(f"Aprobados: {aprobados}, Suspensos: {suspensos}")
