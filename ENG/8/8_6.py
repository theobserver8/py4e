lista = []

while (True):
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    lista.append(value)

print("Maximum: ", max(lista))
print("Minimum: ", min(lista))