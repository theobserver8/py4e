posicion = 0
indice = 0
cadena = input("Introduzca una cadena: ")

while indice < len(cadena):
    posicion = posicion - 1
    print(cadena[posicion])
    indice = indice + 1