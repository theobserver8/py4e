nombre = input("Intrdouce nombre del archivo: ")

if nombre == "na na boo boo":
    print("NA NA BOO BOO PARA TI - Te he atrapado!")

else:
    try:
        mf = open(nombre)
    except:
        print("No se encuentra el archivo")
        exit()

    contador = 0
    total = 0

    for linea in mf:
        contador = contador + 1

    print("Hay %d líneas subject en %s" %(contador, nombre))