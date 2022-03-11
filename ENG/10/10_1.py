fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("No se encuentra el archivo")
    exit()

cont = 0

cantidad = dict()
for line in fhand:
    line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    if line.startswith("From:"): #Con esto me quito las lineas que empiezan por "From:" Paso a la siguiente línea del archivo.
        continue

    if line.startswith("From"):
        temp = line.split() #Me guarda en una lista cada una de las palabras de la línea
        email = temp[1]

        if email not in cantidad:
            cantidad[email] = 1
        else:
            cantidad[email] = cantidad[email] + 1

lista = list()
for key, val in list(cantidad.items()):
    lista.append((val,key))

lista.sort(reverse=True) #La ordenamos en orden inverso en función de la cantidad
print(lista[0][1], lista[0][0])
