ventas_por_dia = {
    "lunes": 1250.00,
    "martes": 980.50,
    "miércoles": 1430.20,
    "jueves": 890.00,
    "viernes": 1560.80,
}

print(ventas_por_dia.values())

# Construye el reporte
reporte = {
    "total_ventas": sum ( ventas_por_dia.values()),
    "num_dias": len( ventas_por_dia),
    "promedio_diario":sum(ventas_por_dia.values()) / len ( ventas_por_dia),
    "mejor_dia": max( ventas_por_dia),
    "peor_dia": min( ventas_por_dia),
}

print("REPORTE SEMANAL")
for clave, valor in reporte.items():
    print(f"  {clave}: {valor}")