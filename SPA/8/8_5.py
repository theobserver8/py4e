nombre = input("Intrdouce un nombre de archivo: ")

try:
    mf = open(nombre)
except:
    print("No se encuentra el archivo")
    exit()

contador = 0

for linea in mf:
    linea = linea.rstrip()
    if linea.startswith('From'):
        if linea.startswith('From:'):
            continue
        else:
            dividido = linea.split()
            print(dividido[1]) #la segunda palabra. Posicion 1.
            contador = contador + 1

print("Hay %d lineas en el archivo con la palabra From al inicio" % contador)