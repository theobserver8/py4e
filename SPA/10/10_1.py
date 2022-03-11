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
            direccion = linea[1]
            if direccion not in dicc:
                dicc[direccion] = 1
            else:
                dicc[direccion] += 1

lista = list()
for email, contador in dicc.items():
    lista.append((contador, email)) #Un parentesis por el append y el otro porque tiene que forma una tupla.

lista.sort(reverse=True)
print(lista[0][1], lista[0][0])