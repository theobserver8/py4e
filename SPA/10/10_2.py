nombre = input("Ingresa un nombre de archivo: ")

try:
    mf = open(nombre)
except:
    print("No se encuentra el archivo")
    exit()

dicc = dict()

for linea in mf:
    if linea.startswith("From"):
        if linea.startswith("From:"):
            continue
        else:
            linea = linea.split() #Convierte cadena (es el renglón) en una lista con las palabras
            tiempo = linea[5]
            delimiter = ':'
            tiempo = tiempo.split(delimiter)
            hora = tiempo[0]

            if hora not in dicc:
                dicc[hora] = 1
            else:
                dicc[hora] += 1

lista = list()
for hora, contador in dicc.items():
    lista.append((hora, contador)) #Un parentesis por el append y el otro porque tiene que forma una tupla.

lista.sort()
for hora, contador in lista:
    print(hora, contador) #Hago esto para que me las muestre con salto de linea