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

            pos_ini = direccion.find('@')
            dominio = direccion[pos_ini+1:] #Como ya tengo guardada la dirección, salto desde la siguente posición del @ hasta el final.

            if dominio not in dicc:
                dicc[dominio] = 1
            else:
                dicc[dominio] += 1

print(dicc)