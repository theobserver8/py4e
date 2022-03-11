import string

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("No se encuentra el archivo")
    exit()

cantidad = dict()
for line in fhand:
    line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    line = line.translate(str.maketrans('','', string.punctuation)) #Elimino todos los signos de puntuación y me convierte los espacios a nada
    line = line.translate(str.maketrans('','', " "))
    line = line.lower() #Convierto todas las letras a minúscula
    for letter in line:
        if letter not in cantidad:
            cantidad[letter] = 1
        else:
            cantidad[letter] = cantidad[letter] + 1

lista = list()
for key, val in list(cantidad.items()):
    lista.append((val, key))

lista.sort(reverse=True)

for key, val in lista:
    print(key, val)
