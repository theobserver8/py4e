try:
    fhand = open("romeo.txt")
except:
    print("No se encuentra el archivo")
    exit()

lista = [] #Definimos la lista vacia

for line in fhand:
    line = line.rstrip() #Me quita el salto de linea en las lineas leidas
    temp = line.split() #Me guarda en una lista cada una de las palabras de la línea

    
    for i in range(len(temp)):  #Recorro el renglón que estoy leyendo entero.
        enc = 0  #Establezco a cero el check de encontrado
        for j in range(len(lista)): #Recorro toda la lista
            if temp[i] == lista[j]: #Si el temporal coincide con un elemento de la lista significa que:
                enc = 1 #Que lo he encontrado
                continue #No sigo mirando en la lista. Me salgo del for de la lista.
        if enc != 1: #Si no lo he encontrado añado el temporal a la lista. Y al empezar paso a la siguiente palabra del temporal
            lista.append(temp[i])

lista.sort() #Ordena por orden alfabético
print (lista)
