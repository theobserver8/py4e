numero = input("Introduzca un numero: ")

cantidad = 0
total = 0
mayor = numero
menor = numero

while True:
    try:
        if numero == 'fin':
            break
        numero = float(numero)

        if cantidad == 0:
            mayor = numero
            menor = numero
        else:
            if numero > mayor:
                mayor = numero
            elif numero < menor:
                menor = numero

        total = total + numero
        cantidad = cantidad + 1
        numero = input("Introduzca un numero: ")
    except:
        print("Entrada inválida")
        numero = input("Introduzca un numero: ")

print(total, cantidad, mayor, menor)