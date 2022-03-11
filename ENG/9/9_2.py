fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("No se encuentra el archivo")
    exit()

cont = 0

diassemana = dict()
for line in fhand:
    line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    if line.startswith("From:"): #Con esto me quito las lineas que empiezan por "From:" Paso a la siguiente línea del archivo.
        continue

    if line.startswith("From"):
        temp = line.split() #Me guarda en una lista cada una de las palabras de la línea
        word = temp[2]
        if word not in diassemana:
            diassemana[word] = 1
        else:
            diassemana[word] = diassemana[word] + 1

print(diassemana)