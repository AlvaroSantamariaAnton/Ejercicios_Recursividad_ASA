def es_palindromo(texto):
    # Filtrar el texto para conservar solo caracteres alfanuméricos
    texto_filtrado = ''
    for caracter in texto:
        if caracter.isalnum():
            texto_filtrado += caracter.lower()
    
    # Sustituir los caracteres acentuados por su equivalente sin acento
    texto_filtrado = texto_filtrado.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    
    # Verificar que el texto filtrado es igual a su imagen reflejada
    return texto_filtrado == texto_filtrado[::-1]

# Pedir al usuario que introduzca una o varias frases
frases_usuario = input("Introduce una o varias frases separadas por coma: ").split(',')

# Comprobar si las frases son palíndromas
for frase in frases_usuario:
    frase = frase.strip()  # Eliminar espacios en blanco al inicio y al final de la frase
    if frase:
        if es_palindromo(frase):
            print('La frase "{}" es un palíndromo.'.format(frase))
        else:
            print('La frase "{}" no es un palíndromo.'.format(frase))
    else:
        print("Por favor, introduce una frase válida.")