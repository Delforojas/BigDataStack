# Ejercicios de funciones en Python

Este directorio contiene varios ejercicios desarrollados para practicar el uso de funciones en Python.

Cada ejercicio está separado en su propio archivo para mantener el código organizado y facilitar su reutilización.

El archivo `main.py` funciona como punto de entrada principal del programa. Desde él se importan las funciones de los distintos módulos y se muestran mediante un menú interactivo controlado por un bucle `while`.

## Conceptos trabajados

- Creación de funciones con `def`
- Parámetros y argumentos
- Valores de retorno con `return`
- Importación de funciones entre archivos
- Organización del código en módulos
- Bucles `while`
- Menús interactivos
- Condicionales `if`, `elif` y `else`
- Validación de datos
- Contadores y acumuladores

## Estructura del proyecto

```text
Funciones/
│
├── main.py
├── acumulador_gastos.py
├── calculadora_funciones.py
├── contador_vocales.py
├── contrasena.py
├── conversor_monedas.py
├── Funciones_teoria.py
├── media_notas.py
├── mini_cajero.py
├── multiplicar.py
├── numero_secreto.py
├── simulador_ahorro.py
└── validador_contrasenas.py
```

## Ejercicios incluidos

### Acumulador de gastos

Permite introducir varios gastos y calcular el importe total acumulado.

### Calculadora con funciones

Realiza operaciones básicas:

- Suma
- Resta
- Multiplicación
- División

También controla la división entre cero.

### Contador de vocales

Recorre una frase y cuenta cuántas veces aparece cada vocal.

### Comprobación de contraseña

Solicita una contraseña al usuario y limita el número de intentos disponibles.

### Conversor de monedas

Convierte una cantidad en euros a diferentes monedas mediante funciones independientes.

### Media de notas

Solicita varias notas, calcula la suma total y obtiene la media.

### Mini cajero

Simula operaciones básicas de un cajero, como consultar saldo, ingresar o retirar dinero.

### Tabla de multiplicar

Muestra la tabla de multiplicar del número introducido por el usuario.

### Número secreto

El usuario intenta adivinar un número secreto utilizando un número limitado de intentos.

### Simulador de ahorro

Calcula cuántos meses son necesarios para alcanzar un objetivo de ahorro.

### Validador de contraseñas

Comprueba si una contraseña cumple diferentes requisitos de seguridad, como:

- Longitud mínima
- Presencia de números
- Presencia de letras mayúsculas

## Funcionamiento de `main.py`

El archivo `main.py` importa las funciones de los distintos módulos y muestra un menú principal.

El menú se mantiene activo mediante un bucle `while` hasta que el usuario selecciona la opción de salir.

Ejemplo simplificado:

```python
while True:
    mostrar_menu()

    opcion = input("Elige una opción: ")

    if opcion == "1":
        ejecutar_acumulador_gastos()

    elif opcion == "2":
        ejecutar_calculadora()

    elif opcion == "3":
        ejecutar_contador_vocales()

    elif opcion == "0":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida.")
```

Gracias al bucle `while`, el usuario puede ejecutar varios ejercicios sin tener que reiniciar manualmente el programa.

## Ejecución

Para iniciar el menú principal:

```bash
python main.py
```

## Objetivo

El objetivo de este proyecto es aprender a dividir un programa en funciones y módulos, evitando escribir todo el código en un único archivo.

Esta estructura permite crear programas más organizados, legibles y fáciles de mantener.