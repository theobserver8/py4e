#nombre = input("Intrdouce nombre del archivo: ")
nombre = 'mbox-short.txt'

try:
    mf = open(nombre)
except:
    print("No se encuentra el archivo")
    exit()


for linea in mf:
    linea = linea.rstrip() #Me quita el salto de linea en las líneas leídas
    linea_mod = linea.upper() #Funcion que convierte a mayúsculas la línea leída
    print(linea_mod)