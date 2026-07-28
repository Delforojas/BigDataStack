# Manejo de archivos y datos en Python

Esta carpeta contiene ejercicios desarrollados para practicar la lectura, escritura y procesamiento de diferentes formatos de datos utilizados habitualmente en aplicaciones de Python.

Los ejemplos incluyen archivos de texto, CSV, JSON, manejo de fechas y análisis de frecuencias mediante `Counter`.

## Conceptos trabajados

- Apertura y cierre de archivos mediante `with`

- Lectura y escritura de archivos de texto

- Manejo de archivos CSV

- Uso del módulo `csv`

- Serialización y deserialización JSON

- Uso del módulo `json`

- Conversión y comparación de fechas con `datetime`

- Conteo de elementos mediante `collections.Counter`

- Recorrido de archivos línea a línea

- Formateo de datos

## Estructura

```text

Datos/

│

├── README.md

├── archivos_txt.py

├── archivos_csv.py

├── archivos_json.py

├── procesamiento_fechas.py

├── conteo_frecuencias.py

│

├── datos_ejemplo.txt

├── ventas.csv

└── resumen.json

```

## Archivos

### `archivos_txt.py`

Practica la creación y lectura de archivos de texto.

El ejercicio incluye:

- crear un archivo `.txt`;

- escribir información mediante `write()`;

- leer el archivo completo con `read()`;

- recorrer el archivo línea por línea utilizando un bucle `for`;

- eliminar espacios en blanco con `strip()`.

---

### `archivos_csv.py`

Trabaja con archivos CSV utilizando el módulo `csv`.

Se practican las siguientes operaciones:

- creación de un archivo CSV;

- escritura mediante `csv.writer`;

- lectura mediante `csv.DictReader`;

- conversión de registros a una lista de diccionarios;

- cálculo del importe total de cada venta.

---

### `archivos_json.py`

Introduce el uso del formato JSON para almacenar datos estructurados.

El ejercicio muestra cómo:

- crear un diccionario;

- guardar información mediante `json.dump()`;

- leer archivos JSON mediante `json.load()`;

- acceder posteriormente a los datos recuperados.

---

### `procesamiento_fechas.py`

Contiene ejercicios relacionados con el módulo `datetime`.

Se practican operaciones como:

- convertir cadenas de texto a objetos `datetime`;

- calcular los días transcurridos entre dos fechas;

- comparar fechas;

- localizar la fecha más reciente.

---

### `conteo_frecuencias.py`

Utiliza la clase `Counter` del módulo `collections` para analizar datos.

El ejercicio incluye:

- contar la frecuencia de aparición de distintos eventos;

- calcular el número total de acciones;

- obtener los elementos más frecuentes mediante `most_common()`;

- calcular el porcentaje que representa cada acción sobre el total.

## Archivos de ejemplo

### `datos_ejemplo.txt`

Archivo de texto utilizado para practicar lectura y escritura.

### `ventas.csv`

Archivo CSV con un conjunto de ventas utilizado durante los ejercicios.

### `resumen.json`

Archivo JSON generado automáticamente a partir de un diccionario de Python.

## Ejecución

Cada ejercicio puede ejecutarse de forma independiente:

```bash

python archivos_txt.py

```

```bash

python archivos_csv.py

```

```bash

python archivos_json.py

```

```bash

python procesamiento_fechas.py

```

```bash

python conteo_frecuencias.py

```

## Objetivo

El objetivo de estos ejercicios es aprender a trabajar con las principales fuentes de datos utilizadas en Python.

Estos conocimientos sirven como base para proyectos de análisis de datos, automatización de tareas, desarrollo web y procesamiento de información.
