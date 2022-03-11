numero = input("Introduzca un numero: ")

total = 0
cantidad = 0

while True:
    try:
        if numero == 'fin':
            break
        numero = float(numero)
        total = total + numero
        cantidad = cantidad + 1
        numero = input("Introduzca un numero: ")
    except:
        print("Entrada inválida")
        numero = input("Introduzca un numero: ")

media = total/cantidad
print(total, cantidad, media)