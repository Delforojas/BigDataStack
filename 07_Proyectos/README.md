# Gestor de gastos personales

Aplicación de consola desarrollada en Python para registrar, consultar y analizar gastos personales.

Los gastos se almacenan temporalmente en memoria mediante una lista de diccionarios. Cada gasto contiene un concepto, una cantidad y una categoría.

## Funcionalidades

- Añadir nuevos gastos
- Mostrar todos los gastos registrados
- Calcular el importe total
- Crear un resumen por categoría
- Buscar gastos por categoría
- Buscar gastos por importe mínimo
- Mostrar un menú interactivo
- Validar las opciones introducidas

## Conceptos utilizados

- Funciones
- Listas
- Diccionarios
- Bucles `while`
- Bucles `for`
- Condicionales
- Parámetros
- Contadores y acumuladores
- Formateo de cadenas con f-strings
- Búsqueda y filtrado de datos

## Estructura de los datos

Cada gasto se representa mediante un diccionario:

```python
{
    "concepto": "Café",
    "cantidad": 2.50,
    "categoria": "comida"
}
```

Todos los gastos se almacenan dentro de una lista:

```python
gastos = [
    {
        "concepto": "Café",
        "cantidad": 2.50,
        "categoria": "comida"
    },
    {
        "concepto": "Metro",
        "cantidad": 1.50,
        "categoria": "transporte"
    }
]
```

## Menú principal

La aplicación muestra las siguientes opciones:

```text
1. Añadir gasto
2. Ver todos los gastos
3. Resumen por categoría
4. Buscar gastos
5. Salir
```

El menú permanece activo mediante un bucle `while` hasta que el usuario selecciona la opción de salir.

## Ejecución

Desde la carpeta del proyecto:

```bash
python gestor_gastos.py
```

## Limitaciones actuales

Los gastos se almacenan únicamente en memoria.

Al cerrar la aplicación, los datos se pierden porque todavía no existe persistencia en archivos o bases de datos.

## Posibles mejoras

- Guardar los gastos en un archivo JSON
- Cargar automáticamente los gastos al iniciar
- Editar gastos
- Eliminar gastos
- Filtrar por fecha
- Añadir presupuestos mensuales
- Exportar resultados a CSV
- Conectar la aplicación con una base de datos
- Crear una interfaz web con Django

## Objetivo

El objetivo de este proyecto es aplicar conjuntamente los fundamentos de Python en una aplicación funcional, organizada mediante funciones y estructuras de datos.