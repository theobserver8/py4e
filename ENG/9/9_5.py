fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("No se encuentra el archivo")
    exit()

cont = 0

histogram = dict()
for line in fhand:
    line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    if line.startswith("From:"): #Con esto me quito las lineas que empiezan por "From:" Paso a la siguiente línea del archivo.
        continue

    if line.startswith("From"):
        #temp = line.split() #Me guarda en una lista cada una de las palabras de la línea
        #word = temp[1]

        inicial = line.find('@')
        final = line.find(' ', inicial)
        host = line[inicial+1:final]

        if host not in histogram:
            histogram[host] = 1
        else:
            histogram[host] = histogram[host] + 1

print(histogram)