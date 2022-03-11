nombre = 'romeo.txt'

try:
    mf = open(nombre)
except:
    print("No se encuentra el archivo")
    exit()

lista = ['hola', 'prueba']

for linea in mf:
    linea = linea.rstrip()
    dividido = linea.split()

    for palabra in dividido:
        encontrado = 0
        i = 0
        while (i<(len(lista)) and encontrado == 0): #Aquí es and. En cuanto una de las dos falla, termina el bucle.
            if palabra == lista[i]:
                encontrado = 1
            i = i + 1
        if encontrado == 0:
            lista.append(palabra)

lista.sort()
print(lista)