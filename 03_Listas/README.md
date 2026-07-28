# Ejercicios de listas en Python

Esta carpeta contiene ejercicios desarrollados para practicar la creación, consulta y modificación de listas en Python.

Los ejercicios están separados por temática para facilitar la lectura del código y mostrar de forma progresiva los conceptos aprendidos.

## Conceptos trabajados

- Creación de listas

- Acceso mediante índices

- Índices negativos

- Slicing

- Longitud de una lista con `len()`

- Añadir elementos con `append()` e `insert()`

- Eliminar elementos con `remove()` y `pop()`

- Ordenación con `sort()` y `sorted()`

- Recorrido de listas con bucles `for`

- List comprehensions

- Filtrado de elementos

- Redondeo de valores con `round()`

## Estructura

```text

Listas/

│

├── README.md

├── listas_basicas.py

├── metodos_listas.py

└── list_comprehensions.py

```

## Archivos

### `listas_basicas.py`

Contiene ejercicios relacionados con las operaciones fundamentales de las listas:

- creación de una lista;

- acceso mediante índices;

- acceso al último elemento con índices negativos;

- extracción de partes de una lista mediante slicing.

Como ejemplo, se utiliza una lista de ventas diarias para separar las ventas realizadas entre semana de las correspondientes al fin de semana.

### `metodos_listas.py`

Contiene ejercicios para practicar los principales métodos de las listas.

Se realizan operaciones como:

- añadir productos con `append()`;

- insertar elementos en una posición concreta con `insert()`;

- eliminar elementos con `remove()`;

- extraer elementos con `pop()`;

- consultar la cantidad de elementos con `len()`;

- ordenar listas mediante `sort()` y `sorted()`.

También se muestra la diferencia entre modificar la lista original con `sort()` y generar una nueva lista ordenada con `sorted()`.

### `list_comprehensions.py`

Contiene ejercicios de transformación y filtrado de listas.

Se comparan dos formas de generar una nueva lista:

1. Un bucle `for` tradicional.

2. Una list comprehension.

Los ejercicios incluyen:

- aplicar IVA a una lista de precios;

- redondear valores;

- ordenar resultados;

- filtrar precios superiores a una cantidad determinada.