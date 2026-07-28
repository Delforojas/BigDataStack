# Ejercicios de diccionarios en Python

Esta carpeta contiene ejercicios desarrollados para practicar el uso de diccionarios en Python.

Los ejercicios utilizan ejemplos relacionados con clientes, productos y ventas para representar situaciones similares a las que pueden aparecer en aplicaciones reales y procesos de análisis de datos.

## Conceptos trabajados

- Creación de diccionarios
- Acceso a valores mediante claves
- Uso del método `get()`
- Añadir y modificar pares clave-valor
- Eliminar elementos
- Métodos `keys()`, `values()` e `items()`
- Actualización mediante `update()`
- Copias de diccionarios con `copy()`
- Recorrido de diccionarios
- Listas de diccionarios
- Cálculo y enriquecimiento de registros
- Agrupación de datos
- Filtrado mediante list comprehensions
- Funciones `sum()`, `len()`, `max()` y `min()`
- Conteo de elementos mediante `Counter`
- Creación de reportes

## Estructura

```text
Diccionarios/
│
├── README.md
├── diccionario_basico.py
├── metodos_diccionarios.py
├── enriquecer_registros.py
├── filtrar_ventas.py
├── agrupar_por_categoria.py
├── agrupar_ventas_producto.py
└── dashboard_ventas.py
```

## Archivos

### `diccionario_basico.py`

Contiene un registro individual de una venta representado mediante un diccionario.

Se practican las siguientes operaciones:

- acceder a valores mediante claves;
- consultar claves opcionales con `get()`;
- añadir nuevos campos;
- calcular el precio total de una venta;
- mostrar cantidades con formato monetario.

### `metodos_diccionarios.py`

Contiene ejercicios relacionados con los principales métodos de los diccionarios:

- `keys()`;
- `values()`;
- `items()`;
- `update()`;
- `copy()`.

También se practican la actualización y eliminación de datos de un cliente.

### `enriquecer_registros.py`

Trabaja con una lista de ventas representadas mediante diccionarios.

Para cada venta se calculan y añaden nuevos campos:

- importe total;
- categoría de la operación según su importe.

Este ejercicio simula un proceso básico de transformación y enriquecimiento de datos.

### `filtrar_ventas.py`

Filtra las ventas que superan un determinado importe.

También calcula:

- el número de ventas seleccionadas;
- el importe total de las ventas;
- los clientes incluidos en el resultado.

Se utilizan listas de diccionarios, list comprehensions y la función `sum()`.

### `agrupar_por_categoria.py`

Agrupa productos según su categoría.

El resultado es un diccionario en el que cada categoría contiene los nombres de los productos asociados.

Este ejercicio permite practicar la creación dinámica de claves y listas dentro de un diccionario.

### `agrupar_ventas_producto.py`

Analiza una lista de ventas y realiza varias operaciones:

- filtrado de ventas por importe;
- extracción de valores;
- cálculo del total;
- conteo de ventas por producto.

Para realizar el conteo se utiliza `Counter` del módulo `collections`.

### `dashboard_ventas.py`

Construye un reporte semanal a partir de un diccionario de ventas diarias.

El reporte incluye:

- ventas totales;
- número de días registrados;
- promedio diario;
- día con mayor cantidad de ventas;
- día con menor cantidad de ventas.

Este ejercicio combina diccionarios con funciones de agregación y generación de reportes.

## Ejecución

Cada ejercicio puede ejecutarse de forma independiente desde la terminal:

```bash
python diccionario_basico.py
```

```bash
python metodos_diccionarios.py
```

```bash
python enriquecer_registros.py
```

```bash
python filtrar_ventas.py
```

```bash
python agrupar_por_categoria.py
```

```bash
python agrupar_ventas_producto.py
```

```bash
python dashboard_ventas.py
```

## Objetivo

El objetivo de estos ejercicios es aprender a almacenar, consultar, modificar, filtrar, agrupar y transformar datos mediante diccionarios de Python.

También se busca comprender cómo combinar diccionarios y listas para representar colecciones de registros similares a tablas de una base de datos.
