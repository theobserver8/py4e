def cuenta(cadena, letra):
    contador = 0
    for char in cadena:
        if letra == char:
            contador = contador + 1
    return contador

cadena = input('Introduzca una cadena: ')
letra = input('Introduzca letra a contar: ')
contador = cuenta(cadena, letra)

print(letra + " aparece " + str(contador) + " veces")