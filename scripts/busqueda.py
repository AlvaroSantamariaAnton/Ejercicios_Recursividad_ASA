def busqueda_binaria_recursiva(arr, objetivo, inicio=0, fin=None):
    # Establecer el valor de 'fin' si no se proporciona
    if fin is None:
        fin = len(arr) - 1
    
    # Verificar si el rango de búsqueda es válido
    if inicio > fin:
        return -1  # Elemento no encontrado
    
    # Calcular el índice medio del rango actual
    medio = (inicio + fin) // 2
    
    # Comprobar si el elemento objetivo está en el índice medio
    if arr[medio] == objetivo:
        return medio
    # Si el elemento objetivo es mayor que el elemento medio, buscar en la mitad derecha del rango
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, fin)
    # Si el elemento objetivo es menor que el elemento medio, buscar en la mitad izquierda del rango
    else:
        return busqueda_binaria_recursiva(arr, objetivo, inicio, medio - 1)
    
try:
    # Solicitar al usuario que ingrese la lista de números ordenados
    arr_input = input("Ingrese la lista ordenada de números separados por espacios: ").split()
    arr = [int(x) for x in arr_input]  # Convertir los elementos de la lista a enteros
except ValueError:
    print("Error: La lista contiene caracteres no numéricos.")
    exit()

# Solicitar al usuario que ingrese el elemento que desea buscar
elemento_objetivo = input("Ingrese el elemento que desea buscar en la lista: ")

# Verificar si la lista está ordenada
if arr != sorted(arr):
    print("Error: La lista ingresada no está ordenada.")
else:
    try:
        elemento_objetivo = int(elemento_objetivo)
        # Realizar la búsqueda binaria recursiva
        indice = busqueda_binaria_recursiva(arr, elemento_objetivo)
        # Imprimir el resultado de la búsqueda
        if indice != -1:
            print(f"El elemento {elemento_objetivo} se encuentra en el índice {indice}.")
        else:
            print(f"El elemento {elemento_objetivo} no se encuentra en la lista.")
    except ValueError:
        print("Error: El elemento a buscar no es un número válido.")