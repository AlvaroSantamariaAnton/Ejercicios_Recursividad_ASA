def organizar_fichas_rvb(num_rojo, num_verde, num_azul):
    # Crear una lista de fichas con la cantidad especificada de cada color
    fichas = ['rojo'] * num_rojo + ['verde'] * num_verde + ['azul'] * num_azul
    
    # Índices para insertar las próximas fichas de cada color
    idx_rojo = 0  # Siguiente posición para una ficha roja
    idx_verde = num_rojo  # Siguiente posición para una ficha verde
    idx_azul = num_rojo + num_verde  # Siguiente posición para una ficha azul
    
    # Iterar sobre las fichas y colocarlas en sus posiciones correctas
    for i in range(len(fichas)):
        if fichas[i] == 'verde':
            fichas[idx_verde] = 'verde'
            idx_verde += 1
        elif fichas[i] == 'azul':
            fichas[idx_azul] = 'azul'
            idx_azul += 1
    
    return fichas

# Solicitar al usuario la cantidad de fichas de cada color
num_rojo = int(input("Ingrese el número de fichas rojas: "))
num_verde = int(input("Ingrese el número de fichas verdes: "))
num_azul = int(input("Ingrese el número de fichas azules: "))

# Organizar las fichas en el orden RVB
fichas_ordenadas = organizar_fichas_rvb(num_rojo, num_verde, num_azul)

# Mostrar el resultado
print("Fichas ordenadas:", fichas_ordenadas)