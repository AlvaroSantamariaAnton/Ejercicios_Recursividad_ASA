# Ejercicios de Recursividad

## Búsqueda Binaria Recursiva

Este script en Python implementa el algoritmo de búsqueda binaria de forma recursiva para encontrar un elemento en una lista ordenada.

### Uso

1. **Ejecución del Script:**
   - Ejecuta el script en un entorno de Python. Se te pedirá ingresar una lista de números ordenados y el elemento que deseas buscar en esa lista.

2. **Ingreso de Datos:**
   - Ingresa la lista de números ordenados separados por espacios cuando se te solicite.
   - Ingresa el elemento que deseas buscar en la lista.

### Ejemplo de Ejecución

```bash
$ python busqueda_binaria_recursiva.py
Ingrese la lista ordenada de números separados por espacios: 1 3 5 7 9
Ingrese el elemento que desea buscar en la lista: 5
El elemento 5 se encuentra en el índice 2.
```
### Notas

- Asegúrate de que la lista ingresada esté ordenada, de lo contrario, el script mostrará un mensaje de error.
- Si el elemento a buscar no es un número válido, el script también mostrará un mensaje de error.
- Si el elemento no se encuentra en la lista, se mostrará un mensaje indicando que no se encontró el elemento.

## Verificador de Palíndromos

Este script en Python comprueba si una o varias frases ingresadas por el usuario son palíndromas.

### Uso

1. **Ejecución del Script:**
   - Ejecuta el script en un entorno de Python. Se te pedirá ingresar una o varias frases separadas por comas.

2. **Ingreso de Datos:**
   - Ingresa una o varias frases separadas por comas cuando se te solicite.

### Ejemplo de Ejecución

```bash
$ python verificador_palindromos.py
Introduce una o varias frases separadas por coma: Anita lava la tina, A mamá Roma le aviva el amor a mamá, La ruta natural
La frase "Anita lava la tina" es un palíndromo.
La frase "A mamá Roma le aviva el amor a mamá" es un palíndromo.
La frase "La ruta natural" no es un palíndromo.
```

### Notas

- El script elimina los espacios en blanco al inicio y al final de cada frase ingresada.
- Se filtran los caracteres no alfanuméricos y se convierten todas las letras a minúsculas para realizar la verificación de palíndromos.
- Las frases que contienen solo caracteres no alfanuméricos o están vacías se consideran inválidas y se muestra un mensaje de advertencia.

## Organizador de Fichas RVB

Este script en Python organiza un conjunto de fichas en el orden Rojo-Verde-Azul (RVB) específico.

### Uso

1. **Ejecución del Script:**
   - Ejecuta el script en un entorno de Python. Se te pedirá ingresar la cantidad de fichas de cada color: rojo, verde y azul.

2. **Ingreso de Datos:**
   - Ingresa el número de fichas rojas, verdes y azules cuando se te solicite.

### Ejemplo de Ejecución

```bash
$ python organizador_fichas_rvb.py
Ingrese el número de fichas rojas: 2
Ingrese el número de fichas verdes: 3
Ingrese el número de fichas azules: 1
Fichas ordenadas: ['rojo', 'rojo', 'verde', 'verde', 'verde', 'azul']
```

### Notas

- El script organiza las fichas en el orden Rojo-Verde-Azul (RVB), donde primero se colocan todas las fichas rojas, luego las verdes y finalmente las azules.
- Si se ingresan cantidades negativas de fichas, se considerarán como cero.
- Si no se ingresa un número entero válido, el script mostrará un mensaje de error.

## Link al repositorio de GitHub

https://github.com/AlvaroSantamariaAnton/Ejercicios_Recursividad_ASA.git
