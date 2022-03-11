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
            linea = linea.split()
            direccion = linea[1]

            if direccion not in dicc:
                dicc[direccion] = 1
            else:
                dicc[direccion] += 1

valores = list(dicc.values())
maximo = max(valores)

for clave in dicc:
    if dicc[clave] == maximo:
        print(clave, maximo)