from datetime import datetime

fechas_str = ["2024-01-15", "2024-03-22", "2024-02-08", "2024-04-01"]
hoy = datetime.now()

# Convertir strings a datetime
fechas = [datetime.strptime(f, "%Y-%m-%d")for f in fechas_str]

# Calcular días desde cada fecha hasta hoy
for i, fecha in enumerate(fechas):
    dias = (hoy - fecha).days
    print(f"{fechas_str[i]} → hace {dias} días")

# Encontrar la más reciente
mas_reciente = max(fechas)
print(f"\nMás reciente: {mas_reciente.strftime('%Y-%m-%d')}")