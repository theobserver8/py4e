nombre = input("Intrdouce nombre del archivo: ")

try:
    mf = open(nombre)
except:
    print("No se encuentra el archivo")
    exit()

contador = 0
total = 0

for linea in mf:
    linea = linea.rstrip() #Me quita el salto de linea en las líneas leídas
    if linea.startswith('X-DSPAM-Confidence'):
        linea_mod = linea
        pos = linea_mod.find(':')
        numero = linea_mod[pos+2:] #Paso a la siguiente que es el espacio en blanco. Y a la siguiente que es la primera cifra. La última que es el \n no se incluye.
        #print(repr(numero)) Nos permite comprobar que la cadena es correcta. Si hay o no '\n', espacios, etc.
        numero = float(numero)
        total = total + numero

        contador = contador + 1

    else:
        continue

media = total / contador
#print("Promedio spam confidence: %g" % media) #Si lo ponemos así, reduce a 6 decimales
print("Promedio spam confidence: ", media)