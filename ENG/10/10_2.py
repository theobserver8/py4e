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
        tiempo = temp[5]

        hora, minuto, segundo = tiempo.split(':')

        if hora not in cantidad:
            cantidad[hora] = 1
        else:
            cantidad[hora] = cantidad[hora] + 1

lista = list()
for key, val in list(cantidad.items()):
    lista.append((key, val))

lista.sort()
for key, val in lista:
    print(key, val)
