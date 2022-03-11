lista = []

while(True):
    inp = input('Ingresa un número: ')
    if inp == 'hecho':
        break
    valor = float(inp)
    lista.append(valor)

print("Máximo: ", max(lista))
print("Mínimo: ", min(lista))