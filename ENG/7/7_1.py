try:
    fhand = open("mbox-short.txt")
except:
    print("No se encuentra el archivo")
    exit()

for line in fhand:
    line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    new_line = line.upper() #Funciona que convierte a mayusculas la linea leida
    print(new_line)