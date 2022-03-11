import string

nombre = input("Ingresa un nombre de archivo: ")

try:
    mf = open(nombre)
except:
    print("No se encuentra el archivo")
    exit()

dicc = dict()

for linea in mf:
    #linea = linea.split() #Convierte cadena (es el renglón) en una lista con las palabras
    #Ahora solo quiero una cadena completa
    linea = linea.rstrip()
    linea = linea.translate(str.maketrans('', '', string.punctuation))
    linea = linea.translate(str.maketrans('', '', ' '))

    linea = linea.lower()
    for letra in linea:
        if letra not in dicc:
            dicc[letra] = 1
        else:
            dicc[letra] += 1

lista = list()
for letra, contador in dicc.items():
    lista.append((contador, letra))

lista.sort(reverse=True)

for letra, contador in lista:
    print(letra, contador)