fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("No se encuentra el archivo")
    exit()

cont = 0

for line in fhand:
    #line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    if line.startswith("From:"): #Con esto me quito las lineas que empiezan por "From:" Paso a la siguiente línea.
        continue

    if line.startswith("From"):
        temp = line.split() #Me guarda en una lista cada una de las palabras de la línea
        print(temp[1])
        cont = cont + 1

print("There were %d lines in the file with From as the first word" % cont)