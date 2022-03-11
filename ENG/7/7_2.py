fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("No se encuentra el archivo")
    exit()

count = 0
sum = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        posini = line.find(" ") #Me encuentra la posición del primer espacio en blanco de la linea
        posfin = line.find("\n") #Me encuentra la posicion del barra n

        number = line[posini+1:posfin] #Me hace un slice entre las dos posiciones anteriores
        number = float(number) #Convierto a float ese string (que es el numero que busco)
        count = count + 1
        sum = sum + number

media = sum/count
print(media)