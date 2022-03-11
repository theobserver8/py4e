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
            dia = linea[2]
            if dia not in dicc:
                dicc[dia] = 1
            else:
                dicc[dia] += 1

print(dicc) 